# Guía del Estudiante (sin Kiro) - Tetris con Matrices

¡Bienvenido! En este curso vas a construir tu propio **Tetris** en Python
escribiendo **todo el código a mano**, sin ningún agente de inteligencia
artificial. Aquí no usamos prompts ni generación automática: tú tecleas cada
línea, la ejecutas, lees los errores y aprendes a resolverlos. Esa es, al final,
la mejor forma de aprender a programar de verdad.

> ¿Prefieres aprender usando un asistente? Existe una versión hermana de esta
> guía, [guia_estudiante.md](guia_estudiante.md), que construye el mismo juego
> con la ayuda de **Kiro** y *spec driven development*. Ambas llegan al mismo
> resultado; esta es la ruta **autónoma**, para programar por tu cuenta.

Si ya hiciste el curso de **Snake**, aprendiste variables, listas, tuplas,
bucles, condicionales y una probadita de Pygame. Ahora damos el siguiente paso:
vas a dominar las **matrices (listas de listas)**.

> La gran idea de este curso: **en Tetris, TODO es una matriz.** El tablero es
> una matriz, cada pieza es una matriz, rotar es cambiar de matriz y "pegar" una
> pieza es copiar una matriz dentro de otra.

---

## Antes de empezar: ¿qué es una matriz?

Una **matriz** es simplemente una **lista de listas**. Imagina una cuadrícula
(como la de un cuaderno o un tablero de ajedrez): tiene **filas** (van de arriba
hacia abajo) y **columnas** (van de izquierda a derecha).

En Python, cada fila es una lista, y la matriz es una lista que contiene todas
esas filas:

```python
# Una matriz de 3 filas y 4 columnas, todas llenas de ceros
matriz = [
    [0, 0, 0, 0],   # fila 0
    [0, 0, 0, 0],   # fila 1
    [0, 0, 0, 0],   # fila 2
]
```

Para leer o cambiar una casilla usamos **dos índices**: primero la fila, después
la columna.

```python
matriz[1][2] = 5   # fila 1, columna 2 -> ahora vale 5
```

```
        col 0   col 1   col 2   col 3
fila 0    0       0       0       0
fila 1    0       0       5       0   <- aquí pusimos el 5
fila 2    0       0       0       0
```

> **Regla de oro del curso:** siempre escribimos `matriz[fila][columna]`.
> Primero la fila (vertical), luego la columna (horizontal). Confundir el orden
> es el error más común, así que repítelo como un mantra: **fila, luego columna**.

### El tablero de Tetris

El tablero de Tetris es una matriz de **10 columnas de ancho por 20 filas de
alto**. Se accede así:

```python
tablero[fila][columna]
```

- `fila` va de `0` (arriba) a `19` (abajo). La fila crece hacia **abajo**.
- `columna` va de `0` (izquierda) a `9` (derecha).
- El valor `0` significa **casilla vacía**.
- Un número del `1` al `7` significa **casilla ocupada** por una pieza de ese tipo.

### Las piezas como matrices

Cada pieza (tetrominó) también es una matriz pequeña. El número que la rellena la
identifica y, más adelante, decide su **color**. Este es el mapeo que usaremos en
todo el curso:

| Pieza | Número | Color neón (Etapa final) |
|-------|--------|--------------------------|
| I     | 1      | Cian neón `(0, 255, 255)`     |
| O     | 2      | Amarillo neón `(255, 255, 0)` |
| T     | 3      | Magenta neón `(255, 0, 255)`  |
| S     | 4      | Verde neón `(57, 255, 20)`    |
| Z     | 5      | Rojo/rosa neón `(255, 49, 49)`|
| J     | 6      | Azul neón `(77, 77, 255)`     |
| L     | 7      | Naranja neón `(255, 149, 0)`  |

Por ejemplo, la pieza **T** (número 3) se ve así como matriz:

```python
[
    [0, 3, 0],
    [3, 3, 3],
    [0, 0, 0],
]
```

Fíjate: los `0` son huecos vacíos y los `3` son las casillas ocupadas por la
pieza T. ¡La forma de la letra T aparece si miras dónde están los números!

---

## ¿Cómo vamos a trabajar? Programando a mano

Sin un agente que escriba por ti, tu método de trabajo será el de cualquier
programador:

1. **Leer** el objetivo de la lección y entender qué vas a construir.
2. **Escribir** el código a mano en tu editor, entendiendo cada línea.
3. **Ejecutar** el programa (`python main.py`) y observar el resultado.
4. **Leer los errores** con calma: Python te dice el archivo, la línea y el tipo
   de error. Casi siempre la pista está ahí.
5. **Depurar**: añade `print(...)` para ver qué valen tus variables, corrige y
   vuelve a ejecutar.

> Consejo: escribe poco y ejecuta seguido. Es mejor probar cada función pequeña
> que teclear 200 líneas y ejecutarlas todas de golpe. Los errores son normales;
> leerlos y resolverlos **es** aprender a programar.

### Compara tu avance con la solución

Cada lección tiene su propia rama de Git con la solución completa de esa etapa.
Si te atascas o quieres comprobar tu resultado, puedes mirarla:

```bash
git checkout leccion-3-ventana-numeros   # cambia a la solución de la lección 3
python main.py                            # ejecútala para ver cómo debería quedar
```

Intenta escribir tú primero y usa la rama solo para comparar. Aprenderás mucho
más resolviendo por tu cuenta.

### Cómo se estructura cada lección

- **Objetivos de aprendizaje** — qué sabrás hacer al terminar.
- **Conceptos nuevos** — las ideas de matrices o de Python que aparecen.
- **Escribe el código** — el código que debes teclear, explicado por bloques.
- **Resultado esperado** — qué debe verse en la terminal o en la ventana.
- **Actividad práctica** — algo que haces tú para afianzar lo aprendido.

---

# Lección 1: La matriz y el tablero 10×20

Rama de referencia: `leccion-1-matriz-tablero`

### Objetivos de aprendizaje
- Entender qué es una matriz (lista de listas).
- Crear el tablero de Tetris como una matriz de 20 filas × 10 columnas.
- Leer y modificar casillas usando `tablero[fila][columna]`.

### Conceptos nuevos
- Lista por comprensión: `[0 for _ in range(10)]` crea una lista de 10 ceros.
- Constantes: guardamos las dimensiones en `ANCHO` y `ALTO` para reutilizarlas.

### Escribe el código

Crea la carpeta `tetris/` con un archivo vacío `tetris/__init__.py` (así Python
la reconoce como paquete) y luego el archivo `tetris/tablero.py`:

```python
ANCHO = 10   # columnas
ALTO = 20    # filas

def crear_tablero(ancho=ANCHO, alto=ALTO):
    # Creamos ALTO filas; cada fila es una lista de ANCHO ceros.
    return [[0 for _ in range(ancho)] for _ in range(alto)]

def mostrar_tablero(tablero):
    # Recorremos fila por fila e imprimimos los números.
    for fila in tablero:
        print(" ".join(str(celda) for celda in fila))
```

La parte de adentro `[0 for _ in range(ancho)]` construye **una fila** de 10
ceros. La de afuera la repite `alto` veces (20), dando 20 filas.

Ahora crea `main.py` en la raíz del proyecto para probarlo:

```python
from tetris.tablero import crear_tablero, mostrar_tablero

tablero = crear_tablero()
tablero[0][0] = 1     # esquina superior izquierda
tablero[19][9] = 1    # esquina inferior derecha
mostrar_tablero(tablero)
```

### Resultado esperado
Todavía no hay ventana; usamos la terminal. Al ejecutar `python main.py` deberías
ver 20 filas de 10 números, con un `1` en la primera y la última posición:

```
1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
... (20 filas en total) ...
0 0 0 0 0 0 0 0 0 1
```

### Actividad práctica
1. Coloca "a mano" un `1` en la esquina superior izquierda y otro en la inferior
   derecha (ya lo hiciste arriba). Cámbialos de sitio y comprueba el resultado.
2. **Pregunta para pensar:** ¿por qué la esquina inferior derecha es `[19][9]` y
   no `[20][10]`?

---

# Lección 2: Las piezas y sus rotaciones

Rama de referencia: `leccion-2-piezas`

### Objetivos de aprendizaje
- Representar cada pieza como una matriz pequeña.
- Entender que la rotación no calcula nada: solo **cambia de matriz**.

### Conceptos nuevos
- Diccionarios: `PIEZAS` guarda cada pieza por su nombre.
- El módulo `random` para elegir una pieza al azar.

### Escribe el código

Crea `tetris/piezas.py`. Cada pieza guarda **una lista con todas sus rotaciones
ya escritas**. Rotar será avanzar al siguiente elemento de esa lista.

```python
import random

NUMERO_PIEZA = {"I": 1, "O": 2, "T": 3, "S": 4, "Z": 5, "J": 6, "L": 7}

PIEZAS = {
    "T": [
        [[0, 3, 0],
         [3, 3, 3],
         [0, 0, 0]],   # rotación 0
        [[0, 3, 0],
         [0, 3, 3],
         [0, 3, 0]],   # rotación 1
        [[0, 0, 0],
         [3, 3, 3],
         [0, 3, 0]],   # rotación 2
        [[0, 3, 0],
         [3, 3, 0],
         [0, 3, 0]],   # rotación 3
    ],
    # Escribe tú las demás: I, O, S, Z, J, L (mira la rama leccion-2-piezas
    # si necesitas comparar). Recuerda rellenar cada una con su número.
}

def pieza_aleatoria():
    return random.choice(list(PIEZAS.keys()))

def mostrar_pieza(nombre, rotacion=0):
    for fila in PIEZAS[nombre][rotacion]:
        print(" ".join(str(celda) for celda in fila))
```

La idea clave: en lugar de hacer matemáticas para rotar, **escribimos los estados
a mano**. La pieza O (cuadrado) tiene una sola rotación; I, S y Z tienen dos;
T, J y L pueden tener cuatro.

### Resultado esperado
Si en `main.py` llamas a `mostrar_pieza("T", 0)` verás la forma de una T con
números `3`. Al cambiar el índice de rotación, la forma cambia de orientación.

### Actividad práctica
1. Escribe las dos rotaciones de la pieza **I** (número 1): horizontal y vertical.
2. Verifica que la pieza **O** (número 2) se ve igual en todas sus rotaciones.
   ¿Por qué no necesita más de una?
3. Imprime las 4 rotaciones de la T y comprueba que forman un giro completo.

---

# Lección 3: La ventana de Pygame con números

Rama de referencia: `leccion-3-ventana-numeros`

A partir de aquí usamos **Pygame**. Instálalo con:

```bash
pip install -r requirements.txt
```

### Objetivos de aprendizaje
- Abrir una ventana de Pygame y dibujar la cuadrícula 10×20.
- Dibujar el **número** de cada casilla como texto.

### Conceptos nuevos
- Bucle de juego: un `while` que mantiene la ventana viva y procesa eventos.
- Recorrer una matriz con dos bucles `for` anidados (uno por filas, otro por columnas).

### Escribe el código

Crea `tetris/grafico.py`:

```python
import pygame
from . import tablero as tab

TAM = 30                 # tamaño en píxeles de cada celda
FONDO = (10, 10, 20)
REJILLA = (40, 40, 55)
BLANCO = (240, 240, 240)

def dibujar_tablero(pantalla, fuente, tablero):
    for fila in range(len(tablero)):            # recorre filas (0..19)
        for col in range(len(tablero[fila])):   # recorre columnas (0..9)
            rect = pygame.Rect(col * TAM, fila * TAM, TAM, TAM)
            pygame.draw.rect(pantalla, REJILLA, rect, 1)
            numero = tablero[fila][col]
            if numero != 0:
                texto = fuente.render(str(numero), True, BLANCO)
                pantalla.blit(texto, texto.get_rect(center=rect.center))

def ejecutar(tablero):
    pygame.init()
    pantalla = pygame.display.set_mode((tab.ANCHO * TAM, tab.ALTO * TAM))
    pygame.display.set_caption("Tetris con Matrices")
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("consolas", 20)
    corriendo = True
    while corriendo:
        reloj.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
        pantalla.fill(FONDO)
        dibujar_tablero(pantalla, fuente, tablero)
        pygame.display.flip()
    pygame.quit()
```

Fíjate cómo el bucle exterior recorre **filas** y el interior **columnas**. La
posición en pantalla se calcula multiplicando por el tamaño de celda:
`x = col * TAM`, `y = fila * TAM`. Igual que en la matriz, **la fila decide la
vertical y la columna la horizontal**.

En `main.py`, coloca a mano algunas piezas y abre la ventana (necesitarás una
función `fusionar` sencilla en `tablero.py` para copiar una pieza en el tablero;
la escribirás en detalle en la Lección 5, pero puedes adelantarla).

### Resultado esperado
Una ventana con una cuadrícula de 10×20. Las casillas vacías se ven con borde y
sin número; las ocupadas muestran su número dibujado como texto.

### Actividad práctica
1. Pon a mano algunos números distintos de `0` y ejecuta la ventana para verlos.
2. Cambia el tamaño `TAM` y observa cómo crece o se encoge la cuadrícula.

---

# Lección 4: La pieza que cae (movimiento y rotación)

Rama de referencia: `leccion-4-pieza-cae`

### Objetivos de aprendizaje
- Guardar el estado de la pieza activa (nombre, rotación, fila, columna).
- Mover la pieza a izquierda/derecha, hacerla bajar y rotarla.

### Conceptos nuevos
- Una **clase** `Juego` para guardar todo el estado en un solo lugar.
- El descenso automático por tiempo dentro del bucle de juego.

### Escribe el código

Necesitas una comprobación de límites. Añade a `tablero.py`:

```python
def es_valida(tablero, matriz, fila, columna):
    alto = len(tablero)
    ancho = len(tablero[0])
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                f = fila + i
                c = columna + j
                if c < 0 or c >= ancho or f >= alto:
                    return False
    return True
```

Ahora crea `tetris/juego.py` con la clase `Juego`:

```python
from . import piezas
from . import tablero as tab

class Juego:
    def __init__(self):
        self.tablero = tab.crear_tablero()
        self.pieza = None
        self.rotacion = 0
        self.fila = 0
        self.columna = 0
        self.nueva_pieza()

    def matriz_pieza_actual(self):
        return piezas.PIEZAS[self.pieza][self.rotacion]

    def nueva_pieza(self):
        self.pieza = piezas.pieza_aleatoria()
        self.rotacion = 0
        self.fila = 0
        ancho_pieza = len(self.matriz_pieza_actual()[0])
        self.columna = tab.ANCHO // 2 - ancho_pieza // 2

    def mover(self, dx):
        if tab.es_valida(self.tablero, self.matriz_pieza_actual(),
                         self.fila, self.columna + dx):
            self.columna += dx

    def rotar(self):
        siguiente = (self.rotacion + 1) % len(piezas.PIEZAS[self.pieza])
        matriz = piezas.PIEZAS[self.pieza][siguiente]
        if tab.es_valida(self.tablero, matriz, self.fila, self.columna):
            self.rotacion = siguiente   # solo rota si cabe

    def bajar(self):
        if tab.es_valida(self.tablero, self.matriz_pieza_actual(),
                         self.fila + 1, self.columna):
            self.fila += 1
        else:
            self.nueva_pieza()   # de momento reaparece arriba (aún no se acumula)

    def tablero_con_pieza(self):
        copia = [fila[:] for fila in self.tablero]
        matriz = self.matriz_pieza_actual()
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] != 0:
                    f, c = self.fila + i, self.columna + j
                    if 0 <= f < len(copia) and 0 <= c < len(copia[0]):
                        copia[f][c] = matriz[i][j]
        return copia
```

El truco de la rotación cíclica es `% len(...)`: si la rotación llega al final,
el módulo la devuelve a `0`. Y solo cambiamos de estado **si es válido**.

Conecta el teclado en el bucle de `grafico.py` (dentro del `for evento`):
`K_LEFT` → `mover(-1)`, `K_RIGHT` → `mover(1)`, `K_UP` → `rotar()`,
`K_DOWN` → `bajar()`. Añade también una caída automática por tiempo.

### Resultado esperado
Una pieza (dibujada con su número) baja sola cada cierto tiempo. Con las flechas
la mueves a los lados y con la de arriba cambia de forma.

### Actividad práctica
1. Cambia la velocidad de caída (el intervalo de tiempo) y observa el efecto.
2. Haz que al rotar se imprima en la terminal el índice de rotación para ver el
   ciclo `0 → 1 → 2 → 3 → 0`.
3. **Reto corto:** ¿qué pasa si intentas mover la pieza fuera del borde?

---

# Lección 5: Colisiones y fusión con el tablero

Rama de referencia: `leccion-5-colisiones-fusion`

### Objetivos de aprendizaje
- Detectar el choque con otras piezas (no solo con los bordes).
- **Fusionar** (copiar) la matriz de la pieza dentro del tablero al aterrizar.

### Conceptos nuevos
- Recorrer solo las casillas ocupadas (valor distinto de `0`) de la pieza.
- Copiar valores de una matriz a otra respetando el desfase (fila, columna).

### Escribe el código

Amplía `es_valida` en `tablero.py` para que además detecte casillas ocupadas:

```python
def es_valida(tablero, matriz, fila, columna):
    alto = len(tablero)
    ancho = len(tablero[0])
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                f = fila + i
                c = columna + j
                if c < 0 or c >= ancho or f >= alto:      # fuera de los bordes
                    return False
                if f >= 0 and tablero[f][c] != 0:         # choca con algo ocupado
                    return False
    return True
```

Añade `fusionar` en `tablero.py`:

```python
def fusionar(tablero, matriz, fila, columna):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                tablero[fila + i][columna + j] = matriz[i][j]
```

Y en `juego.py`, cambia `bajar()` para que al aterrizar fusione y saque otra pieza:

```python
    def bajar(self):
        if tab.es_valida(self.tablero, self.matriz_pieza_actual(),
                         self.fila + 1, self.columna):
            self.fila += 1
        else:
            tab.fusionar(self.tablero, self.matriz_pieza_actual(),
                         self.fila, self.columna)
            self.nueva_pieza()
```

`f` y `c` son la posición **real en el tablero**. Solo miramos las casillas
ocupadas para no bloquear ni borrar con los huecos.

### Resultado esperado
La pieza se detiene al llegar a la base o encima de otra pieza y se queda
**pegada** al tablero. Enseguida aparece una pieza nueva arriba, y las piezas se
**acumulan**.

### Actividad práctica
1. Deja caer varias piezas y observa cómo se acumulan sin borrarse entre sí.
2. Quita a propósito la comprobación de bordes en `es_valida` y observa el error
   de "índice fuera de rango". Luego arréglalo.
3. **Pregunta clave:** ¿por qué en `fusionar` copiamos solo las casillas con
   número y no los ceros?

---

# Lección 6: Líneas completas, puntuación y fin del juego

Rama de referencia: `leccion-6-lineas-puntuacion`

### Objetivos de aprendizaje
- Detectar filas completas y eliminarlas, desplazando el resto hacia abajo.
- Sumar puntos y detectar el fin del juego.

### Conceptos nuevos
- Filtrar filas: quedarnos solo con las que aún tienen algún `0`.
- Reconstruir la matriz añadiendo filas vacías arriba.

### Escribe el código

Añade a `tablero.py`:

```python
def lineas_completas(tablero):
    return [i for i, fila in enumerate(tablero) if 0 not in fila]

def eliminar_lineas(tablero):
    ancho = len(tablero[0])
    alto = len(tablero)
    # Nos quedamos con las filas que TODAVÍA tienen algún hueco (0).
    filas_restantes = [fila for fila in tablero if 0 in fila]
    eliminadas = alto - len(filas_restantes)
    # Añadimos arriba tantas filas vacías como filas eliminamos.
    nuevas = [[0] * ancho for _ in range(eliminadas)]
    tablero[:] = nuevas + filas_restantes
    return eliminadas
```

En `juego.py`, añade `puntuacion`, `lineas` y `terminado` en `__init__`, marca el
fin del juego en `nueva_pieza` y elimina líneas al aterrizar:

```python
PUNTOS_POR_LINEAS = {0: 0, 1: 100, 2: 300, 3: 500, 4: 800}

# En nueva_pieza(), al final:
    if not tab.es_valida(self.tablero, self.matriz_pieza_actual(),
                         self.fila, self.columna):
        self.terminado = True

# En bajar(), en la rama del "else" (cuando aterriza):
    tab.fusionar(self.tablero, self.matriz_pieza_actual(), self.fila, self.columna)
    eliminadas = tab.eliminar_lineas(self.tablero)
    self.lineas += eliminadas
    self.puntuacion += PUNTOS_POR_LINEAS.get(eliminadas, 0)
    self.nueva_pieza()
```

Una fila está **completa** cuando no tiene ningún `0`. Las descartamos, contamos
cuántas quitamos y ponemos esa misma cantidad de filas vacías **arriba**, de modo
que el resto "cae". En `grafico.py` dibuja un panel con la puntuación y una
pantalla de fin con opción de reiniciar (tecla `R`).

### Resultado esperado
Cuando una fila se llena por completo, **desaparece** y las piezas de arriba
bajan. La puntuación sube. Si el tablero se llena, el juego termina.

### Actividad práctica
1. Llena una fila entera a propósito y comprueba que desaparece y suma puntos.
2. Cambia la fórmula de puntos y observa el efecto.
3. Provoca el fin del juego y verifica que se muestra la puntuación final.

---

# Lección 7: Estilo neón (mejorar solo la presentación)

Rama de referencia: `leccion-7-neon`

### Objetivos de aprendizaje
- Cambiar el dibujo de cada celda de números a **colores neón**.
- Comprobar que la lógica de matrices **no cambia**: solo mejora la capa visual.

### Conceptos nuevos
- Diccionario `COLORES`: cada número de pieza tiene su color neón.
- Dibujar rectángulos rellenos con un contorno claro para simular el brillo.

### Escribe el código

Añade en `piezas.py` el diccionario de colores:

```python
COLORES = {
    0: (10, 10, 20),      # fondo (celda vacía)
    1: (0, 255, 255),     # I - cian
    2: (255, 255, 0),     # O - amarillo
    3: (255, 0, 255),     # T - magenta
    4: (57, 255, 20),     # S - verde
    5: (255, 49, 49),     # Z - rojo/rosa
    6: (77, 77, 255),     # J - azul
    7: (255, 149, 0),     # L - naranja
}
```

Y cambia el dibujo de celda en `grafico.py` (importa `COLORES` desde `piezas`):

```python
def dibujar_tablero(pantalla, fuente, matriz):
    for fila in range(len(matriz)):
        for col in range(len(matriz[fila])):
            rect = pygame.Rect(col * TAM, fila * TAM, TAM, TAM)
            numero = matriz[fila][col]
            if numero == 0:
                pygame.draw.rect(pantalla, FONDO, rect)
                pygame.draw.rect(pantalla, REJILLA, rect, 1)
            else:
                pygame.draw.rect(pantalla, COLORES[numero], rect.inflate(-2, -2))
                pygame.draw.rect(pantalla, BLANCO, rect, 2)   # contorno brillante
```

Lo importante: **es la misma matriz de siempre**. Antes dibujábamos su número;
ahora pintamos su color. La lógica del juego no se toca.

### Resultado esperado
El mismo Tetris de antes, pero con piezas de colores neón brillantes sobre fondo
oscuro. Se ve vistoso, ¡y no tocaste ni una línea de la lógica!

### Actividad práctica
1. Cambia los colores del diccionario `COLORES` a tu paleta favorita.
2. Haz el contorno más grueso o más claro para variar el efecto de brillo.
3. **Comprobación clave:** confirma que `juego.py` y `tablero.py` no cambiaron
   entre la etapa de números y la de neón.

---

# Lección 8: Sonidos y animaciones

Rama de referencia: `leccion-8-sonidos-animaciones`

### Objetivos de aprendizaje
- Añadir sonidos sencillos al girar una pieza y al eliminar filas.
- Mostrar una animación breve al fusionar, sin bloquear el juego.

### Conceptos nuevos
- `pygame.mixer` para reproducir sonidos.
- **Degradación segura:** si no hay audio, el juego sigue funcionando igual.
- Contador de fotogramas para animaciones cortas.

### Escribe el código

Crea `tetris/audio.py`:

```python
import os
import pygame

_CARPETA = os.path.join(os.path.dirname(__file__), "..", "assets", "sonidos")
_ARCHIVOS = {"giro": "giro.wav", "linea": "linea.wav"}
_sonidos = {}
_activo = False

def iniciar_audio():
    global _activo
    try:
        pygame.mixer.init()
        _activo = True
    except pygame.error:
        _activo = False   # sin audio, pero el juego sigue

def cargar_sonidos():
    if not _activo:
        return
    for nombre, archivo in _ARCHIVOS.items():
        ruta = os.path.join(_CARPETA, archivo)
        if os.path.exists(ruta):
            _sonidos[nombre] = pygame.mixer.Sound(ruta)

def reproducir(nombre):
    if _activo and nombre in _sonidos:   # degradación silenciosa
        _sonidos[nombre].play()
```

El audio es **opcional**: el `try/except` hace que, si algo falla, el juego
continúe sin romperse. Llama a `reproducir("giro")` cuando la rotación tenga
éxito y a `reproducir("linea")` cuando elimines filas. Para la animación, guarda
un contador de fotogramas que decrece cada vuelta del bucle y, mientras sea mayor
que cero, dibuja un destello sobre las celdas recién fusionadas.

> El proyecto ya incluye `giro.wav` y `linea.wav` en `assets/sonidos/`. Si
> quieres crearlos tú, mira `tools/generar_sonidos.py`.

### Resultado esperado
Al rotar suena un "clic" corto y al completar una línea suena un efecto. Al
pegarse una pieza ves un destello breve. Todo esto es solo presentación: la
lógica sigue intacta.

### Actividad práctica
1. Cambia los archivos de sonido por otros cortos y ligeros.
2. Borra a propósito un archivo de sonido y comprueba que el juego **no se rompe**.
3. Ajusta la duración del destello (número de fotogramas) y observa el efecto.

---

# Retos para estudiantes avanzados

¿Ya terminaste el Tetris completo? ¡Excelente! Aquí van retos para llevarlo más
lejos, en el mismo espíritu de los retos del curso Snake.

### 1. Niveles de velocidad
Haz que el juego acelere a medida que eliminas líneas. Por ejemplo, cada 10
líneas sube un nivel y las piezas caen más rápido.
- *Pista:* guarda un contador de líneas totales y reduce el intervalo de caída al
  subir de nivel.

### 2. Pieza siguiente
Muestra en un recuadro al lado del tablero cuál será la **próxima pieza**.
- *Pista:* genera la siguiente pieza por adelantado y dibújala en una
  mini-cuadrícula aparte. ¡Es solo dibujar otra matriz pequeña!

### 3. Guardado de récord
Guarda la puntuación más alta en un archivo de texto y muéstrala en pantalla.
- *Pista:* al terminar el juego, lee el récord del archivo; si la puntuación
  actual es mayor, guárdala.

### 4. Efectos neón extra
Añade más brillo: un resplandor alrededor de las piezas, un fondo con degradado,
o un destello especial cuando eliminas **cuatro líneas de golpe** (¡un Tetris!).
- *Pista:* todo esto vive en `grafico.py`; la lógica no cambia.

### Otras ideas
- Un modo de "caída instantánea" (la pieza baja del todo con la barra espaciadora).
- Contador de piezas colocadas y de tiempo jugado.
- Una pantalla de inicio con el título en neón.

---

## Cierre

Construiste un Tetris completo **escribiendo cada línea a mano** y entendiendo que
**todo es una matriz**: el tablero, las piezas, las rotaciones y la fusión. Y
viste cómo, separando la lógica de la presentación, pudiste pasar de números a un
vistoso estilo neón **sin cambiar la lógica**. Aprender a programar así, leyendo
tus propios errores y resolviéndolos, es lo que te convierte en programador.
¡Sigue experimentando con los retos!
