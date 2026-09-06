# Guía del Instructor - Tetris con Matrices

Esta guía docente acompaña al curso **Tetris con Matrices**, la evolución del curso de **Snake**. Mientras Snake introdujo los fundamentos de Python, este proyecto tiene un objetivo conceptual claro: enseñar el **manejo de matrices (listas de listas)** construyendo un Tetris con **Kiro** y **spec driven development**.

Está pensada para quien imparte el curso a estudiantes principiantes-intermedios (edad 11-12 en adelante). Aquí encontrarás la planificación por sesiones, los errores comunes que anticipar, las soluciones de las actividades, la rúbrica de evaluación y recomendaciones para usar Kiro en el aula.

> **Idea pedagógica central que debes reforzar en cada sesión:** en Tetris **todo es una matriz**. El tablero es una matriz de 10 columnas × 20 filas, cada pieza es una matriz, rotar es cambiar de matriz y fusionar es copiar una matriz dentro de otra. Además, separamos **lógica** (matrices puras) de **presentación** (Pygame), lo que permite pasar de números a neón sin tocar la lógica.

**Convenciones del curso** (mantenlas siempre coherentes):
- Acceso al tablero: `tablero[fila][columna]`. La fila crece hacia abajo (0 arriba, 19 abajo), la columna hacia la derecha (0 a 9).
- Mapeo de piezas: **I=1, O=2, T=3, S=4, Z=5, J=6, L=7**.
- Colores neón (Etapa final): I cian `(0,255,255)`, O amarillo `(255,255,0)`, T magenta `(255,0,255)`, S verde `(57,255,20)`, Z rojo/rosa `(255,49,49)`, J azul `(77,77,255)`, L naranja `(255,149,0)`, sobre fondo oscuro `(10,10,20)`.

---

## Planificación por sesiones

El curso se organiza en **8 sesiones** que siguen la progresión de etapas del proyecto (una lección de la guía del estudiante por sesión). La duración estimada asume clases de aproximadamente 90 minutos; ajústala a tu contexto. Todas las sesiones terminan en algo observable en la ventana de Pygame, salvo las dos primeras, que preparan los datos.

| Sesión | Tema | Duración estimada | Lección del estudiante |
|--------|------|-------------------|------------------------|
| 1 | Matrices y el tablero 10×20 | 90 min | Lección 1 |
| 2 | Piezas y rotaciones | 90 min | Lección 2 |
| 3 | Ventana de Pygame con números | 90–120 min | Lección 3 |
| 4 | La pieza que cae: movimiento y rotación | 120 min | Lección 4 |
| 5 | Colisiones y fusión | 120 min | Lección 5 |
| 6 | Líneas, puntuación y fin del juego | 120 min | Lección 6 |
| 7 | Estilo neón | 90 min | Lección 7 |
| 8 | Sonidos y animaciones + proyecto final | 90–120 min | Lección 8 + retos |

> Recomendación: dedica los primeros 10-15 minutos de cada sesión a repasar lo anterior y ejecutar la versión que quedó de la clase pasada, para que el avance sea visible y motivador (estilo Snake).

### Sesión 1 — Matrices y el tablero 10×20
- **Objetivos:** entender qué es una matriz (lista de listas); crear el tablero como matriz de 20×10; leer/escribir con `tablero[fila][columna]`.
- **Puntos clave a reforzar:**
  - El orden **fila, luego columna**. Repítelo hasta el cansancio.
  - Por qué los índices van de `0` a `n-1` (la fila 19 y la columna 9 son las últimas).
  - La lista por comprensión `[[0 for _ in range(ancho)] for _ in range(alto)]`.
- **Cierre esperado:** el estudiante crea y muestra un tablero vacío en la terminal.

### Sesión 2 — Piezas y rotaciones
- **Objetivos:** representar cada pieza como matriz pequeña; entender la rotación como **cambio de matriz** (no cálculo).
- **Puntos clave a reforzar:**
  - Cada pieza guarda una **lista de rotaciones** ya escritas.
  - La rotación cíclica con el operador módulo `%`.
  - El mapeo de números I=1 … L=7 y por qué es constante.
- **Cierre esperado:** imprimir las rotaciones de la T y la I y ver los giros.

### Sesión 3 — Ventana de Pygame con números
- **Objetivos:** abrir la ventana, dibujar la cuadrícula 10×20 y el número de cada casilla.
- **Puntos clave a reforzar:**
  - El bucle de juego y el manejo del evento de cierre.
  - Recorrer la matriz con dos `for` anidados (fila exterior, columna interior).
  - La correspondencia `x = col * TAM`, `y = fila * TAM`.
- **Cierre esperado:** ver la cuadrícula y algunos números dibujados en la ventana.

### Sesión 4 — La pieza que cae
- **Objetivos:** modelar el estado con la clase `Juego`; mover, bajar y rotar.
- **Puntos clave a reforzar:**
  - Qué guarda el estado (`pieza`, `rotacion`, `fila`, `columna`).
  - Descenso automático por tiempo vs. teclas del jugador.
  - Rotación cíclica que solo se aplica si es válida.
- **Cierre esperado:** una pieza baja sola y responde a las teclas.

### Sesión 5 — Colisiones y fusión
- **Objetivos:** validar posiciones (`es_valida`) y fusionar la pieza en el tablero.
- **Puntos clave a reforzar:**
  - Recorrer **solo casillas ocupadas** (`!= 0`) de la pieza.
  - La posición real `f = fila + i`, `c = columna + j`.
  - Fusionar es **copiar** números, no ceros.
- **Cierre esperado:** las piezas se detienen y se acumulan.

### Sesión 6 — Líneas, puntuación y fin del juego
- **Objetivos:** eliminar filas completas, sumar puntos y detectar el fin.
- **Puntos clave a reforzar:**
  - Fila completa = sin ningún `0`.
  - Reconstruir la matriz añadiendo filas vacías **arriba**.
  - Fin del juego cuando la pieza nueva no cabe.
- **Cierre esperado:** un Tetris jugable y completo (en estilo números).

### Sesión 7 — Estilo neón
- **Objetivos:** cambiar la presentación a colores neón sin tocar la lógica.
- **Puntos clave a reforzar:**
  - **La lógica no cambia**; solo la función que dibuja una celda.
  - El diccionario `COLORES` (número → RGB) y el fondo oscuro.
  - Separación datos/presentación como buena práctica.
- **Cierre esperado:** el mismo Tetris con piezas neón brillantes.

### Sesión 8 — Sonidos, animaciones y proyecto final
- **Objetivos:** añadir sonidos y animaciones; iniciar el proyecto final/retos.
- **Puntos clave a reforzar:**
  - Audio **opcional y degradable** (`try/except`).
  - Animaciones cortas por contador de fotogramas (no bloquean el bucle).
  - Todo vive en la presentación; la lógica sigue intacta.
- **Cierre esperado:** juego pulido y elección de un reto para el proyecto final.

---

## Errores comunes y cómo resolverlos

Anticipar estos errores te ahorrará mucho tiempo. Casi todos vienen de confundir el modelo mental de la matriz.

### 1. Confundir filas y columnas
- **Síntoma:** las piezas aparecen giradas, en la posición equivocada, o el tablero se ve "acostado".
- **Causa:** escribir `tablero[columna][fila]` en lugar de `tablero[fila][columna]`.
- **Solución:** repetir la regla **fila, luego columna**. Sugiere nombrar variables `fila` y `col` en vez de `i`, `j` cuando haya dudas. Pídeles dibujar en papel la cuadrícula con los índices.

### 2. Índices fuera de rango (`IndexError`)
- **Síntoma:** el programa se cae con `list index out of range`, normalmente al mover o bajar cerca de un borde.
- **Causa:** olvidar comprobar los límites antes de acceder al tablero, o usar `20`/`10` como último índice en lugar de `19`/`9`.
- **Solución:** insistir en que `es_valida` compruebe los bordes **antes** de tocar el tablero (`c < 0`, `c >= ANCHO`, `f >= ALTO`) y que solo se lea `tablero[f][c]` cuando `f >= 0`. Recordar que los índices válidos van de `0` a `n-1`.

### 3. Olvidar copiar solo lo ocupado al fusionar
- **Síntoma:** al pegar una pieza, se "borran" casillas que ya estaban ocupadas alrededor.
- **Causa:** copiar también los `0` de la matriz de la pieza sobre el tablero.
- **Solución:** en `fusionar`, copiar **solo** cuando `matriz[i][j] != 0`. Explicar que los `0` de la pieza son huecos que no deben sobrescribir el tablero.

### 4. Modificar la matriz original de la pieza sin querer
- **Síntoma:** las piezas cambian de forma de manera extraña con el tiempo.
- **Causa:** asignaciones que comparten la misma lista (referencias) en vez de copiar.
- **Solución:** para dibujar la pieza sobre el tablero usar una **copia** (`tablero_con_pieza()` devuelve una copia). Introduce la diferencia entre copiar una lista y compartir la referencia con un ejemplo pequeño.

### 5. La rotación se sale del tablero
- **Síntoma:** al rotar cerca del borde, la pieza desaparece o da error.
- **Causa:** aplicar la rotación sin validarla.
- **Solución:** calcular la siguiente rotación, comprobar con `es_valida` y aplicarla **solo si cabe**; si no, mantener el estado anterior.

### 6. La ventana "no responde"
- **Síntoma:** la ventana de Pygame se congela.
- **Causa:** no procesar los eventos en el bucle (falta el manejo de `pygame.event.get()`), o un bucle bloqueante.
- **Solución:** revisar que cada vuelta del bucle procese eventos, actualice el estado y redibuje. Las animaciones deben durar pocos fotogramas.

### 7. Rotación cíclica mal calculada
- **Síntoma:** al llegar a la última rotación, error o se queda "atascada".
- **Causa:** no usar el módulo para volver a `0`.
- **Solución:** `siguiente = (self.rotacion + 1) % len(PIEZAS[self.pieza])`.

---

## Soluciones esperadas de las actividades prácticas

Estas son las respuestas de referencia para las actividades de la guía del estudiante. Sirven como apoyo; acepta variaciones equivalentes.

### Sesión 1 (Matriz y tablero)
1. Colocar `1` en las esquinas: `tablero[0][0] = 1` y `tablero[19][9] = 1`.
2. Al imprimir, se ven los `1` en la primera y última posición.
3. **¿Por qué `[19][9]` y no `[20][10]`?** Porque los índices empiezan en `0`; con 20 filas, la última es la `19`, y con 10 columnas, la última es la `9`.

### Sesión 2 (Piezas y rotaciones)
1. Las dos rotaciones de la pieza **I** (número 1), horizontal y vertical:
   ```python
   # horizontal
   [[0, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]
   # vertical
   [[0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0]]
   ```
2. La pieza **O** (cuadrado, número 2) se ve igual en cualquier rotación porque es simétrica; por eso basta con una sola matriz de rotación.
3. Las cuatro rotaciones de la T completan un giro de 360° (0 → 1 → 2 → 3 → 0).

### Sesión 3 (Ventana con números)
1. Colocar números distintos de `0` a mano y verlos dibujados en la cuadrícula.
2. Cambiar `TAM` agranda o reduce visualmente cada celda (y toda la cuadrícula).
3. Una "torre" es varios números en la misma columna, en filas consecutivas hacia abajo.

### Sesión 4 (Pieza que cae)
1. Reducir/aumentar el intervalo de caída acelera/desacelera la pieza.
2. Imprimir la rotación al girar muestra el ciclo `0 → 1 → 2 → 3 → 0`.
3. Mover contra el borde no debe hacer nada: `mover` no cambia la columna si `es_valida` devuelve `False`.

### Sesión 5 (Colisiones y fusión)
1. Al caer varias piezas, se acumulan sin borrarse porque `fusionar` solo copia casillas ocupadas.
2. Quitar la comprobación de bordes en `es_valida` provoca `IndexError`; restaurarla lo soluciona. (Ejercicio para entender el porqué.)
3. **¿Por qué copiar solo las casillas con número?** Porque los `0` de la pieza son huecos; si los copiáramos, borrarían lo que ya había en el tablero.

### Sesión 6 (Líneas, puntuación y fin)
1. Al llenar una fila completa, desaparece y las de arriba bajan; la puntuación sube.
2. Una fórmula de puntos válida: `{1: 100, 2: 300, 3: 500, 4: 800}` según líneas eliminadas a la vez.
3. Al llenar el tablero, la pieza nueva no cabe (`es_valida` False en la posición inicial) y `terminado` pasa a `True`; se muestra la puntuación final.

### Sesión 7 (Neón)
1. Cambiar los valores de `COLORES` cambia la paleta.
2. Un contorno más grueso/claro intensifica el efecto de brillo.
3. **Comprobación clave:** `juego.py`, `tablero.py` y `piezas.py` no cambian entre la etapa de números y la de neón. Solo cambia la función de dibujo de celda en `grafico.py`.

### Sesión 8 (Sonidos y animaciones)
1. Sustituir los archivos de sonido por otros cortos y ligeros funciona sin cambiar la lógica.
2. Borrar un sonido no rompe el juego: la degradación silenciosa (`try/except` y comprobación en `reproducir`) lo maneja.
3. Ajustar el número de fotogramas alarga o acorta el destello sin bloquear el bucle.

---

## Criterios de evaluación y rúbrica

En la línea del curso Snake, la evaluación combina participación, tareas y el proyecto final:

| Componente | Peso |
|------------|------|
| Participación (asistencia, preguntas, trabajo en clase) | 20% |
| Tareas (actividades prácticas de cada sesión) | 30% |
| Proyecto final (Tetris completo + un reto avanzado) | 50% |

### Rúbrica del proyecto final (sobre el 50%)

| Criterio | Excelente | Aceptable | Insuficiente |
|----------|-----------|-----------|--------------|
| **Uso de matrices** | El tablero y las piezas se modelan correctamente como listas de listas; el acceso `tablero[fila][columna]` es coherente. | Modela matrices con algún error menor de índices. | Confunde filas/columnas o no usa matrices correctamente. |
| **Lógica del juego** | Movimiento, rotación cíclica, colisiones, fusión, líneas y fin del juego funcionan bien. | La mayoría funciona; falla algún caso (bordes, líneas múltiples). | Faltan mecánicas clave o el juego se cae con frecuencia. |
| **Separación lógica/presentación** | La lógica no cambia entre números y neón; todo lo visual vive en la presentación. | Separación mayormente respetada con alguna mezcla. | Lógica y presentación están mezcladas. |
| **Estilo neón y pulido** | Colores neón correctos, puntuación en pantalla, sonidos/animaciones opcionales. | Neón funcional con pulido parcial. | Sin evolución visual respecto a la etapa de números. |
| **Uso de Kiro / spec driven** | Prompts claros; revisa y entiende el código generado; sigue el flujo de specs. | Usa Kiro pero con revisión limitada. | No sigue el flujo ni revisa lo generado. |
| **Entrega con Git (Pull Request)** | Rama con su nombre y PR abierto correctamente. | PR con detalles menores incompletos. | No entrega mediante PR. |

> La **entrega** se realiza vía Git: el estudiante crea una rama con su nombre, confirma sus cambios, sube la rama y abre un **Pull Request**. El PR es la evidencia de que completó la asignación (ver el README del proyecto).

---

## Recomendaciones para usar Kiro en el aula

El curso se apoya en **Kiro** y **spec driven development**. Estas prácticas ayudan a que el aula aproveche la herramienta sin perder el aprendizaje.

### 1. Trabajar desde las specs
- Antes de programar, revisa con el grupo los tres documentos del spec en `.kiro/specs/tetris-matrices/`: `requirements.md`, `design.md` y `tasks.md`.
- Explica que las specs describen **qué** queremos antes del **cómo**. Esto da contexto a Kiro y a los estudiantes.
- Avanza tarea por tarea siguiendo `tasks.md`; cada tarea termina en algo observable.

### 2. Escribir buenos prompts
- Un buen prompt describe el **objetivo**, los **datos** (las matrices) y el **resultado esperado**.
- Modela en clase el prompt sugerido de cada lección (están en la guía del estudiante) y luego pide a los estudiantes que escriban el suyo.
- Enseña a acotar: pedir una función concreta a la vez es mejor que "hazme todo el Tetris".

### 3. Revisar el código generado
- **Regla de oro:** nada se acepta sin entenderse. Después de cada generación, dedica unos minutos a leer el código en voz alta y explicar qué hace cada parte.
- Pide a los estudiantes que ejecuten y prueben en la ventana antes de continuar.
- Usa los errores comunes de esta guía como lista de verificación al revisar (filas/columnas, límites, fusión).

### 4. Ritmo y motivación
- Empieza cada sesión ejecutando lo de la clase anterior: el avance visible mantiene la motivación (igual que en Snake).
- Reserva las últimas sesiones para los **retos avanzados** (niveles de velocidad, pieza siguiente, récord, efectos neón extra) como proyecto final.
- Fomenta que compartan sus variantes de colores neón y sus retos; el componente visual del Tetris invita a personalizar.

---

## Cierre

Este curso lleva a los estudiantes de "entender una lista" a "modelar un juego completo con matrices", reforzando de paso una buena práctica profesional: **separar la lógica de la presentación**. Con Kiro y el flujo de specs, tu rol como instructor es guiar la comprensión y la revisión, no solo la generación de código. Si mantienes visible el avance en cada sesión y refuerzas la regla **fila, luego columna**, tendrás un aula motivada y un aprendizaje sólido de matrices.
