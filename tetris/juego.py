"""Leccion 5: colisiones y fusion.

La clase Juego ahora detecta colisiones (con `es_valida`) y, cuando una pieza
no puede bajar mas, la FUSIONA con el tablero (copia su matriz) y genera una
pieza nueva. Asi las piezas se acumulan como en el Tetris clasico.
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
        """Baja una fila. Si no puede, FUSIONA la pieza y saca una nueva.

        Ahora las piezas se acumulan: al aterrizar, copiamos su matriz en el
        tablero (fusionar) y generamos una pieza nueva arriba.
        """
        if tab.es_valida(self.tablero, self.matriz_pieza_actual(),
                         self.fila + 1, self.columna):
            self.fila += 1
        else:
            tab.fusionar(self.tablero, self.matriz_pieza_actual(),
                         self.fila, self.columna)
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
