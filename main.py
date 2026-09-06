"""Leccion 3 - La ventana de Pygame con numeros.

Abrimos por primera vez una ventana. Colocamos algunas piezas "a mano" en el
tablero (fusionando sus matrices) y las vemos dibujadas como NUMEROS sobre la
cuadricula 10x20. Todavia no caen; eso llega en la Leccion 4.

    python main.py

Cierra la ventana o pulsa Esc para salir.
"""

from tetris.tablero import crear_tablero, fusionar
from tetris.piezas import PIEZAS


def main():
    try:
        from tetris import grafico
    except ImportError:
        print("Falta Pygame. Instala las dependencias con:")
        print("    pip install -r requirements.txt")
        return

    # Creamos el tablero vacio y colocamos algunas piezas a mano para verlas.
    tablero = crear_tablero()
    fusionar(tablero, PIEZAS["T"][0], 0, 3)    # una T arriba al centro
    fusionar(tablero, PIEZAS["L"][0], 17, 0)   # una L abajo a la izquierda
    fusionar(tablero, PIEZAS["I"][0], 18, 4)   # una I acostada abajo

    grafico.ejecutar(tablero)


if __name__ == "__main__":
    main()
