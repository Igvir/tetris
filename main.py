"""Leccion 6 - Lineas, puntuacion y fin del juego.

Cuando llenas una fila entera, desaparece y sumas puntos. Si el tablero se llena
y una pieza nueva no cabe, el juego termina (pulsa R para reiniciar).

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
