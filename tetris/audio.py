"""Sonidos del juego con pygame.mixer.

PLANTILLA DE INICIO: completa las funciones marcadas con TODO en la Leccion 8.
El audio es OPCIONAL y degradable: si el mezclador no arranca o falta un archivo,
el juego debe continuar sin fallar. Toda esta logica vive en la presentacion.
"""

import os

import pygame

_CARPETA = os.path.join(os.path.dirname(__file__), "..", "assets", "sonidos")
_ARCHIVOS = {
    "giro": "giro.wav",
    "linea": "linea.wav",
}

_sonidos = {}
_activo = False


def iniciar_audio():
    """Inicializa el mezclador de forma segura. Si falla, desactiva el audio.

    TODO (Leccion 8): inicializa pygame.mixer dentro de un try/except y guarda
    en `_activo` si el audio quedo disponible.
    """
    # De momento el audio queda desactivado hasta que lo implementes.
    global _activo
    _activo = False


def cargar_sonidos():
    """Carga los archivos de sonido disponibles. Ignora los que falten.

    TODO (Leccion 8): si el audio esta activo, carga cada archivo de _ARCHIVOS
    que exista en la carpeta de sonidos.
    """
    # TODO: implementa la carga de sonidos en la Leccion 8.
    return


def reproducir(nombre):
    """Reproduce un sonido si el audio esta disponible y el sonido existe.

    Si no hay audio o falta el sonido, no hace nada (degradacion silenciosa).
    """
    if _activo and nombre in _sonidos:
        _sonidos[nombre].play()
