"""Leccion 3: la ventana de Pygame que dibuja la matriz con NUMEROS.

Abrimos una ventana y dibujamos la cuadricula de 10x20. Recorremos la matriz
del tablero con dos bucles anidados (fila, luego columna) y dibujamos el numero
de cada casilla como texto. Las casillas con 0 se ven vacias.

Todavia no hay piezas que caigan: eso llega en la Leccion 4. Aqui el objetivo
es ver los NUMEROS de la matriz dibujados en pantalla.
"""

import pygame

from . import tablero as tab

TAM = 30                 # tamano en pixeles de cada celda
FONDO = (10, 10, 20)     # fondo oscuro
REJILLA = (40, 40, 55)   # lineas de la cuadricula
BLANCO = (240, 240, 240)


def dibujar_tablero(pantalla, fuente, tablero):
    """Dibuja la cuadricula y el numero de cada casilla."""
    for fila in range(len(tablero)):            # recorre filas (0..19)
        for col in range(len(tablero[fila])):   # recorre columnas (0..9)
            x = col * TAM
            y = fila * TAM
            rect = pygame.Rect(x, y, TAM, TAM)
            pygame.draw.rect(pantalla, REJILLA, rect, 1)   # borde de la celda
            numero = tablero[fila][col]
            if numero != 0:
                texto = fuente.render(str(numero), True, BLANCO)
                pantalla.blit(texto, texto.get_rect(center=rect.center))


def ejecutar(tablero):
    """Abre la ventana y dibuja el tablero recibido hasta que se cierre."""
    pygame.init()
    ancho_ventana = tab.ANCHO * TAM
    alto_ventana = tab.ALTO * TAM
    pantalla = pygame.display.set_mode((ancho_ventana, alto_ventana))
    pygame.display.set_caption("Tetris con Matrices - Leccion 3 (numeros)")
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("consolas", 20)

    corriendo = True
    while corriendo:
        reloj.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                corriendo = False

        pantalla.fill(FONDO)
        dibujar_tablero(pantalla, fuente, tablero)
        pygame.display.flip()

    pygame.quit()
