"""Genera sonidos sencillos para el juego usando solo la libreria estandar.

Crea dos archivos WAV ligeros en assets/sonidos/:
- giro.wav  : un "clic" corto y agudo para cuando se rota una pieza.
- linea.wav : un pequeno arpegio ascendente para cuando se elimina una fila.

No requiere dependencias externas (solo `wave`, `math` y `struct`). Ejecuta:

    python tools/generar_sonidos.py
"""

import math
import os
import struct
import wave

FRECUENCIA_MUESTREO = 44100   # muestras por segundo
CARPETA = os.path.join(os.path.dirname(__file__), "..", "assets", "sonidos")


def _escribir_wav(ruta, muestras):
    """Escribe una lista de muestras (float entre -1 y 1) como WAV mono 16 bits."""
    with wave.open(ruta, "w") as w:
        w.setnchannels(1)          # mono
        w.setsampwidth(2)          # 16 bits
        w.setframerate(FRECUENCIA_MUESTREO)
        cuadros = b"".join(
            struct.pack("<h", int(max(-1.0, min(1.0, m)) * 32767)) for m in muestras
        )
        w.writeframes(cuadros)


def _tono(frecuencia, duracion, volumen=0.5):
    """Genera un tono con una envolvente suave para que no suene brusco."""
    total = int(FRECUENCIA_MUESTREO * duracion)
    muestras = []
    for i in range(total):
        t = i / FRECUENCIA_MUESTREO
        # Envolvente: sube y baja para evitar chasquidos al inicio/fin.
        envolvente = math.sin(math.pi * i / total)
        muestras.append(volumen * envolvente * math.sin(2 * math.pi * frecuencia * t))
    return muestras


def generar_giro():
    """Un clic corto y agudo (una sola nota breve)."""
    return _tono(880, 0.08, volumen=0.4)


def generar_linea():
    """Un arpegio ascendente de tres notas para celebrar la linea."""
    muestras = []
    for frecuencia in (523, 659, 784):   # do, mi, sol
        muestras.extend(_tono(frecuencia, 0.10, volumen=0.5))
    return muestras


def main():
    carpeta = os.path.normpath(CARPETA)
    os.makedirs(carpeta, exist_ok=True)
    _escribir_wav(os.path.join(carpeta, "giro.wav"), generar_giro())
    _escribir_wav(os.path.join(carpeta, "linea.wav"), generar_linea())
    print("Sonidos generados en:", carpeta)


if __name__ == "__main__":
    main()
