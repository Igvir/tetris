"""Leccion 7: colores NEON (la logica no cambia, solo el dibujo).

Lo unico que cambia respecto a la Leccion 6 es como dibujamos una celda: en vez
de escribir el numero, pintamos un rectangulo con el color neon de esa pieza
sobre un fondo oscuro. La clase Juego, el tablero y las piezas no cambian nada:
por eso separar la logica de la presentacion es tan util.
"""

import pygame

from .juego import Juego
from .piezas import COLORES
from . import tablero as tab

TAM = 30
MARGEN_LATERAL = 160
FONDO = (10, 10, 20)
REJILLA = (40, 40, 55)
BLANCO = (240, 240, 240)

INTERVALO_CAIDA = 500


def dibujar_tablero(pantalla, fuente, matriz):
    for fila in range(len(matriz)):
        for col in range(len(matriz[fila])):
            x = col * TAM
            y = fila * TAM
            rect = pygame.Rect(x, y, TAM, TAM)
            numero = matriz[fila][col]
            if numero == 0:
                pygame.draw.rect(pantalla, FONDO, rect)
                pygame.draw.rect(pantalla, REJILLA, rect, 1)
            else:
                # Relleno con el color neon y contorno claro para el "brillo".
                pygame.draw.rect(pantalla, COLORES[numero], rect.inflate(-2, -2))
                pygame.draw.rect(pantalla, BLANCO, rect, 2)


def dibujar_panel(pantalla, fuente, fuente_grande, juego):
    x = tab.ANCHO * TAM + 15
    pantalla.blit(fuente.render("Puntos", True, BLANCO), (x, 20))
    pantalla.blit(fuente_grande.render(str(juego.puntuacion), True, (0, 255, 255)), (x, 45))
    pantalla.blit(fuente.render("Lineas", True, BLANCO), (x, 100))
    pantalla.blit(fuente_grande.render(str(juego.lineas), True, (255, 0, 255)), (x, 125))
    if juego.terminado:
        pantalla.blit(fuente.render("FIN", True, (255, 80, 80)), (x, 200))
        pantalla.blit(fuente.render("R reinicia", True, BLANCO), (x, 230))


def ejecutar():
    pygame.init()
    ancho_ventana = tab.ANCHO * TAM + MARGEN_LATERAL
    pantalla = pygame.display.set_mode((ancho_ventana, tab.ALTO * TAM))
    pygame.display.set_caption("Tetris con Matrices - Leccion 7 (neon)")
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("consolas", 20)
    fuente_grande = pygame.font.SysFont("consolas", 32, bold=True)

    juego = Juego()
    tiempo = 0
    corriendo = True
    while corriendo:
        tiempo += reloj.tick(60)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            elif evento.type == pygame.KEYDOWN:
                if juego.terminado:
                    if evento.key == pygame.K_r:
                        juego.reiniciar()
                    elif evento.key == pygame.K_ESCAPE:
                        corriendo = False
                    continue
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

        if not juego.terminado and tiempo >= INTERVALO_CAIDA:
            tiempo = 0
            juego.bajar()

        pantalla.fill(FONDO)
        dibujar_tablero(pantalla, fuente, juego.tablero_con_pieza())
        dibujar_panel(pantalla, fuente, fuente_grande, juego)
        pygame.display.flip()

    pygame.quit()
