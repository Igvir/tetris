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


def _ruta_dentro(carpeta, nombre):
    """Une `carpeta` + `nombre` asegurando que el resultado no se sale de ella.

    [SEGURIDAD - validacion de rutas al ESCRIBIR]
    Aqui el riesgo es el espejo del de audio.py: en lugar de leer, escribimos.
    Si un nombre contuviera "..", podriamos crear o sobrescribir un archivo
    fuera de assets/sonidos/ sin querer. Por eso resolvemos la ruta a absoluta
    y comprobamos que empiece por la carpeta de destino.

    Diferencia con la lectura: al escribir preferimos FALLAR de forma ruidosa
    (lanzar ValueError) en vez de ignorar en silencio, porque escribir en el
    sitio equivocado es un error que conviene ver de inmediato.
    """
    # Resolvemos ".." y normalizamos antes de decidir si la ruta es valida.
    destino = os.path.abspath(os.path.join(carpeta, nombre))
    # El separador final evita aceptar carpetas vecinas con prefijo parecido.
    carpeta_con_sep = os.path.join(carpeta, "")
    if not destino.startswith(carpeta_con_sep):
        raise ValueError("Nombre de archivo no permitido: %r" % (nombre,))
    return destino


def main():
    carpeta = os.path.abspath(CARPETA)
    os.makedirs(carpeta, exist_ok=True)
    # [SEGURIDAD] Pasamos cada nombre por _ruta_dentro() para garantizar que los
    # WAV solo se escriban dentro de assets/sonidos/.
    _escribir_wav(_ruta_dentro(carpeta, "giro.wav"), generar_giro())
    _escribir_wav(_ruta_dentro(carpeta, "linea.wav"), generar_linea())
    print("Sonidos generados en:", carpeta)


if __name__ == "__main__":
    main()
