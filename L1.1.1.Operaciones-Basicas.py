# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.23.7",
# ]
# ///

import marimo

__generated_with = "0.23.5"
app = marimo.App(
    css_file="/usr/local/_marimo/custom.css",
    auto_download=["html"],
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # L 1.1.1 — Python como calculadora: operaciones básicas
    **Programación con Python I — Fundamentos · Módulo 1 · Unidad 1.1**

    ---

    En esta lección vas a ejecutar operaciones matemáticas directamente en Python.
    Escribe una expresión en una celda, presiona **Ctrl + Enter**, y el resultado
    aparece automáticamente debajo. No necesitas nada más por ahora.

    > **Cómo ejecutar una celda:**
    > Haz clic dentro de la celda y presiona **Ctrl + Enter** (Windows / Linux)
    > o **Cmd + Enter** (Mac).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Las cuatro operaciones que ya conoces

    Ejecuta cada celda y observa el resultado.
    """)
    return


@app.cell
def _():
    # ■ Celda 1 (Suma)
    5 + 2    
    return


@app.cell
def _():
    # ■ Celda 2 (Resta)
    5 - 2
    return


@app.cell
def _():
    # ■ Celda 3 (Multiplicación)
    5 * 2
    return


@app.cell
def _():
    # ■ Celda 4 (División convencional)
    5 / 2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    👉**¿Notaste el resultado de la división?**
    El resultado de la división `5 / 2` es `2.5` , no es `2`

    En Python la división (barra simple `/`) **siempre devuelve un número decimal**,
    aunque el resultado sea exacto.<br> `10 / 2` da `5.0`, no `5`.<br>
    Eso es intencional — lo veremos en detalle más adelante.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## División entera: el operador `//`

    La doble barra devuelve solo la parte entera — sin decimales.
    No redondea: descarta los decimales.
    """)
    return


@app.cell
def _():
    # ■ Celda 5 (División entera: devuelve solo la parte entera del cociente)
    5 // 2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    El resultado de la división entera 5 // 2 = 2 es el entero antes del punto decimal del resultado de la división, sin redondeo.

    `5 // 2` da `2`, no `2.5`.

    Compara:
    - `/`  → siempre decimal:  `5 / 2 = 2.5`
    - `//` → siempre entero:   `5 // 2 = 2`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Potenciación: el operador `**`

    En Python el operador exponencial se escribe con dos asteriscos, no con `^`.
    """)
    return


@app.cell
def _():
    # ■ Celda 6 (Potenciación: 5 al cuadrado)
    5 ** 2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Esto es:
    - 5 al cuadrado, o
    - 5 elevado a la potencia 2
    $$5^2 = 5 * 5 = 25$$

    `5 ** 2` es 5 al cuadrado = `25`.

    > El símbolo `**` no es universal para la elevación a una potencia, pero debería serlo. Por definición, la elevación a una potencia
    > es una multiplicación repetida. Utilizar el símbolo `*` dos veces representa una multiplicación repetida.
    > Es conciso, rápido y eficiente.<br>

    Prueba en la celda de abajo: ¿cuánto es `5 ** 3`?
    """)
    return


@app.cell
def _():
    5 ** 3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Módulo: el operador `%`

    El símbolo `%` en Python **no significa porcentaje**.<br>
    Se llama **módulo** y devuelve el *residuo* de una división entera.
    """)
    return


@app.cell
def _():
    # ■ Celda 7 (Módulo: devuelve el residuo de la división)
    5 % 2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **¿Cómo funciona?**

    $5 ÷ 2 = 2$ con residuo  1<br>  porque $5 = 2 × 2 + 1$<br>

    La división entera `//` te da el `2`.<br>
    El módulo `%` te da el residuo: `1`.

    **Analogía del reloj:** imagina un reloj de 12 horas.
    Si son las 10 y pasan 5 horas, no son las 15 — son las **3**.
    Eso es exactamente lo que hace el módulo: cuenta en ciclos.

    **Uso frecuente:** saber si un número es par o impar.
    - Par:   `número % 2 = 0`
    - Impar: `número % 2 = 1`

    Compruébalo:
    """)
    return


@app.cell
def _():
    6 % 2
    return


@app.cell
def _():
    7 % 2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Resumen — Los 7 operadores aritméticos de Python

    | Operador | Nombre | Ejemplo | Resultado |
    |:--------:|--------|---------|:---------:|
    | `+`  | **Suma**             | `5 + 2`  | `7`   |
    | `-`  | **Resta**            | `5 - 2`  | `3`   |
    | `*`  | **Multiplicación**   | `5 * 2`  | `10`  |
    | `/`  | **División**         | `5 / 2`  | `2.5` |
    | `//` | **División entera**  | `5 // 2` | `2`   |
    | `**` | **Potenciación**        | `5 ** 2` | `25`  |
    | `%`  | **Módulo (residuo)** | `5 % 2`  | `1`   |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ### ✏️ Ejercicio 1 — Convertir horas a días<br>
    Dadas 100 horas, ¿cuántos días completos son y cuántas horas sobran?
    Pista: un día tiene 24 horas. Usa // para los días y % para las horas sobrantes.
    """)
    return


@app.cell
def _():
    100 % 24
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ### ✏️ Ejercicio 2 — Repartir minutos en bloques

    Tienes **500 minutos** de video y los quieres dividir en bloques de **45 minutos**.
    ¿Cuántos bloques completos puedes armar y cuántos minutos sobran?
    """)
    return


@app.cell
def _():
    500 // 45
    500 % 45
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## ✅ Lo que aprendiste en esta lección

    - Python tiene **7 operadores aritméticos**: `+` `-` `*` `/` `**` `%` `//`
    - La salida directa muestra el **último valor** de la celda
    - `/` siempre devuelve decimal — `//` devuelve solo la parte entera
    - `%` devuelve el **residuo** de la división — útil para distribución y paridad
    - `//` y `%` trabajan en equipo

    ---
    **→ Siguiente lección: L 1.1.2 — Orden de operaciones**

    *¿Por qué `5 + 2 * 3` da `11` y no `21`? Lo vemos en la próxima lección.*
    """)
    return


if __name__ == "__main__":
    app.run()
