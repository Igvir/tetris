# Guía del Estudiante (con Kiro) - Tetris con Matrices

¡Bienvenido! En este curso vas a construir tu propio **Tetris** en Python usando **Kiro** y una forma de trabajar llamada **spec driven development** (desarrollo guiado por especificaciones).

> Esta es la ruta **con asistente**. Si prefieres aprender escribiendo todo el
> código a mano, sin ningún agente de IA, usa la versión hermana
> [guia_estudiante_sin_kiro.md](guia_estudiante_sin_kiro.md). Ambas construyen el
> mismo juego y siguen las mismas 8 lecciones.

Si ya hiciste el curso de **[Snake](https://github.com/Igvir/snake_game)**, aprendiste variables, listas, tuplas, bucles, condicionales y una probadita de Pygame. Ahora damos el siguiente paso: vas a dominar las **matrices (listas de listas)**. Y lo mejor de todo: verás resultados en pantalla desde la primera lección.

> La gran idea de este curso: **en Tetris, TODO es una matriz.** El tablero es una matriz, cada pieza es una matriz, rotar es cambiar de matriz y "pegar" una pieza es copiar una matriz dentro de otra.

---

## Paso 0: Prepara tu copia del proyecto y tu rama de trabajo

Antes de escribir nada, deja lista tu copia del proyecto y **crea una rama con tu nombre a partir de la rama `inicio`**, que es la plantilla de partida del curso. Ahí los módulos del juego están como esqueleto (con comentarios `TODO`) para que tú los completes. Así conservas la rama `main` intacta como referencia y, al terminar, entregas tu trabajo con un Pull Request desde tu rama.

```bash
# 1. Clona el repositorio (o haz un fork y clona el tuyo)
git clone <url-del-repositorio>
cd tetris

# 2. Crea tu rama de trabajo a partir de `inicio` y cámbiate a ella
git checkout -b tetris-nombre-apellido origin/inicio
```

Cuando creas tu rama a partir de `inicio`, **esta guía ya viene incluida** en `docs/` dentro de tu rama, junto con el andamiaje del proyecto. No tienes que descargarla aparte: ábrela desde tu editor y síguela desde ahí.

> La rama `inicio` es la **plantilla**: al ejecutar `python main.py` antes de empezar, verás un mensaje que indica qué falta implementar (es normal). La rama `main` contiene la **solución completa** por si quieres compararla al final.

> Trabaja siempre en **tu rama** (`tetris-nombre-apellido`), no en `main`. Guarda tus avances con `git add` y `git commit` a menudo. Al final del curso subirás tu rama y abrirás un Pull Request: ese PR es la evidencia de que completaste la asignación (ver la sección de entrega en el [README](../README.md)).

Para consultar la solución de una lección concreta sin perder tu trabajo, primero confirma tus cambios (`git commit`) y luego usa `git checkout leccion-N-...`; para volver a lo tuyo, `git checkout tetris-nombre-apellido`.

---

## Antes de empezar: ¿qué es una matriz?

Una **matriz** es simplemente una **lista de listas**. Imagina una cuadrícula (como la de un cuaderno o un tablero de ajedrez): tiene **filas** (van de arriba hacia abajo) y **columnas** (van de izquierda a derecha).

En Python, cada fila es una lista, y la matriz es una lista que contiene todas esas filas:

```python
# Una matriz de 3 filas y 4 columnas, todas llenas de ceros
matriz = [
    [0, 0, 0, 0],   # fila 0
    [0, 0, 0, 0],   # fila 1
    [0, 0, 0, 0],   # fila 2
]
```

Para leer o cambiar una casilla usamos **dos índices**: primero la fila, después la columna.

```python
matriz[1][2] = 5   # fila 1, columna 2 -> ahora vale 5
```

```
        col 0   col 1   col 2   col 3
fila 0    0       0       0       0
fila 1    0       0       5       0   <- aquí pusimos el 5
fila 2    0       0       0       0
```

> **Regla de oro del curso:** siempre escribimos `matriz[fila][columna]`. Primero la fila (vertical), luego la columna (horizontal). Confundir el orden es el error más común, así que repítelo como un mantra: **fila, luego columna**.

### El tablero de Tetris

El tablero de Tetris es una matriz de **10 columnas de ancho por 20 filas de alto**. Se accede así:

```python
tablero[fila][columna]
```

- `fila` va de `0` (arriba) a `19` (abajo). La fila crece hacia **abajo**.
- `columna` va de `0` (izquierda) a `9` (derecha).
- El valor `0` significa **casilla vacía**.
- Un número del `1` al `7` significa **casilla ocupada** por una pieza de ese tipo.

### Las piezas como matrices

Cada pieza (tetrominó) también es una matriz pequeña. El número que la rellena la identifica y, más adelante, decide su **color**. Este es el mapeo que usaremos en todo el curso:

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

Fíjate: los `0` son huecos vacíos y los `3` son las casillas ocupadas por la pieza T. ¡La forma de la letra T aparece si miras dónde están los números!

---

## ¿Cómo vamos a trabajar? Spec driven development con Kiro

En lugar de escribir todo el código de golpe, usaremos **Kiro** con un método ordenado:

1. **Especificación (spec):** primero describimos QUÉ queremos, no cómo. En este proyecto ya existen tres documentos base en `.kiro/specs/tetris-matrices/`:
   - `requirements.md` — los requisitos (qué debe hacer el juego).
   - `design.md` — el diseño (cómo se organiza).
   - `tasks.md` — las tareas (los pasos a seguir).
2. **Prompt:** en cada etapa le pedimos a Kiro que construya una parte, con un prompt claro y concreto.
3. **Revisión:** leemos el código que genera Kiro, lo entendemos, lo probamos en la ventana y lo ajustamos.

> Kiro es tu compañero de programación, no un reemplazo de tu cabeza. Tu trabajo más importante es **entender** y **revisar** lo que se genera. Un buen prompt describe el objetivo, los datos (las matrices) y el resultado que esperas ver.

### Cómo se estructura cada lección

Cada lección de esta guía tiene siempre las mismas secciones para que sepas qué esperar:

- **Objetivos de aprendizaje** — qué sabrás hacer al terminar.
- **Conceptos nuevos** — las ideas de matrices o de Python que aparecen.
- **Prompt sugerido de Kiro** — qué pedirle para construir la etapa.
- **Código explicado** — fragmentos con explicación línea a línea.
- **Resultado esperado en la ventana** — qué debe verse en Pygame.
- **Actividad práctica** — algo que haces tú para afianzar lo aprendido.

---

# Lección 1: La matriz y el tablero 10×20

### Objetivos de aprendizaje
- Entender qué es una matriz (lista de listas).
- Crear el tablero de Tetris como una matriz de 20 filas × 10 columnas.
- Leer y modificar casillas usando `tablero[fila][columna]`.

### Conceptos nuevos
- Lista por comprensión: `[0 for _ in range(10)]` crea una lista de 10 ceros.
- Constantes: guardamos las dimensiones en `ANCHO` y `ALTO` para reutilizarlas.

### Prompt sugerido de Kiro
> "Crea el módulo `tablero.py`. Define las constantes `ANCHO = 10` y `ALTO = 20`. Implementa `crear_tablero(ancho=10, alto=20)` que devuelva una matriz (lista de listas) de `alto` filas por `ancho` columnas, todas con valor `0`. Añade también `mostrar_tablero(tablero)` que imprima la matriz en la terminal para depurar. Comenta el código en español."

### Código explicado

```python
ANCHO = 10   # columnas
ALTO = 20    # filas

def crear_tablero(ancho=ANCHO, alto=ALTO):
    # Creamos ALTO filas; cada fila es una lista de ANCHO ceros.
    return [[0 for _ in range(ancho)] for _ in range(alto)]
```

La parte de adentro `[0 for _ in range(ancho)]` construye **una fila** de 10 ceros. La de afuera la repite `alto` veces (20), dando 20 filas. El resultado es nuestra cuadrícula vacía.

```python
def mostrar_tablero(tablero):
    # Recorremos fila por fila e imprimimos los números.
    for fila in tablero:
        print(" ".join(str(celda) for celda in fila))
```

### Resultado esperado
Todavía no hay ventana; usamos la terminal para comprobar los datos. Al llamar a `mostrar_tablero(crear_tablero())` deberías ver 20 filas de 10 ceros:

```
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
... (20 filas en total) ...
```

### Actividad práctica
1. Crea un tablero y coloca "manualmente" un `1` en la esquina superior izquierda y otro en la esquina inferior derecha. Pista: `tablero[0][0] = 1` y `tablero[19][9] = 1`.
2. Imprime el tablero y confirma que los `1` aparecen donde esperabas.
3. **Pregunta para pensar:** ¿por qué la esquina inferior derecha es `[19][9]` y no `[20][10]`?

---

# Lección 2: Las piezas y sus rotaciones

### Objetivos de aprendizaje
- Representar cada pieza como una matriz pequeña.
- Entender que la rotación no calcula nada: solo **cambia de matriz**.

### Conceptos nuevos
- Diccionarios: `PIEZAS` guarda cada pieza por su nombre.
- Rotación cíclica: al pasar del último estado se vuelve al primero.

### Prompt sugerido de Kiro
> "Crea el módulo `piezas.py`. Define `NUMERO_PIEZA` con I=1, O=2, T=3, S=4, Z=5, J=6, L=7. Define `PIEZAS` como un diccionario donde cada nombre apunta a una **lista de matrices de rotación**, rellenas con el número de la pieza y `0` en los huecos. Añade `pieza_aleatoria()` que devuelva el nombre de una pieza al azar. Comenta en español."

### Código explicado

Cada pieza guarda **una lista con todas sus rotaciones ya escritas**. Rotar es avanzar al siguiente elemento de esa lista.

```python
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
    # ... I, O, S, Z, J, L
}
```

La idea clave: en lugar de hacer matemáticas para rotar, **escribimos los estados a mano**. La pieza O (cuadrado) tiene una sola rotación; I, S y Z tienen dos; T, J y L pueden tener cuatro. Es una decisión de diseño con datos que nos ahorra cálculos complejos.

```python
import random

def pieza_aleatoria():
    return random.choice(list(PIEZAS.keys()))
```

### Resultado esperado
Si imprimes la rotación 0 de la pieza T verás la forma de una T dibujada con números 3 sobre ceros. Al cambiar de índice de rotación, la forma cambia de orientación.

### Actividad práctica
1. Escribe (a mano, en papel o en el editor) las dos rotaciones de la pieza **I** (número 1). Recuerda: horizontal y vertical.
2. Verifica que la pieza **O** (número 2) se ve igual en todas sus rotaciones. ¿Por qué no necesita más de una?
3. Imprime cada rotación de la T y comprueba que forman un giro completo.

---

# Lección 3: La ventana de Pygame con números

### Objetivos de aprendizaje
- Abrir una ventana de Pygame y dibujar la cuadrícula 10×20.
- Dibujar el **número** de cada casilla como texto (Etapa 1 del proyecto).

### Conceptos nuevos
- Bucle de juego: `while` que mantiene la ventana viva.
- Recorrer una matriz con dos bucles `for` anidados (uno por filas, otro por columnas).

### Prompt sugerido de Kiro
> "Crea `grafico.py` y `main.py`. En `grafico.py` inicializa Pygame, crea una ventana y un reloj, y dibuja la cuadrícula de 10×20 celdas. Recorre el tablero con dos bucles anidados y dibuja el número de cada casilla como texto; deja las casillas con `0` visualmente vacías. Maneja el cierre de la ventana limpiamente. En `main.py` abre la ventana y arranca el bucle. Comenta en español."

### Código explicado

```python
import pygame

TAM = 30  # tamaño en píxeles de cada celda

def dibujar_tablero(pantalla, tablero, fuente):
    for fila in range(len(tablero)):            # recorre filas (0..19)
        for col in range(len(tablero[fila])):   # recorre columnas (0..9)
            x = col * TAM
            y = fila * TAM
            # Dibuja el borde de la celda para ver la cuadrícula
            rect = pygame.Rect(x, y, TAM, TAM)
            pygame.draw.rect(pantalla, (60, 60, 60), rect, 1)
            numero = tablero[fila][col]
            if numero != 0:
                texto = fuente.render(str(numero), True, (255, 255, 255))
                pantalla.blit(texto, (x + 8, y + 4))
```

Fíjate cómo el bucle exterior recorre **filas** y el interior **columnas**. La posición en pantalla se calcula multiplicando por el tamaño de celda: `x = col * TAM`, `y = fila * TAM`. Igual que en la matriz, **la fila decide la vertical y la columna la horizontal**.

### Resultado esperado
Una ventana con una cuadrícula de 10×20. Las casillas vacías se ven como celdas con borde y sin número; las ocupadas muestran su número (1 a 7) dibujado como texto. ¡Ahora ves tus datos directamente en pantalla!

### Actividad práctica
1. Pon a mano algunos números distintos de `0` en el tablero y ejecuta la ventana para verlos dibujados.
2. Cambia el tamaño `TAM` y observa cómo crece o se encoge la cuadrícula.
3. Dibuja una "torre" de piezas colocando varios números en la misma columna.

---

# Lección 4: La pieza que cae (movimiento y rotación)

### Objetivos de aprendizaje
- Guardar el estado de la pieza activa (nombre, rotación, fila, columna).
- Mover la pieza a izquierda/derecha, hacerla bajar y rotarla.

### Conceptos nuevos
- Una **clase** `Juego` para guardar todo el estado en un solo lugar.
- El descenso automático por tiempo dentro del bucle de juego.

### Prompt sugerido de Kiro
> "Crea la clase `Juego` en `juego.py` con `tablero`, `pieza`, `rotacion`, `fila`, `columna`, `puntuacion` y `terminado`. Implementa `matriz_pieza_actual()`, `nueva_pieza()` (aparece arriba y al centro), `mover(dx)`, `bajar()` y `rotar()` (avanza cíclicamente al siguiente estado). También `tablero_con_pieza()` que devuelva una copia del tablero con la pieza dibujada. Conecta el teclado en `grafico.py` para mover, rotar y bajar. Comenta en español."

### Código explicado

```python
def matriz_pieza_actual(self):
    # Devuelve la matriz de la rotación actual de la pieza activa.
    return PIEZAS[self.pieza][self.rotacion]

def rotar(self):
    siguiente = (self.rotacion + 1) % len(PIEZAS[self.pieza])
    matriz = PIEZAS[self.pieza][siguiente]
    if es_valida(self.tablero, matriz, self.fila, self.columna):
        self.rotacion = siguiente   # solo rota si cabe
```

El truco de la rotación cíclica es `% len(...)`: si la rotación llega al final, el módulo la devuelve a `0`. Y solo cambiamos de estado **si es válido** (más sobre validez en la Lección 5).

```python
def mover(self, dx):
    if es_valida(self.tablero, self.matriz_pieza_actual(), self.fila, self.columna + dx):
        self.columna += dx
```

`dx` vale `-1` para izquierda y `+1` para derecha. Solo movemos si la nueva posición es válida.

### Resultado esperado
En la ventana ves una pieza (dibujada con su número) que baja sola cada cierto tiempo. Con las flechas la mueves a los lados y con la tecla de rotar cambia de forma. Con la flecha abajo baja más rápido.

### Actividad práctica
1. Cambia la velocidad de caída (el intervalo de tiempo) y observa el efecto.
2. Haz que la tecla de rotar imprima en la terminal el índice de rotación actual para ver el ciclo `0 → 1 → 2 → 3 → 0`.
3. **Reto corto:** ¿qué pasa si intentas mover la pieza fuera del borde? (Debe ignorarse; lo aseguramos en la próxima lección.)

---

# Lección 5: Colisiones y fusión con el tablero

### Objetivos de aprendizaje
- Comprobar si una posición de la pieza es válida (colisiones).
- **Fusionar** (copiar) la matriz de la pieza dentro del tablero al aterrizar.

### Conceptos nuevos
- Recorrer solo las casillas ocupadas (valor distinto de `0`) de la pieza.
- Copiar valores de una matriz a otra respetando el desfase (fila, columna).

### Prompt sugerido de Kiro
> "Implementa `es_valida(tablero, matriz, fila, columna)`: recorre solo las casillas distintas de `0` de la matriz de la pieza; devuelve `False` si alguna sale de los límites o pisa una casilla ocupada, y `True` en caso contrario. Implementa `fusionar(tablero, matriz, fila, columna)` que copie los números distintos de `0` de la pieza en el tablero. En `bajar()`, cuando la pieza no pueda descender, fusiona y genera una pieza nueva. Comenta en español."

### Código explicado

```python
def es_valida(tablero, matriz, fila, columna):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:          # solo miramos casillas ocupadas
                f = fila + i
                c = columna + j
                if c < 0 or c >= ANCHO or f >= ALTO:   # fuera de los bordes
                    return False
                if f >= 0 and tablero[f][c] != 0:      # choca con algo ocupado
                    return False
    return True
```

`f` y `c` son la posición **real en el tablero**: la posición de la pieza (`fila`, `columna`) más el desfase dentro de su matriz (`i`, `j`). Solo comprobamos las casillas ocupadas para no bloquear con los huecos.

```python
def fusionar(tablero, matriz, fila, columna):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                tablero[fila + i][columna + j] = matriz[i][j]
```

Fusionar es **copiar** los números de la pieza al tablero. Fíjate que solo copiamos las casillas ocupadas para no borrar con ceros lo que ya había.

### Resultado esperado
La pieza baja, y al llegar a la base o encima de otra pieza **se detiene y se queda pegada** al tablero (sus números permanecen). Enseguida aparece una pieza nueva arriba.

### Actividad práctica
1. Deja caer varias piezas y observa cómo se acumulan sin borrarse entre sí.
2. Cambia `es_valida` a propósito para que ignore los bordes y observa el error de "índice fuera de rango". Luego arréglalo. (Así entiendes por qué la comprobación es importante.)
3. **Pregunta clave:** ¿por qué en `fusionar` copiamos solo las casillas con número y no los ceros?

---

# Lección 6: Líneas completas, puntuación y fin del juego

### Objetivos de aprendizaje
- Detectar filas completas y eliminarlas, desplazando el resto hacia abajo.
- Sumar puntos y detectar el fin del juego.

### Conceptos nuevos
- Filtrar filas: quedarnos solo con las que aún tienen algún `0`.
- Reconstruir la matriz añadiendo filas vacías arriba.

### Prompt sugerido de Kiro
> "Implementa `lineas_completas(tablero)` que devuelva los índices de filas sin ningún `0`, y `eliminar_lineas(tablero)` que quite las filas completas, desplace las demás hacia abajo, añada filas vacías arriba y devuelva cuántas eliminó. Suma puntos según las líneas eliminadas. Detecta el fin del juego cuando una pieza nueva no cabe en su posición inicial y muestra la puntuación final con opción de reiniciar o salir. Comenta en español."

### Código explicado

```python
def eliminar_lineas(tablero):
    # Nos quedamos con las filas que TODAVÍA tienen algún hueco (0).
    filas_restantes = [fila for fila in tablero if 0 in fila]
    eliminadas = ALTO - len(filas_restantes)
    # Añadimos arriba tantas filas vacías como filas eliminamos.
    nuevas = [[0] * ANCHO for _ in range(eliminadas)]
    tablero[:] = nuevas + filas_restantes
    return eliminadas
```

Una fila está **completa** cuando no tiene ningún `0`. Las descartamos, contamos cuántas quitamos y ponemos esa misma cantidad de filas vacías **arriba**, de modo que el resto "cae" hacia abajo. Usamos `tablero[:] = ...` para modificar la misma matriz.

```python
def nueva_pieza(self):
    self.pieza = pieza_aleatoria()
    self.rotacion = 0
    self.fila = 0
    self.columna = ANCHO // 2 - 1   # arriba y al centro
    if not es_valida(self.tablero, self.matriz_pieza_actual(), self.fila, self.columna):
        self.terminado = True       # no cabe -> fin del juego
```

### Resultado esperado
Cuando una fila se llena por completo, **desaparece** y las piezas de arriba bajan un nivel. La puntuación sube. Si el tablero se llena y una pieza nueva no cabe, el juego termina y se muestra la puntuación final.

### Actividad práctica
1. Llena una fila entera a propósito y comprueba que desaparece y suma puntos.
2. Cambia la fórmula de puntos para que dar varias líneas de golpe valga más (por ejemplo, 1 línea = 100, 2 = 300, 3 = 500, 4 = 800).
3. Provoca el fin del juego y verifica que se muestra la puntuación final.

---

# Lección 7: Estilo neón (mejorar solo la presentación)

### Objetivos de aprendizaje
- Cambiar el dibujo de cada celda de números a **colores neón**.
- Comprobar que la lógica de matrices **no cambia**: solo mejora la capa visual.

### Conceptos nuevos
- Diccionario `COLORES`: cada número de pieza tiene su color neón.
- Dibujar rectángulos rellenos con un contorno claro para simular el brillo.

### Prompt sugerido de Kiro
> "Sin tocar la lógica (`piezas.py`, `tablero.py`, `juego.py`), añade en `grafico.py` un diccionario `COLORES` que asocie cada número (1 a 7) a su color neón, con fondo oscuro. Reemplaza el dibujo de números por rectángulos pintados con `COLORES[numero]`, dejando las casillas `0` con el fondo oscuro y añadiendo un contorno claro para simular el brillo. Mantén la puntuación en pantalla. Comenta en español."

### Código explicado

```python
FONDO = (10, 10, 20)   # fondo oscuro para que resalte el neón

COLORES = {
    1: (0, 255, 255),     # I - cian
    2: (255, 255, 0),     # O - amarillo
    3: (255, 0, 255),     # T - magenta
    4: (57, 255, 20),     # S - verde
    5: (255, 49, 49),     # Z - rojo/rosa
    6: (77, 77, 255),     # J - azul
    7: (255, 149, 0),     # L - naranja
}

def dibujar_celda_neon(pantalla, fila, col, numero):
    x, y = col * TAM, fila * TAM
    rect = pygame.Rect(x, y, TAM, TAM)
    if numero == 0:
        pygame.draw.rect(pantalla, FONDO, rect)          # celda vacía
    else:
        pygame.draw.rect(pantalla, COLORES[numero], rect) # relleno neón
        pygame.draw.rect(pantalla, (255, 255, 255), rect, 2)  # contorno brillante
```

Lo importante: **es la misma matriz de siempre**. Antes dibujábamos su número; ahora pintamos su color. La lógica del juego no se toca; solo cambió la función que dibuja una celda. Esa es la magia de separar los datos de la presentación.

### Resultado esperado
El mismo Tetris de antes, pero con piezas de colores neón brillantes sobre un fondo oscuro y la puntuación en pantalla. Se ve profesional y vistoso, ¡y no tocaste ni una línea de la lógica!

### Actividad práctica
1. Cambia los colores del diccionario `COLORES` a tu paleta favorita.
2. Prueba a hacer el contorno más grueso o más claro para variar el efecto de brillo.
3. **Comprobación clave:** confirma que `juego.py`, `tablero.py` y `piezas.py` no cambiaron nada entre la Etapa números y la Etapa neón.

---

# Lección 8: Sonidos y animaciones

### Objetivos de aprendizaje
- Añadir sonidos sencillos al girar una pieza y al eliminar filas.
- Mostrar animaciones breves al fusionar y al eliminar líneas, sin bloquear el juego.

### Conceptos nuevos
- `pygame.mixer` para reproducir sonidos.
- **Degradación segura:** si no hay audio, el juego sigue funcionando igual.
- Contador de fotogramas para animaciones cortas.

### Prompt sugerido de Kiro
> "Crea `audio.py` con `iniciar_audio()`, `cargar_sonidos()` y `reproducir(nombre)`, usando `pygame.mixer`. Si el mezclador no arranca o falta un archivo, el juego debe seguir sin fallar (audio opcional). Reproduce un sonido de giro al rotar con éxito y uno de línea al eliminar filas. Añade una animación breve (destello/parpadeo) al fusionar una pieza y al eliminar filas, controlada por un contador de fotogramas para que no bloquee el bucle. La lógica de matrices no debe cambiar. Comenta en español."

### Código explicado

```python
import pygame

_sonidos = {}
_activo = False

def iniciar_audio():
    global _activo
    try:
        pygame.mixer.init()
        _activo = True
    except pygame.error:
        _activo = False   # sin audio, pero el juego sigue

def reproducir(nombre):
    # Si no hay audio o falta el sonido, no hace nada (degradación silenciosa).
    if _activo and nombre in _sonidos:
        _sonidos[nombre].play()
```

El audio es **opcional**: envolvemos la inicialización en un `try/except` para que, si algo falla, el juego continúe sin romperse. Las animaciones se controlan con un contador que dura pocos fotogramas, así no se congela el juego.

### Resultado esperado
Al rotar suena un "clic" corto, y al completar una línea suena un efecto. Al pegarse una pieza ves un destello breve, y las filas parpadean justo antes de desaparecer. Todo esto es solo presentación: la lógica sigue intacta.

### Actividad práctica
1. Cambia los archivos de sonido por otros de tu elección (cortos y ligeros).
2. Borra a propósito un archivo de sonido y comprueba que el juego **no se rompe**.
3. Ajusta la duración del destello (número de fotogramas) y observa el efecto.

---

# Retos para estudiantes avanzados

¿Ya terminaste el Tetris completo? ¡Excelente! Aquí van retos para llevarlo más lejos, en el mismo espíritu de los retos del curso Snake. Recuerda usar Kiro con un buen prompt para cada uno.

### 1. Niveles de velocidad
Haz que el juego acelere a medida que eliminas líneas. Por ejemplo, cada 10 líneas sube un nivel y las piezas caen más rápido.
- *Pista:* guarda un contador de líneas totales y reduce el intervalo de caída al subir de nivel.

### 2. Pieza siguiente
Muestra en un recuadro al lado del tablero cuál será la **próxima pieza**.
- *Pista:* genera la siguiente pieza por adelantado y dibújala en una mini-cuadrícula aparte. ¡Es solo dibujar otra matriz pequeña!

### 3. Guardado de récord
Guarda la puntuación más alta en un archivo de texto y muéstrala en pantalla.
- *Pista:* al terminar el juego, lee el récord del archivo; si la puntuación actual es mayor, guárdala.

### 4. Efectos neón extra
Añade más brillo: un resplandor alrededor de las piezas, un fondo con degradado, o un destello especial cuando eliminas **cuatro líneas de golpe** (¡un Tetris!).
- *Pista:* todo esto vive en `grafico.py`; la lógica no cambia. Prueba a dibujar varios contornos de colores más claros alrededor de cada celda.

### Otras ideas
- Un modo de "caída instantánea" (la pieza baja del todo con la barra espaciadora).
- Contador de piezas colocadas y de tiempo jugado.
- Una pantalla de inicio con el título en neón.

---

## Cierre

Construiste un Tetris completo entendiendo que **todo es una matriz**: el tablero, las piezas, las rotaciones y la fusión. Y viste cómo, separando la lógica de la presentación, pudiste pasar de números a un vistoso estilo neón **sin cambiar la lógica**. Ese es exactamente el tipo de pensamiento que hace a un buen programador. ¡Sigue experimentando con los retos!
