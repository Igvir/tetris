"""Presentacion del juego en una ventana de Pygame.

Contiene el bucle de juego, la lectura del teclado, el dibujo del tablero y
las animaciones. Reutiliza la clase Juego sin cambios.

Estilos de dibujo:
- ESTILO_NUMEROS: dibuja el numero de cada casilla (Etapa 1).
- ESTILO_NEON:    pinta cada casilla con su color neon (Etapa 2).
"""

import pygame

from . import audio
from .juego import Juego
from .piezas import COLORES
from . import tablero as tab

TAM = 30                      # tamano en pixeles de cada celda
MARGEN_LATERAL = 160          # espacio a la derecha para la puntuacion
FONDO = (10, 10, 20)          # fondo oscuro para resaltar el neon
REJILLA = (40, 40, 55)        # color de las lineas de la cuadricula
BLANCO = (240, 240, 240)

ESTILO_NUMEROS = "numeros"
ESTILO_NEON = "neon"

# Velocidad de caida automatica (milisegundos entre descensos).
INTERVALO_CAIDA = 500

# Duracion de las animaciones en fotogramas.
FRAMES_ANIMACION = 8


def _dibujar_celda_numeros(pantalla, fuente, fila, col, numero):
    x, y = col * TAM, fila * TAM
    rect = pygame.Rect(x, y, TAM, TAM)
    pygame.draw.rect(pantalla, REJILLA, rect, 1)
    if numero != 0:
        texto = fuente.render(str(numero), True, BLANCO)
        rect_texto = texto.get_rect(center=rect.center)
        pantalla.blit(texto, rect_texto)


def _dibujar_celda_neon(pantalla, fuente, fila, col, numero):
    x, y = col * TAM, fila * TAM
    rect = pygame.Rect(x, y, TAM, TAM)
    if numero == 0:
        pygame.draw.rect(pantalla, FONDO, rect)
        pygame.draw.rect(pantalla, REJILLA, rect, 1)
    else:
        color = COLORES.get(numero, BLANCO)
        pygame.draw.rect(pantalla, color, rect.inflate(-2, -2))
        # Contorno claro para simular el brillo neon.
        pygame.draw.rect(pantalla, BLANCO, rect, 2)


class Presentacion:
    """Ventana de Pygame que ejecuta el juego con el estilo elegido."""

    def __init__(self, estilo=ESTILO_NEON):
        self.estilo = estilo
        self.juego = Juego()
        self.animacion_frames = 0
        self.celdas_destello = []

    def _dibujar_celda(self, pantalla, fuente, fila, col, numero):
        if self.estilo == ESTILO_NUMEROS:
            _dibujar_celda_numeros(pantalla, fuente, fila, col, numero)
        else:
            _dibujar_celda_neon(pantalla, fuente, fila, col, numero)

    def _dibujar(self, pantalla, fuente, fuente_grande):
        pantalla.fill(FONDO)
        matriz = self.juego.tablero_con_pieza()
        for fila in range(len(matriz)):
            for col in range(len(matriz[fila])):
                self._dibujar_celda(pantalla, fuente, fila, col, matriz[fila][col])

        # Animacion de destello: parpadeo blanco sobre las celdas recien fusionadas.
        if self.animacion_frames > 0 and (self.animacion_frames // 2) % 2 == 0:
            for (f, c) in self.celdas_destello:
                if 0 <= f < len(matriz) and 0 <= c < len(matriz[0]):
                    rect = pygame.Rect(c * TAM, f * TAM, TAM, TAM)
                    pygame.draw.rect(pantalla, BLANCO, rect)

        # Panel lateral con la puntuacion.
        x_panel = tab.ANCHO * TAM + 15
        texto_p = fuente.render("Puntos", True, BLANCO)
        pantalla.blit(texto_p, (x_panel, 20))
        valor_p = fuente_grande.render(str(self.juego.puntuacion), True, (0, 255, 255))
        pantalla.blit(valor_p, (x_panel, 45))

        texto_l = fuente.render("Lineas", True, BLANCO)
        pantalla.blit(texto_l, (x_panel, 100))
        valor_l = fuente_grande.render(str(self.juego.lineas), True, (255, 0, 255))
        pantalla.blit(valor_l, (x_panel, 125))

        if self.juego.terminado:
            texto_fin = fuente.render("FIN - R reinicia", True, (255, 49, 49))
            pantalla.blit(texto_fin, (x_panel, 200))

        pygame.display.flip()

    def _al_fusionar(self, celdas, lineas_eliminadas):
        """Dispara sonidos y animacion cuando una pieza aterriza."""
        self.celdas_destello = celdas
        self.animacion_frames = FRAMES_ANIMACION
        if lineas_eliminadas > 0:
            audio.reproducir("linea")

    def ejecutar(self):
        pygame.init()
        audio.iniciar_audio()
        audio.cargar_sonidos()

        ancho_ventana = tab.ANCHO * TAM + MARGEN_LATERAL
        alto_ventana = tab.ALTO * TAM
        pantalla = pygame.display.set_mode((ancho_ventana, alto_ventana))
        pygame.display.set_caption("Tetris con Matrices")
        reloj = pygame.time.Clock()
        fuente = pygame.font.SysFont("consolas", 20)
        fuente_grande = pygame.font.SysFont("consolas", 32, bold=True)

        tiempo_acumulado = 0
        corriendo = True
        while corriendo:
            dt = reloj.tick(60)
            tiempo_acumulado += dt

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False
                elif evento.type == pygame.KEYDOWN:
                    if self.juego.terminado:
                        if evento.key == pygame.K_r:
                            self.juego.reiniciar()
                        elif evento.key == pygame.K_ESCAPE:
                            corriendo = False
                        continue
                    if evento.key == pygame.K_LEFT:
                        self.juego.mover(-1)
                    elif evento.key == pygame.K_RIGHT:
                        self.juego.mover(1)
                    elif evento.key == pygame.K_UP:
                        if self.juego.rotar():
                            audio.reproducir("giro")
                    elif evento.key == pygame.K_DOWN:
                        celdas = self.juego.celdas_pieza_actual()
                        fusiono, lineas = self.juego.bajar()
                        if fusiono:
                            self._al_fusionar(celdas, lineas)
                    elif evento.key == pygame.K_SPACE:
                        celdas = self.juego.celdas_pieza_actual()
                        fusiono, lineas = self.juego.caida_rapida()
                        if fusiono:
                            self._al_fusionar(celdas, lineas)
                    elif evento.key == pygame.K_ESCAPE:
                        corriendo = False

            # Caida automatica por tiempo.
            if not self.juego.terminado and tiempo_acumulado >= INTERVALO_CAIDA:
                tiempo_acumulado = 0
                celdas = self.juego.celdas_pieza_actual()
                fusiono, lineas = self.juego.bajar()
                if fusiono:
                    self._al_fusionar(celdas, lineas)

            if self.animacion_frames > 0:
                self.animacion_frames -= 1

            self._dibujar(pantalla, fuente, fuente_grande)

        pygame.quit()


def jugar(estilo=ESTILO_NEON):
    """Punto de entrada de alto nivel: crea la ventana y ejecuta el juego."""
    Presentacion(estilo=estilo).ejecutar()
