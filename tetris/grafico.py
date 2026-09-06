"""Presentacion del juego en una ventana de Pygame.

PLANTILLA DE INICIO: completa el dibujo y el bucle de juego siguiendo la guia
del estudiante (Lecciones 3, 4, 6, 7 y 8). Reutiliza la clase Juego sin cambios.

Estilos de dibujo:
- ESTILO_NUMEROS: dibuja el numero de cada casilla (Lecciones 3-6).
- ESTILO_NEON:    pinta cada casilla con su color neon (Leccion 7).
"""

import pygame

from . import audio
from .juego import Juego
from .piezas import COLORES
from . import tablero as tab

TAM = 30                      # tamano en pixeles de cada celda
MARGEN_LATERAL = 160          # espacio a la derecha para la puntuacion
FONDO = (10, 10, 20)          # fondo oscuro
REJILLA = (40, 40, 55)        # color de las lineas de la cuadricula
BLANCO = (240, 240, 240)

ESTILO_NUMEROS = "numeros"
ESTILO_NEON = "neon"

INTERVALO_CAIDA = 500         # milisegundos entre descensos automaticos
FRAMES_ANIMACION = 8          # duracion del destello al fusionar (Leccion 8)


def dibujar_celda_numeros(pantalla, fuente, fila, col, numero):
    """Dibuja una celda con su numero (Leccion 3).

    TODO (Leccion 3): dibuja el borde de la celda y, si numero != 0, el numero
    como texto centrado.
    """
    raise NotImplementedError("Completa dibujar_celda_numeros en la Leccion 3")


def dibujar_celda_neon(pantalla, fuente, fila, col, numero):
    """Dibuja una celda con su color neon (Leccion 7).

    TODO (Leccion 7): pinta el fondo si numero == 0, o el color COLORES[numero]
    con un contorno claro si esta ocupada.
    """
    raise NotImplementedError("Completa dibujar_celda_neon en la Leccion 7")


class Presentacion:
    """Ventana de Pygame que ejecuta el juego con el estilo elegido.

    TODO (Lecciones 3-8): completa el dibujo del tablero, el panel de puntuacion,
    la animacion de destello y el bucle de juego con el teclado.
    """

    def __init__(self, estilo=ESTILO_NEON):
        self.estilo = estilo
        self.juego = Juego()
        self.animacion_frames = 0
        self.celdas_destello = []

    def _dibujar_celda(self, pantalla, fuente, fila, col, numero):
        if self.estilo == ESTILO_NUMEROS:
            dibujar_celda_numeros(pantalla, fuente, fila, col, numero)
        else:
            dibujar_celda_neon(pantalla, fuente, fila, col, numero)

    def _dibujar(self, pantalla, fuente, fuente_grande):
        """TODO (Lecciones 3, 6, 8): rellena el fondo, recorre tablero_con_pieza(),
        dibuja cada celda, el panel de puntuacion y la animacion de destello."""
        raise NotImplementedError("Completa el dibujo en las Lecciones 3, 6 y 8")

    def ejecutar(self):
        """TODO (Lecciones 3-4): inicializa Pygame, crea la ventana y el reloj,
        y ejecuta el bucle de juego leyendo el teclado (mover, rotar, bajar) y
        aplicando la caida automatica por tiempo."""
        raise NotImplementedError("Completa el bucle de juego en las Lecciones 3 y 4")


def jugar(estilo=ESTILO_NEON):
    """Punto de entrada de alto nivel: crea la ventana y ejecuta el juego."""
    Presentacion(estilo=estilo).ejecutar()
