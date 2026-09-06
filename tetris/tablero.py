"""La matriz del tablero de juego y las operaciones sobre ella.

PLANTILLA DE INICIO: completa las funciones marcadas con TODO siguiendo la guia
del estudiante (Lecciones 1, 5 y 6). El tablero es una matriz de ALTO filas por
ANCHO columnas; se accede como `tablero[fila][columna]`. `0` = casilla vacia;
un numero 1..7 = casilla ocupada.
"""

ANCHO = 10   # columnas
ALTO = 20    # filas


def crear_tablero(ancho=ANCHO, alto=ALTO):
    """Crea y devuelve un tablero vacio (matriz de ceros).

    TODO (Leccion 1): devuelve una matriz de `alto` filas por `ancho` columnas,
    todas con valor 0. Pista: usa una lista por comprension.
    """
    # TODO: reemplaza esto por tu implementacion.
    raise NotImplementedError("Completa crear_tablero en la Leccion 1")


def mostrar_tablero(tablero):
    """Imprime la matriz del tablero en la terminal (util para depurar).

    TODO (Leccion 1): recorre cada fila e imprime sus numeros separados por
    espacios.
    """
    # TODO: reemplaza esto por tu implementacion.
    raise NotImplementedError("Completa mostrar_tablero en la Leccion 1")


def es_valida(tablero, matriz, fila, columna):
    """Indica si la matriz de una pieza cabe en (fila, columna).

    TODO (Lecciones 4 y 5): recorre SOLO las casillas ocupadas (distintas de 0)
    de la pieza y devuelve False si alguna sale de los limites (Leccion 4) o
    pisa una casilla ya ocupada (Leccion 5). Devuelve True si todo cabe.
    """
    # TODO: reemplaza esto por tu implementacion.
    raise NotImplementedError("Completa es_valida en las Lecciones 4 y 5")


def fusionar(tablero, matriz, fila, columna):
    """Copia los numeros distintos de 0 de la pieza dentro del tablero.

    TODO (Leccion 5): copia en el tablero solo las casillas ocupadas de la
    pieza, respetando el desfase (fila, columna).
    """
    # TODO: reemplaza esto por tu implementacion.
    raise NotImplementedError("Completa fusionar en la Leccion 5")


def lineas_completas(tablero):
    """Devuelve los indices de las filas totalmente ocupadas (sin ningun 0).

    TODO (Leccion 6): devuelve una lista con los indices de las filas llenas.
    """
    # TODO: reemplaza esto por tu implementacion.
    raise NotImplementedError("Completa lineas_completas en la Leccion 6")


def eliminar_lineas(tablero):
    """Elimina las filas completas, desplaza el resto hacia abajo y anade filas
    vacias arriba. Devuelve cuantas filas se eliminaron.

    TODO (Leccion 6): conserva solo las filas con algun hueco, cuenta las
    eliminadas y anade esa cantidad de filas vacias arriba.
    """
    # TODO: reemplaza esto por tu implementacion.
    raise NotImplementedError("Completa eliminar_lineas en la Leccion 6")
