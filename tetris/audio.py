"""Sonidos del juego con pygame.mixer.

El audio es OPCIONAL y degradable: si el mezclador no arranca o falta un
archivo de sonido, el juego continua sin fallar. Toda esta logica vive en la
capa de presentacion; la logica de matrices no depende de ella.
"""

import os

import pygame

# ---------------------------------------------------------------------------
# SEGURIDAD: carpeta de sonidos como ruta absoluta y normalizada
# ---------------------------------------------------------------------------
# os.path.abspath() convierte "tetris/../assets/sonidos" en una ruta completa
# y sin ".." (por ejemplo C:\...\tetris\assets\sonidos). La guardamos ya
# normalizada porque mas abajo la usamos como "frontera": todo archivo que
# carguemos debe quedar DENTRO de esta carpeta.
#
# ¿Por que importa? A esto se le llama defensa ante "path traversal" (recorrido
# de rutas): si un nombre de archivo contuviera algo como "../../secreto.txt",
# sin esta comprobacion el programa podria leer archivos de fuera de la carpeta
# prevista. En este juego los nombres son fijos, pero lo dejamos como buen
# habito y ejemplo educativo de como se valida una ruta.
_CARPETA = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "assets", "sonidos")
)

# Nombre logico -> archivo esperado dentro de assets/sonidos/.
_ARCHIVOS = {
    "giro": "giro.wav",
    "linea": "linea.wav",
}

_sonidos = {}
_activo = False


def _ruta_segura(archivo):
    """Resuelve `archivo` dentro de la carpeta de sonidos de forma segura.

    [SEGURIDAD - validacion de rutas]
    Devuelve la ruta absoluta solo si queda contenida dentro de `_CARPETA`.
    Si el nombre intenta salirse (por ejemplo con "..") devuelve None, de modo
    que nunca cargamos un archivo fuera de assets/sonidos/.

    Idea clave: primero construimos la ruta final y la normalizamos, y DESPUES
    comprobamos donde quedo. Nunca confiamos en el nombre tal cual: confiamos en
    el resultado ya resuelto. Asi, aunque el nombre tenga "..", el "startswith"
    detecta que la ruta se salio de la carpeta y la rechazamos.
    """
    # Paso 1: unir carpeta + nombre y resolver ".." a una ruta absoluta real.
    ruta = os.path.abspath(os.path.join(_CARPETA, archivo))

    # Paso 2: anadir el separador final ("sonidos\") evita un falso positivo:
    # sin el, una carpeta vecina como "...\sonidos_malos" empezaria igual que
    # "...\sonidos" y pasaria el filtro por error.
    carpeta_con_sep = os.path.join(_CARPETA, "")

    # Paso 3: solo aceptamos la ruta si es la propia carpeta o algo dentro de ella.
    if ruta == _CARPETA or ruta.startswith(carpeta_con_sep):
        return ruta
    return None  # La ruta se salio de assets/sonidos/: la rechazamos.


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
        # [SEGURIDAD] Validamos la ruta ANTES de tocar el disco. Si _ruta_segura
        # devuelve None, el nombre apuntaba fuera de la carpeta y lo saltamos.
        # os.path.isfile comprueba ademas que exista y sea un archivo (no una
        # carpeta), para no pasarle a pygame algo que no puede cargar.
        ruta = _ruta_segura(archivo)
        if ruta and os.path.isfile(ruta):
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
