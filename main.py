"""Leccion 1 - La matriz y el tablero 10x20.

Todavia no hay ventana ni Pygame. En esta leccion aprendemos a crear el tablero
como una matriz de numeros y a mostrarlo en la terminal. Ejecuta:

    python main.py
"""

from tetris.tablero import crear_tablero, mostrar_tablero


def main():
    # Creamos el tablero vacio: 20 filas x 10 columnas, todo en 0.
    tablero = crear_tablero()

    # Colocamos "a mano" un 1 en dos esquinas para ver como se escribe una celda.
    tablero[0][0] = 1          # esquina superior izquierda: fila 0, columna 0
    tablero[19][9] = 1         # esquina inferior derecha: fila 19, columna 9

    print("Tablero de Tetris (20 filas x 10 columnas):\n")
    mostrar_tablero(tablero)
    print("\nFijate: 0 es una casilla vacia. La ultima casilla es [19][9], no [20][10].")


if __name__ == "__main__":
    main()
