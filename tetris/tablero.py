"""Leccion 1: la matriz del tablero.

El tablero es una MATRIZ (lista de listas) de ALTO filas por ANCHO columnas.
Se accede siempre como `tablero[fila][columna]`. Por ahora `0` significa
casilla vacia. En las proximas lecciones un numero 1..7 sera una pieza.
"""

ANCHO = 10   # columnas
ALTO = 20    # filas


def crear_tablero(ancho=ANCHO, alto=ALTO):
    """Crea y devuelve un tablero vacio (matriz de ceros).

    La parte interior [0 for _ in range(ancho)] crea UNA fila de 10 ceros.
    La exterior la repite `alto` veces (20), dando 20 filas.
    """
    return [[0 for _ in range(ancho)] for _ in range(alto)]


def mostrar_tablero(tablero):
    """Imprime la matriz del tablero en la terminal, fila por fila."""
    for fila in tablero:
        print(" ".join(str(celda) for celda in fila))
