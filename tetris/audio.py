"""Sonidos del juego con pygame.mixer.

El audio es OPCIONAL y degradable: si el mezclador no arranca o falta un
archivo de sonido, el juego continua sin fallar. Toda esta logica vive en la
capa de presentacion; la logica de matrices no depende de ella.
"""

import os

import pygame

# Carpeta donde viven los sonidos.
_CARPETA = os.path.join(os.path.dirname(__file__), "..", "assets", "sonidos")

# Nombre logico -> archivo esperado dentro de assets/sonidos/.
_ARCHIVOS = {
    "giro": "giro.wav",
    "linea": "linea.wav",
}

_sonidos = {}
_activo = False


def iniciar_audio():
    """Inicializa el mezclador de forma segura. Si falla, desactiva el audio."""
    global _activo
    try:
        pygame.mixer.init()
        _activo = True
    except pygame.error:
        _activo = False


def cargar_sonidos():
    """Carga los archivos de sonido disponibles. Ignora los que falten."""
    if not _activo:
        return
    for nombre, archivo in _ARCHIVOS.items():
        ruta = os.path.join(_CARPETA, archivo)
        if os.path.exists(ruta):
            try:
                _sonidos[nombre] = pygame.mixer.Sound(ruta)
            except pygame.error:
                # Archivo invalido o formato no soportado: lo ignoramos.
                pass


def reproducir(nombre):
    """Reproduce un sonido si el audio esta disponible y el sonido existe.

    Si no hay audio o falta el sonido, no hace nada (degradacion silenciosa).
    """
    if _activo and nombre in _sonidos:
        _sonidos[nombre].play()
