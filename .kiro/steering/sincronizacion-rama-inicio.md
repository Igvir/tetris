---
inclusion: fileMatch
fileMatchPattern: 'tetris/*.py|main.py|docs/guia_estudiante*.md|tests/*.py|requirements.txt'
---

# Sincronización con la rama `inicio`

Este proyecto tiene dos ramas clave con una relación estricta:

- **`main`**: la **solución completa** del tutorial (juego funcional + guías + tests).
- **`inicio`**: la **plantilla de partida** del estudiante. Contiene el mismo
  andamiaje que `main` (estructura, `docs/`, `README.md`, `requirements.txt`,
  `assets/`, `tools/`, `tests/`) pero con los módulos del juego en `tetris/`
  como **esqueleto**: firmas y docstrings iguales a los de `main`, pero con el
  cuerpo reemplazado por `raise NotImplementedError(...)` y comentarios `TODO`
  que apuntan a la lección correspondiente.

El estudiante crea su rama de trabajo a partir de `inicio`
(`git checkout -b tetris-nombre origin/inicio`) y la completa siguiendo las
guías. Por eso `inicio` debe seguir siendo un punto de partida coherente.

## Reglas al modificar el proyecto

Cuando cambies cualquiera de estos elementos en `main`, revisa si `inicio`
necesita actualizarse para no quedar desincronizada:

1. **Firmas o nombres de funciones/clases en `tetris/*.py`**
   (por ejemplo `crear_tablero`, `es_valida`, `fusionar`, `eliminar_lineas`,
   la clase `Juego` y sus métodos, `jugar`, `Presentacion`): si cambian en
   `main`, la firma/docstring correspondiente en `inicio` debe cambiar igual,
   manteniendo el cuerpo como `NotImplementedError` + `TODO`.

2. **Constantes y datos compartidos** (`ANCHO`, `ALTO`, `NUMERO_PIEZA`,
   nombres de piezas, claves de `COLORES`, `INTERVALO_CAIDA`, `ESTILO_NUMEROS`,
   `ESTILO_NEON`): deben coincidir entre ambas ramas. En `inicio`, `PIEZAS`
   mantiene solo la pieza **T** como ejemplo resuelto y `COLORES` solo la
   entrada `0`; el resto queda como `TODO`.

3. **Las guías del estudiante** (`docs/guia_estudiante.md` y
   `docs/guia_estudiante_sin_kiro.md`): el código que muestran o que piden
   escribir debe corresponder con las firmas reales de `main` y con los `TODO`
   de `inicio`. Si cambia una lección, revisa que el esqueleto de `inicio`
   siga alineado con esa lección (mismos nombres, mismo mapeo de lección a
   función).

4. **`requirements.txt`, `tests/` y andamiaje** (`README.md`, `assets/`,
   `tools/`): deben ser idénticos entre `main` e `inicio`, salvo el aviso del
   `README.md` de `inicio` que indica que es la plantilla de partida.

## Cómo mantener la sincronía

- Los cambios de andamiaje o documentación (docs, README salvo el aviso,
  requirements, tests, assets, tools) pueden llevarse tal cual de `main` a
  `inicio` (por ejemplo con `git checkout main -- <ruta>` desde la rama
  `inicio`, o vía PR).
- Los cambios en `tetris/*.py` **no** se copian tal cual: en `inicio` solo se
  actualiza la firma y el docstring, dejando el cuerpo como `NotImplementedError`
  con un `TODO` que cite la lección.
- Regla de oro: **cualquier cosa que el estudiante deba escribir queda como
  `TODO` en `inicio`; todo lo demás debe ser idéntico a `main`.**
- Tras sincronizar, verifica en `inicio` que la sintaxis es válida y que
  `python main.py` muestra el mensaje amistoso de "falta completar código"
  en lugar de un error inesperado.
