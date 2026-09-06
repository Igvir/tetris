"""Logica del juego: la pieza activa, su movimiento y el estado global.

Esta clase solo manipula matrices de numeros. No sabe nada de graficos ni de
sonido; por eso se puede reutilizar tal cual en la version con numeros y en la
version con neon.
"""

from . import piezas
from . import tablero as tab

# Puntos segun cuantas lineas se eliminan a la vez.
PUNTOS_POR_LINEAS = {0: 0, 1: 100, 2: 300, 3: 500, 4: 800}


class Juego:
    """Mantiene el estado del juego y aplica las reglas sobre las matrices."""

    def __init__(self):
        self.tablero = tab.crear_tablero()
        self.puntuacion = 0
        self.lineas = 0
        self.terminado = False
        # Datos de la pieza activa (se rellenan en nueva_pieza).
        self.pieza = None
        self.rotacion = 0
        self.fila = 0
        self.columna = 0
        self.nueva_pieza()

    # --- Pieza activa -----------------------------------------------------

    def matriz_pieza_actual(self):
        """Devuelve la matriz de la rotacion actual de la pieza activa."""
        return piezas.PIEZAS[self.pieza][self.rotacion]

    def nueva_pieza(self):
        """Genera una pieza nueva arriba y al centro. Si no cabe, fin del juego."""
        self.pieza = piezas.pieza_aleatoria()
        self.rotacion = 0
        self.fila = 0
        ancho_pieza = len(self.matriz_pieza_actual()[0])
        self.columna = tab.ANCHO // 2 - ancho_pieza // 2
        if not tab.es_valida(self.tablero, self.matriz_pieza_actual(),
                             self.fila, self.columna):
            self.terminado = True

    # --- Movimiento -------------------------------------------------------

    def mover(self, dx):
        """Mueve la pieza dx columnas (-1 izquierda, +1 derecha) si es valido."""
        if tab.es_valida(self.tablero, self.matriz_pieza_actual(),
                         self.fila, self.columna + dx):
            self.columna += dx
            return True
        return False

    def rotar(self):
        """Pasa a la siguiente rotacion (ciclica) solo si la nueva cabe."""
        siguiente = (self.rotacion + 1) % len(piezas.PIEZAS[self.pieza])
        matriz = piezas.PIEZAS[self.pieza][siguiente]
        if tab.es_valida(self.tablero, matriz, self.fila, self.columna):
            self.rotacion = siguiente
            return True
        return False

    def bajar(self):
        """Baja una fila. Si no puede, fusiona, elimina lineas y saca pieza nueva.

        Devuelve una tupla (fusiono, lineas_eliminadas) para que la capa de
        presentacion pueda disparar sonidos y animaciones.
        """
        if tab.es_valida(self.tablero, self.matriz_pieza_actual(),
                         self.fila + 1, self.columna):
            self.fila += 1
            return (False, 0)

        # La pieza aterrizo: se une al tablero.
        tab.fusionar(self.tablero, self.matriz_pieza_actual(),
                     self.fila, self.columna)
        eliminadas = tab.eliminar_lineas(self.tablero)
        self.lineas += eliminadas
        self.puntuacion += PUNTOS_POR_LINEAS.get(eliminadas, 0)
        self.nueva_pieza()
        return (True, eliminadas)

    def caida_rapida(self):
        """Baja la pieza hasta el fondo de una sola vez y la fusiona."""
        while tab.es_valida(self.tablero, self.matriz_pieza_actual(),
                            self.fila + 1, self.columna):
            self.fila += 1
        return self.bajar()

    # --- Presentacion -----------------------------------------------------

    def tablero_con_pieza(self):
        """Devuelve una COPIA del tablero con la pieza activa dibujada.

        Se usa una copia para no modificar el tablero real hasta la fusion.
        """
        copia = [fila[:] for fila in self.tablero]
        matriz = self.matriz_pieza_actual()
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] != 0:
                    f = self.fila + i
                    c = self.columna + j
                    if 0 <= f < len(copia) and 0 <= c < len(copia[0]):
                        copia[f][c] = matriz[i][j]
        return copia

    def celdas_pieza_actual(self):
        """Lista de (fila, columna) ocupadas por la pieza activa en el tablero."""
        celdas = []
        matriz = self.matriz_pieza_actual()
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] != 0:
                    celdas.append((self.fila + i, self.columna + j))
        return celdas

    def reiniciar(self):
        """Reinicia el juego a su estado inicial."""
        self.__init__()
