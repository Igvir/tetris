# 🎮 Tetris con Matrices en Python

Proyecto educativo para aprender el manejo de **matrices (listas de listas)** en Python construyendo un **Tetris** con **Kiro** y **spec driven development**.

Es la evolución del curso anterior [snake_game](https://github.com/Igvir/snake_game): mientras Snake enseñó los fundamentos (variables, listas, tuplas, bucles y una introducción a Pygame), aquí damos el siguiente paso conceptual: **todo en Tetris es una matriz**.

## 🧠 La gran idea: todo es una matriz

- El **tablero** es una matriz de 10 columnas × 20 filas.
- Cada **pieza** es una matriz donde `0` es una casilla vacía y un número del 1 al 7 la identifica.
- **Rotar** no calcula nada: solo cambia la matriz de la pieza por otra predefinida.
- Al tocar la base u otra pieza, la matriz de la pieza se **fusiona** (se copia) en la matriz del tablero.

El curso avanza por etapas: primero la ventana de Pygame dibuja los **números** de las matrices, y al final evoluciona a un vistoso estilo de **colores neón**, con sonidos y animaciones.

## 🎯 Objetivos de aprendizaje

- Entender y manipular matrices (listas de listas).
- Recorrer matrices con bucles anidados (`fila`, luego `columna`).
- Separar la **lógica** del juego de la **presentación** (Pygame).
- Detectar colisiones, fusionar piezas y eliminar líneas.
- Usar Kiro y specs para construir un proyecto paso a paso.

## 📋 Requisitos

- Python 3.8 o superior
- Pygame 2.5.2

## 🚀 Instalación

```bash
# 1. (Recomendado) crear un entorno virtual
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

# 2. Instalar dependencias
pip install -r requirements.txt
```

## ▶️ Cómo jugar

```bash
python main.py            # estilo neón (por defecto)
python main.py numeros    # estilo números (Etapa 1 del tutorial)
```

### Controles

| Tecla        | Acción                       |
|--------------|------------------------------|
| ← →          | Mover la pieza a los lados   |
| ↑            | Rotar la pieza               |
| ↓            | Bajar más rápido             |
| Barra espacio| Caída instantánea            |
| R            | Reiniciar (al terminar)      |
| Esc          | Salir                        |

## 📁 Estructura del proyecto

```
tetris/
├── tetris/
│   ├── piezas.py     # Matrices de cada pieza, rotaciones y colores neón
│   ├── tablero.py    # Matriz del tablero: crear, validar, fusionar, líneas
│   ├── juego.py      # Lógica del juego: pieza activa, movimiento, puntuación
│   ├── grafico.py    # Presentación en Pygame (números y neón) + animaciones
│   └── audio.py      # Sonidos opcionales con pygame.mixer
├── assets/sonidos/   # Sonidos (giro.wav, linea.wav) — opcionales
├── docs/
│   ├── guia_estudiante.md   # Curso paso a paso para el estudiante
│   └── guia_instructor.md   # Guía docente: planificación, evaluación, soluciones
├── tests/            # Pruebas de la lógica de matrices
├── main.py           # Punto de entrada
├── requirements.txt
└── README.md
```

## 📚 Guías del curso

- **[Guía del estudiante](docs/guia_estudiante.md)** — lecciones progresivas con prompts de Kiro.
- **[Guía del instructor](docs/guia_instructor.md)** — planificación, errores comunes, soluciones y rúbrica.

## 🌱 Recorrido paso a paso (ramas por lección)

Para ver el avance del proyecto **lección por lección**, cada etapa vive en su
propia rama de Git. Empiezas viendo la **matriz con números** y terminas en el
estilo **neón** con sonidos. Cambia de rama con `git checkout <rama>` y ejecuta
`python main.py`.

| Rama | Qué se ve |
|------|-----------|
| `leccion-1-matriz-tablero` | La matriz del tablero 10×20 con números (en la terminal) |
| `leccion-2-piezas` | Las piezas como matrices y sus rotaciones (en la terminal) |
| `leccion-3-ventana-numeros` | Primera ventana de Pygame dibujando los números |
| `leccion-4-pieza-cae` | Una pieza cae, se mueve y rota (números) |
| `leccion-5-colisiones-fusion` | Las piezas se detienen y se acumulan (números) |
| `leccion-6-lineas-puntuacion` | Líneas completas, puntuación y fin del juego (números) |
| `leccion-7-neon` | El mismo juego, ahora con colores neón |
| `leccion-8-sonidos-animaciones` | Versión final: sonidos y animaciones |

```bash
git checkout leccion-1-matriz-tablero   # empieza aquí
python main.py
# ... cuando termines, pasa a la siguiente:
git checkout leccion-2-piezas
```

> La rama `main` contiene el juego completo como referencia. Las primeras
> lecciones muestran los **números** de las matrices antes de llegar al color,
> para entender primero la estructura de datos.

## 🧪 Pruebas

```bash
python -m pytest tests/
```

## 📝 Entrega de la asignación

La entrega se realiza mediante **Git**. Debes crear una rama con tu nombre y abrir un **Pull Request**: ese PR es la evidencia de que completaste la asignación.

```bash
# 1. Clona el repositorio
git clone <url-del-repositorio>
cd tetris

# 2. Crea una rama con tu nombre
git checkout -b tetris-nombre-apellido

# 3. Trabaja en tu solución y guarda los cambios
git add .
git commit -m "Completa la asignacion de Tetris"

# 4. Sube tu rama
git push -u origin tetris-nombre-apellido

# 5. Abre un Pull Request hacia la rama principal desde la interfaz de GitHub
```

> El **Pull Request** es la prueba de que terminaste la asignación. Asegúrate de que tu rama lleve tu nombre y de describir brevemente lo que hiciste en la descripción del PR.

## 💡 Ideas de mejora

- Niveles de velocidad que aumentan con las líneas.
- Mostrar la próxima pieza.
- Guardar el récord en un archivo.
- Más efectos neón (resplandor, degradados, destello al hacer un Tetris).

## ☕ Apóyame

Si este proyecto te resulta útil para aprender o enseñar, puedes invitarme un café. ¡Gracias por el apoyo!

<a href="https://buymeacoffee.com/igvir" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="50" width="210"></a>

## 📄 Licencia

Proyecto educativo de uso libre.
