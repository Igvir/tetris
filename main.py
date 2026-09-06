"""Leccion 7 - Colores neon.

El mismo Tetris de la Leccion 6, pero ahora con piezas de colores neon
brillantes sobre fondo oscuro. Lo importante: la LOGICA no cambio, solo la
forma de dibujar cada celda.

    python main.py

Controles: flechas para mover/rotar/bajar, R reinicia, Esc sale.
"""


def main():
    try:
        from tetris import grafico
    except ImportError:
        print("Falta Pygame. Instala las dependencias con:")
        print("    pip install -r requirements.txt")
        return

    grafico.ejecutar()


if __name__ == "__main__":
    main()
