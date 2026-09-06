"""Leccion 4: la pieza que cae.

Creamos la clase Juego, que guarda el estado de la pieza activa (que pieza,
que rotacion y en que fila/columna esta). La pieza cae sola con el tiempo, y el
jugador puede moverla y rotarla. En esta leccion, al llegar al fondo la pieza
simplemente vuelve a aparecer arriba: TODAVIA NO se acumula. La acumulacion
(fusion) llega en la Leccion 5.
"""

from . import piezas
from . import tablero as tab


class Juego:
    """Mantiene el estado del juego y aplica las reglas sobre las matrices."""

    def __init__(self):
        self.tablero = tab.crear_tablero()
        self.pieza = None
        self.rotacion = 0
        self.fila = 0
        self.columna = 0
        self.nueva_pieza()

    def matriz_pieza_actual(self):
        """Devuelve la matriz de la rotacion actual de la pieza activa."""
        return piezas.PIEZAS[self.pieza][self.rotacion]

    def nueva_pieza(self):
        """Genera una pieza nueva arriba y al centro del tablero."""
        self.pieza = piezas.pieza_aleatoria()
        self.rotacion = 0
        self.fila = 0
        ancho_pieza = len(self.matriz_pieza_actual()[0])
        self.columna = tab.ANCHO // 2 - ancho_pieza // 2

    def mover(self, dx):
        """Mueve la pieza dx columnas (-1 izquierda, +1 derecha) si es valido."""
        if tab.es_valida(self.tablero, self.matriz_pieza_actual(),
                         self.fila, self.columna + dx):
            self.columna += dx

    def rotar(self):
        """Pasa a la siguiente rotacion (ciclica) solo si la nueva cabe."""
        siguiente = (self.rotacion + 1) % len(piezas.PIEZAS[self.pieza])
        matriz = piezas.PIEZAS[self.pieza][siguiente]
        if tab.es_valida(self.tablero, matriz, self.fila, self.columna):
            self.rotacion = siguiente

    def bajar(self):
        """Baja una fila. Si no puede, por ahora reaparece arriba (sin fusionar)."""
        if tab.es_valida(self.tablero, self.matriz_pieza_actual(),
                         self.fila + 1, self.columna):
            self.fila += 1
        else:
            self.nueva_pieza()

    def tablero_con_pieza(self):
        """Devuelve una COPIA del tablero con la pieza activa dibujada."""
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
