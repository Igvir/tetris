"""Leccion 8 - Sonidos y animaciones (version final del juego).

El pulido final: un sonido al rotar, un sonido al eliminar filas y un destello
al fusionar una pieza. El audio es opcional: si no hay archivos de sonido, el
juego funciona igual. La logica de matrices sigue intacta.

    python main.py            # estilo neon
    python main.py numeros    # estilo numeros

Controles: flechas para mover/rotar/bajar, barra espaciadora caida instantanea,
R reinicia, Esc sale.
"""

import sys


def main():
    try:
        from tetris.grafico import jugar, ESTILO_NUMEROS, ESTILO_NEON
    except ImportError:
        print("Falta Pygame. Instala las dependencias con:")
        print("    pip install -r requirements.txt")
        return

    estilo = ESTILO_NEON
    if len(sys.argv) > 1 and sys.argv[1].lower() == "numeros":
        estilo = ESTILO_NUMEROS

    jugar(estilo=estilo)


if __name__ == "__main__":
    main()
