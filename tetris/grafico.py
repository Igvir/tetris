"""Leccion 5: colisiones y fusion (estilo numeros).

Mismo bucle de juego que en la Leccion 4, pero ahora las piezas se DETIENEN al
tocar el fondo u otra pieza y se quedan pegadas (fusionadas) al tablero.
Seguimos dibujando la matriz con NUMEROS.
"""

import pygame

from .juego import Juego
from . import tablero as tab

TAM = 30
FONDO = (10, 10, 20)
REJILLA = (40, 40, 55)
BLANCO = (240, 240, 240)

INTERVALO_CAIDA = 500   # milisegundos entre cada descenso automatico


def dibujar_tablero(pantalla, fuente, matriz):
    for fila in range(len(matriz)):
        for col in range(len(matriz[fila])):
            x = col * TAM
            y = fila * TAM
            rect = pygame.Rect(x, y, TAM, TAM)
            pygame.draw.rect(pantalla, REJILLA, rect, 1)
            numero = matriz[fila][col]
            if numero != 0:
                texto = fuente.render(str(numero), True, BLANCO)
                pantalla.blit(texto, texto.get_rect(center=rect.center))


def ejecutar():
    pygame.init()
    pantalla = pygame.display.set_mode((tab.ANCHO * TAM, tab.ALTO * TAM))
    pygame.display.set_caption("Tetris con Matrices - Leccion 5 (colisiones y fusion)")
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("consolas", 20)

    juego = Juego()
    tiempo = 0
    corriendo = True
    while corriendo:
        tiempo += reloj.tick(60)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    juego.mover(-1)
                elif evento.key == pygame.K_RIGHT:
                    juego.mover(1)
                elif evento.key == pygame.K_UP:
                    juego.rotar()
                elif evento.key == pygame.K_DOWN:
                    juego.bajar()
                elif evento.key == pygame.K_ESCAPE:
                    corriendo = False

        # Caida automatica por tiempo.
        if tiempo >= INTERVALO_CAIDA:
            tiempo = 0
            juego.bajar()

        pantalla.fill(FONDO)
        dibujar_tablero(pantalla, fuente, juego.tablero_con_pieza())
        pygame.display.flip()

    pygame.quit()
