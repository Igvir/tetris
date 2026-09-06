"""La matriz del tablero de juego y las operaciones sobre ella.

El tablero es una matriz de ALTO filas por ANCHO columnas. Se accede siempre
como `tablero[fila][columna]`. `0` es casilla vacia; un numero 1..7 es una
casilla ocupada por una pieza.
"""

ANCHO = 10   # columnas
ALTO = 20    # filas


def crear_tablero(ancho=ANCHO, alto=ALTO):
    """Crea y devuelve un tablero vacio (matriz de ceros)."""
    return [[0 for _ in range(ancho)] for _ in range(alto)]


def mostrar_tablero(tablero):
    """Imprime la matriz del tablero en la terminal (util para depurar)."""
    for fila in tablero:
        print(" ".join(str(celda) for celda in fila))


def es_valida(tablero, matriz, fila, columna):
    """Indica si la matriz de una pieza cabe en (fila, columna).

    Recorre SOLO las casillas ocupadas (distintas de 0) de la pieza y
    comprueba que no salgan de los limites ni pisen una casilla ocupada.
    """
    alto = len(tablero)
    ancho = len(tablero[0])
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                f = fila + i
                c = columna + j
                # Fuera de los limites (izquierda, derecha o base)
                if c < 0 or c >= ancho or f >= alto:
                    return False
                # Choca con una casilla ya ocupada (ignora filas negativas:
                # la pieza aun puede estar entrando por arriba)
                if f >= 0 and tablero[f][c] != 0:
                    return False
    return True


def fusionar(tablero, matriz, fila, columna):
    """Copia los numeros distintos de 0 de la pieza dentro del tablero."""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                tablero[fila + i][columna + j] = matriz[i][j]


def lineas_completas(tablero):
    """Devuelve los indices de las filas totalmente ocupadas (sin ningun 0)."""
    return [indice for indice, fila in enumerate(tablero) if 0 not in fila]


def eliminar_lineas(tablero):
    """Elimina las filas completas, desplaza el resto hacia abajo y anade
    filas vacias arriba. Devuelve cuantas filas se eliminaron.
    """
    ancho = len(tablero[0])
    alto = len(tablero)
    # Conservamos solo las filas que todavia tienen algun hueco (0).
    filas_restantes = [fila for fila in tablero if 0 in fila]
    eliminadas = alto - len(filas_restantes)
    # Anadimos arriba tantas filas vacias como filas eliminamos.
    nuevas = [[0] * ancho for _ in range(eliminadas)]
    tablero[:] = nuevas + filas_restantes
    return eliminadas
