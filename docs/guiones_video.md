# Guiones de video - Curso Tetris con Matrices

Este documento contiene los **guiones escena por escena** para producir el curso en video, uno por cada una de las 8 lecciones, más un video de introducción. Está pensado para un enfoque **híbrido**:

- **Voz/avatar IA** para las partes explicativas (teoría, objetivos, conceptos de matrices). Puedes pegar el texto narrado en herramientas como Coursebox, Fliki, HeyGen o Synthesia.
- **Grabación de pantalla** (por ejemplo con OBS Studio) para la parte práctica: mostrar el editor, el código y el juego en acción.

## Cómo usar este documento

Cada video se divide en **escenas**. Para cada escena verás:

- 🎙️ **Narración** — el texto que dice la voz/avatar (léelo tal cual o pégalo en la herramienta IA).
- 🖥️ **En pantalla** — qué mostrar: diapositiva, código, terminal o el juego.
- ⏱️ **Duración aprox.** — para dosificar el ritmo.

**Convenciones del curso** (mantenlas en todos los videos):
- Acceso al tablero: `tablero[fila][columna]` (fila hacia abajo 0-19, columna 0-9).
- Mapeo de piezas: I=1, O=2, T=3, S=4, Z=5, J=6, L=7.
- Regla de oro repetida en cada video: **fila, luego columna**.
- El estudiante trabaja en su rama a partir de `inicio`; cada lección tiene su rama de solución `leccion-N-...`.

**Consejo de producción:** graba las partes de código con OBS mostrando el editor y una terminal; para "ver el juego correr" (piezas cayendo, neón, líneas que desaparecen) usa captura real de la ventana de Pygame, ya que un avatar IA no puede ejecutarlo.

**Tono:** cercano, motivador y claro, para estudiantes de 11-12 años en adelante. Frases cortas. Celebra cada avance visible.

---

# Video 0 — Introducción al curso (1.5 - 2 min)

### Escena 0.1 — Bienvenida
- 🎙️ **Narración:** "¡Hola y bienvenido al curso de Tetris con Matrices! Vas a construir tu propio Tetris en Python, desde cero, y en el camino vas a dominar una de las herramientas más útiles de la programación: las matrices."
- 🖥️ **En pantalla:** título del curso sobre un fondo neón; de fondo, un clip corto del Tetris terminado (piezas de colores cayendo).
- ⏱️ 15 s

### Escena 0.2 — La gran idea
- 🎙️ **Narración:** "La idea central es simple y poderosa: en Tetris, todo es una matriz. El tablero es una matriz, cada pieza es una matriz, rotar es cambiar de matriz, y pegar una pieza es copiar una matriz dentro de otra. Si entiendes eso, entiendes el juego completo."
- 🖥️ **En pantalla:** diapositiva con cuatro íconos: tablero, pieza, rotación, fusión; cada uno mostrando una pequeña cuadrícula de números.
- ⏱️ 25 s

### Escena 0.3 — De Snake a Tetris
- 🎙️ **Narración:** "Este curso es la evolución del curso de Snake. Allí aprendiste variables, listas y una introducción a Pygame. Aquí damos el siguiente paso: listas de listas, es decir, matrices."
- 🖥️ **En pantalla:** diapositiva "Snake ➜ Tetris"; enlace visible al repositorio de Snake.
- ⏱️ 15 s

### Escena 0.4 — Cómo está organizado
- 🎙️ **Narración:** "El curso tiene ocho lecciones. Empezamos viendo los números de las matrices y terminamos con un juego a todo color, con sonidos y animaciones. Trabajarás en tu propia rama de Git y cada lección tiene una rama con la solución para que compares."
- 🖥️ **En pantalla:** lista de las 8 lecciones; luego terminal mostrando `git checkout -b tetris-nombre origin/inicio`.
- ⏱️ 25 s

### Escena 0.5 — Cierre
- 🎙️ **Narración:** "¿Listo? Abre tu editor y empecemos por la pieza más básica de todo: la matriz."
- 🖥️ **En pantalla:** texto "Lección 1: la matriz y el tablero".
- ⏱️ 10 s

---

# Video 1 — La matriz y el tablero 10x20 (4 - 5 min)

### Escena 1.1 — Objetivos
- 🎙️ **Narración:** "En esta lección vas a entender qué es una matriz, crear el tablero del Tetris y aprender a leer y escribir cualquier casilla. Todo en la terminal; los gráficos llegan pronto."
- 🖥️ **En pantalla:** diapositiva con los 3 objetivos.
- ⏱️ 20 s

### Escena 1.2 — ¿Qué es una matriz?
- 🎙️ **Narración:** "Una matriz es una lista de listas: una cuadrícula, como un cuaderno cuadriculado. Tiene filas, que van de arriba hacia abajo, y columnas, de izquierda a derecha. Para tocar una casilla usamos dos índices: primero la fila, luego la columna. Repite esto como un mantra: fila, luego columna."
- 🖥️ **En pantalla:** diapositiva animada de una cuadrícula 3x4; resaltar `matriz[1][2]` iluminando fila 1 y columna 2.
- ⏱️ 40 s

### Escena 1.3 — El tablero como matriz (código)
- 🎙️ **Narración:** "El tablero de Tetris tiene 10 columnas y 20 filas. Lo creamos con una lista por comprensión: por cada una de las 20 filas, una lista de 10 ceros. El cero significa casilla vacía."
- 🖥️ **En pantalla:** grabación del editor escribiendo `crear_tablero` en `tablero.py`; resaltar la lista por comprensión.
- ⏱️ 50 s

### Escena 1.4 — Verlo funcionar (terminal)
- 🎙️ **Narración:** "Vamos a mostrarlo. Con `mostrar_tablero` recorremos fila por fila e imprimimos los números. Colocamos un uno en dos esquinas para ver cómo se escribe una casilla: fila cero columna cero, y fila diecinueve columna nueve."
- 🖥️ **En pantalla:** terminal ejecutando `python main.py`; señalar los dos `1` en las esquinas de la salida.
- ⏱️ 45 s

### Escena 1.5 — Pregunta y actividad
- 🎙️ **Narración:** "Una pregunta para pensar: ¿por qué la última casilla es diecinueve, nueve, y no veinte, diez? Porque los índices empiezan en cero. Tu actividad: coloca números en otras casillas y comprueba dónde aparecen."
- 🖥️ **En pantalla:** diapositiva con la pregunta y la actividad.
- ⏱️ 25 s

### Escena 1.6 — Cierre
- 🎙️ **Narración:** "Ya tienes el tablero. En la próxima lección le damos forma a las piezas, también como matrices."
- 🖥️ **En pantalla:** texto "Siguiente: las piezas y sus rotaciones".
- ⏱️ 10 s

---

# Video 2 — Las piezas y sus rotaciones (4 - 5 min)

### Escena 2.1 — Objetivos
- 🎙️ **Narración:** "Ahora representamos cada pieza como una matriz pequeña y descubrimos un truco genial: rotar no necesita matemáticas, solo cambiar de matriz."
- 🖥️ **En pantalla:** diapositiva de objetivos.
- ⏱️ 20 s

### Escena 2.2 — Una pieza es una matriz
- 🎙️ **Narración:** "Mira la pieza T. Es una matriz de tres por tres. Los ceros son huecos y los tres dibujan la forma de la letra T. Cada pieza tiene su propio número, del uno al siete."
- 🖥️ **En pantalla:** diapositiva con la matriz de la T; animar resaltando los `3` para que aparezca la forma de T.
- ⏱️ 40 s

### Escena 2.3 — Rotar es cambiar de matriz (código)
- 🎙️ **Narración:** "Aquí está el truco: en lugar de calcular la rotación, guardamos todas las rotaciones ya escritas en una lista. Rotar es simplemente pasar a la siguiente matriz de esa lista. La pieza cuadrado tiene una sola; otras tienen dos o cuatro."
- 🖥️ **En pantalla:** editor mostrando `PIEZAS` en `piezas.py`, desplazándose por las 4 rotaciones de la T.
- ⏱️ 50 s

### Escena 2.4 — Verlo funcionar
- 🎙️ **Narración:** "Al imprimir las cuatro rotaciones de la T, vemos cómo gira. Es solo elegir otra matriz. Una decisión de diseño con datos nos ahorró un montón de matemáticas."
- 🖥️ **En pantalla:** terminal imprimiendo las rotaciones de la T y la I.
- ⏱️ 40 s

### Escena 2.5 — Actividad y cierre
- 🎙️ **Narración:** "Tu actividad: escribe a mano las dos rotaciones de la pieza I. Y piensa por qué la pieza cuadrado no necesita más de una. En la próxima lección, ¡abrimos la ventana!"
- 🖥️ **En pantalla:** diapositiva con la actividad; texto "Siguiente: la ventana de Pygame".
- ⏱️ 25 s

---

# Video 3 — La ventana de Pygame con números (5 - 6 min)

### Escena 3.1 — Objetivos
- 🎙️ **Narración:** "Es hora de ver nuestros datos en pantalla. Vamos a abrir una ventana de Pygame y dibujar la cuadrícula con los números de cada casilla."
- 🖥️ **En pantalla:** diapositiva de objetivos.
- ⏱️ 20 s

### Escena 3.2 — Instalar Pygame
- 🎙️ **Narración:** "A partir de aquí usamos Pygame. Instálalo con pip install, menos requirements punto txt."
- 🖥️ **En pantalla:** terminal ejecutando `pip install -r requirements.txt`.
- ⏱️ 20 s

### Escena 3.3 — El bucle de juego y el recorrido (código)
- 🎙️ **Narración:** "Dibujar el tablero es recorrer la matriz con dos bucles: uno por filas y, dentro, uno por columnas. Para cada casilla calculamos su posición en pantalla: la columna da la horizontal y la fila la vertical. Otra vez: fila, luego columna."
- 🖥️ **En pantalla:** editor mostrando `dibujar_tablero` con los dos `for` anidados; resaltar `x = col * TAM`, `y = fila * TAM`.
- ⏱️ 60 s

### Escena 3.4 — Verlo funcionar (captura del juego)
- 🎙️ **Narración:** "Ejecutamos, y ahí está: la cuadrícula de diez por veinte, con los números dibujados en las casillas ocupadas. Los mismos datos de antes, ahora en una ventana."
- 🖥️ **En pantalla:** captura real de la ventana de Pygame con la cuadrícula y algunas piezas como números.
- ⏱️ 40 s

### Escena 3.5 — Actividad y cierre
- 🎙️ **Narración:** "Prueba a cambiar el tamaño de celda y observa cómo crece la cuadrícula. En la próxima lección, ¡la pieza empieza a caer!"
- 🖥️ **En pantalla:** diapositiva de actividad; texto "Siguiente: la pieza que cae".
- ⏱️ 20 s

---

# Video 4 — La pieza que cae (5 - 6 min)

### Escena 4.1 — Objetivos
- 🎙️ **Narración:** "Vamos a dar vida al juego: una pieza que cae sola y responde a tus teclas. Para eso creamos una clase que guarda el estado del juego."
- 🖥️ **En pantalla:** diapositiva de objetivos.
- ⏱️ 20 s

### Escena 4.2 — La clase Juego (código)
- 🎙️ **Narración:** "Una clase nos deja guardar en un solo lugar qué pieza es, en qué rotación está y en qué fila y columna se encuentra. Es como una ficha que sabe dónde está y cómo girar."
- 🖥️ **En pantalla:** editor mostrando la clase `Juego` y sus atributos en `juego.py`.
- ⏱️ 50 s

### Escena 4.3 — Mover, rotar y bajar (código)
- 🎙️ **Narración:** "Mover suma o resta a la columna. Rotar avanza al siguiente estado, y con el operador módulo, al llegar al final, vuelve al principio. La caída automática usa el reloj del juego para bajar cada cierto tiempo."
- 🖥️ **En pantalla:** editor mostrando `mover`, `rotar` (resaltar el `%`) y `bajar`.
- ⏱️ 60 s

### Escena 4.4 — Verlo funcionar (captura del juego)
- 🎙️ **Narración:** "¡Mira! La pieza baja sola. Con las flechas la muevo a los lados, con la de arriba la roto, y con la de abajo baja más rápido. Por ahora, al tocar el fondo simplemente reaparece arriba. Eso lo arreglamos en la próxima lección."
- 🖥️ **En pantalla:** captura real del juego moviendo y rotando una pieza.
- ⏱️ 40 s

### Escena 4.5 — Cierre
- 🎙️ **Narración:** "Ya se mueve. Ahora falta que las piezas se queden pegadas y se acumulen. Vamos a las colisiones."
- 🖥️ **En pantalla:** texto "Siguiente: colisiones y fusión".
- ⏱️ 15 s

---

# Video 5 — Colisiones y fusión (5 - 6 min)

### Escena 5.1 — Objetivos
- 🎙️ **Narración:** "En esta lección las piezas dejarán de atravesarse: se detendrán al tocar el fondo u otra pieza, y se quedarán pegadas. Eso es acumular, como en el Tetris de verdad."
- 🖥️ **En pantalla:** diapositiva de objetivos.
- ⏱️ 20 s

### Escena 5.2 — ¿Es válida esta posición? (código)
- 🎙️ **Narración:** "La función es válida recorre solo las casillas ocupadas de la pieza y comprueba dos cosas: que no se salga de los bordes y que no pise una casilla ya ocupada. Fíjate en cómo sumamos la posición de la pieza y el desfase dentro de su matriz."
- 🖥️ **En pantalla:** editor mostrando `es_valida`; resaltar `f = fila + i`, `c = columna + j`.
- ⏱️ 60 s

### Escena 5.3 — Fusionar (código)
- 🎙️ **Narración:** "Cuando la pieza no puede bajar más, la fusionamos: copiamos sus números dentro del tablero. Importante: copiamos solo las casillas con número, nunca los ceros, para no borrar lo que ya estaba."
- 🖥️ **En pantalla:** editor mostrando `fusionar` y la llamada en `bajar`.
- ⏱️ 50 s

### Escena 5.4 — Verlo funcionar (captura del juego)
- 🎙️ **Narración:** "Ahora sí: dejo caer varias piezas y se van apilando sin borrarse. Nuestra pila de números empieza a crecer."
- 🖥️ **En pantalla:** captura real del juego acumulando varias piezas.
- ⏱️ 40 s

### Escena 5.5 — Pregunta y cierre
- 🎙️ **Narración:** "Piensa: ¿por qué copiamos solo las casillas con número y no los ceros? En la próxima lección, las filas completas van a desaparecer y llega la puntuación."
- 🖥️ **En pantalla:** diapositiva con la pregunta; texto "Siguiente: líneas y puntuación".
- ⏱️ 20 s

---

# Video 6 — Líneas, puntuación y fin del juego (5 - 6 min)

### Escena 6.1 — Objetivos
- 🎙️ **Narración:** "Convertimos la pila de piezas en un juego completo: las filas llenas desaparecen, sumamos puntos y el juego termina cuando ya no cabe una pieza nueva."
- 🖥️ **En pantalla:** diapositiva de objetivos.
- ⏱️ 20 s

### Escena 6.2 — Eliminar líneas completas (código)
- 🎙️ **Narración:** "Una fila está completa si no tiene ningún cero. Nos quedamos con las filas que aún tienen huecos, contamos cuántas quitamos y añadimos arriba esa misma cantidad de filas vacías. Así, lo de arriba baja."
- 🖥️ **En pantalla:** editor mostrando `eliminar_lineas`; resaltar `if 0 in fila` y el `tablero[:] = ...`.
- ⏱️ 60 s

### Escena 6.3 — Puntuación y fin (código)
- 🎙️ **Narración:** "Sumamos puntos según cuántas líneas quitamos de golpe: más líneas juntas, más puntos. Y si una pieza nueva no cabe al aparecer, el juego termina."
- 🖥️ **En pantalla:** editor mostrando `PUNTOS_POR_LINEAS` y la marca de `terminado` en `nueva_pieza`.
- ⏱️ 45 s

### Escena 6.4 — Verlo funcionar (captura del juego)
- 🎙️ **Narración:** "Completo una fila... ¡y desaparece! Los puntos suben. Y si lleno el tablero, aparece el fin del juego. Ya tenemos un Tetris jugable de principio a fin."
- 🖥️ **En pantalla:** captura real: completar una línea, ver el marcador subir y provocar el game over.
- ⏱️ 45 s

### Escena 6.5 — Cierre
- 🎙️ **Narración:** "Funciona completo, pero todavía en números. En la próxima lección le damos el toque visual: colores neón."
- 🖥️ **En pantalla:** texto "Siguiente: estilo neón".
- ⏱️ 15 s

---

# Video 7 — Estilo neón (4 - 5 min)

### Escena 7.1 — Objetivos
- 🎙️ **Narración:** "Momento de brillar. Pasamos de números a colores neón. Y aquí viene la mejor parte: no vamos a tocar la lógica del juego, ni una línea."
- 🖥️ **En pantalla:** diapositiva de objetivos; a un lado, comparación números vs. neón.
- ⏱️ 20 s

### Escena 7.2 — Un color por número (código)
- 🎙️ **Narración:** "Creamos un diccionario que asocia cada número de pieza a un color neón: la I cian, la O amarilla, la T magenta, y así. Sobre un fondo oscuro, resaltan muchísimo."
- 🖥️ **En pantalla:** editor mostrando el diccionario `COLORES`.
- ⏱️ 40 s

### Escena 7.3 — Solo cambia el dibujo (código)
- 🎙️ **Narración:** "Antes dibujábamos el número de la casilla; ahora pintamos un rectángulo con su color y un contorno claro para el brillo. Es la misma matriz de siempre; solo cambió cómo la mostramos."
- 🖥️ **En pantalla:** editor mostrando la función de dibujo de celda neón; opcional: `git diff` entre lección 6 y 7 mostrando que la lógica no cambió.
- ⏱️ 50 s

### Escena 7.4 — Verlo funcionar (captura del juego)
- 🎙️ **Narración:** "Y aquí está: el mismo Tetris, ahora con piezas neón brillantes. Se ve profesional, y no tocamos la lógica. Ese es el poder de separar los datos de la presentación."
- 🖥️ **En pantalla:** captura real del juego en modo neón.
- ⏱️ 40 s

### Escena 7.5 — Actividad y cierre
- 🎙️ **Narración:** "Tu actividad: cambia la paleta de colores a tu gusto. En la última lección añadimos sonidos y animaciones."
- 🖥️ **En pantalla:** diapositiva de actividad; texto "Siguiente: sonidos y animaciones".
- ⏱️ 20 s

---

# Video 8 — Sonidos, animaciones y proyecto final (5 - 6 min)

### Escena 8.1 — Objetivos
- 🎙️ **Narración:** "Cerramos el curso con el pulido: un sonido al rotar, otro al eliminar líneas, y un destello cuando una pieza se pega. Además, eliges tu proyecto final."
- 🖥️ **En pantalla:** diapositiva de objetivos.
- ⏱️ 20 s

### Escena 8.2 — Audio seguro (código)
- 🎙️ **Narración:** "El audio es opcional. Lo envolvemos en un try-except: si el sonido falla o falta un archivo, el juego sigue funcionando igual, sin romperse. Aprender a hacer código que no se cae ante un fallo es clave."
- 🖥️ **En pantalla:** editor mostrando `audio.py` con el `try/except` en `iniciar_audio`.
- ⏱️ 50 s

### Escena 8.3 — La animación de destello (código)
- 🎙️ **Narración:** "La animación es un contador de fotogramas: mientras es mayor que cero, dibujamos un destello sobre las casillas recién pegadas. Dura pocos cuadros para no frenar el juego."
- 🖥️ **En pantalla:** editor mostrando el contador de animación en `grafico.py`.
- ⏱️ 45 s

### Escena 8.4 — Verlo y oírlo funcionar (captura del juego)
- 🎙️ **Narración:** "Escucha: al rotar suena un clic, y al completar una línea, un efecto. Y mira el destello cuando la pieza se pega. Todo esto es presentación; la lógica de matrices sigue intacta."
- 🖥️ **En pantalla:** captura real con audio: rotar, completar línea, ver el destello.
- ⏱️ 45 s

### Escena 8.5 — Proyecto final y despedida
- 🎙️ **Narración:** "¡Lo lograste! Construiste un Tetris completo entendiendo que todo es una matriz. Ahora elige un reto: niveles de velocidad, mostrar la próxima pieza, guardar el récord o más efectos neón. Sube tu rama, abre tu Pull Request y comparte tu creación. ¡Nos vemos!"
- 🖥️ **En pantalla:** lista de retos; luego terminal con `git push` y la pantalla de crear Pull Request; cierre con el juego neón de fondo.
- ⏱️ 40 s

---

## Notas de producción rápidas

- **Duración total estimada:** ~40-45 minutos repartidos en 9 videos (intro + 8 lecciones).
- **Voz IA:** elige una voz en español neutro; ritmo pausado. Herramientas: Fliki, HeyGen, Coursebox (revisar límites del plan gratuito).
- **Diapositivas:** Gamma o Canva (plan gratis) para las escenas de teoría.
- **Grabación de pantalla:** OBS Studio para editor, terminal y ventana del juego.
- **Subtítulos:** actívalos siempre (accesibilidad); Fliki y los editores gratis los autogeneran.
- **Reutiliza clips:** la captura del juego neón sirve para intro, cierres y miniaturas.
