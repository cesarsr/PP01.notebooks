import marimo

__generated_with = "0.23.9"
app = marimo.App(
    width="medium",
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
    # L 1.1.3 — Tipos numéricos: int, float, type() y casting
    **Programación con Python I — Fundamentos · Módulo 1 · Unidad 1.1**

    ---

    Python tiene dos tipos principales para los números: **int** (entero)
    y **float** (decimal). En esta lección vas a ver la diferencia,
    cómo identificar el tipo de un valor, y cómo convertir entre ellos.

    > **Antes de ejecutar cada celda, intenta predecir el resultado.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## int y float: el mismo valor, distinto tipo

    Ejecuta estas dos celdas y observa la diferencia en el resultado.
    """)
    return


@app.cell
def _():
    6
    return


@app.cell
def _():
    6.0
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `6` y `6.0` valen lo mismo matemáticamente.
    Pero para Python son de **distinto tipo**.

    - `6`   → entero (**int** — integer)
    - `6.0` → decimal (**float** — floating point)

    ¿Cómo saber el tipo de cualquier valor? Con la función `type()`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## La función `type()`

    `type(valor)` te dice de qué tipo es ese valor.
    """)
    return


@app.cell
def _():
    type(6)
    return


@app.cell
def _():
    type(6.0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - `type(6)`   → `<class 'int'>`
    - `type(6.0)` → `<class 'float'>`

    La palabra **class** es simplemente la forma que tiene Python
    de referirse a los tipos. Por ahora ignórala — lo importante
    es lo que viene después: `'int'` o `'float'`.

    ---
    ### ¿Qué pasa cuando operas int y float juntos?
    """)
    return


@app.cell
def _():
    5 + 3.14
    return


@app.cell
def _():
    type(5 + 3.14)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Cuando combinas un `int` y un `float`, el resultado es siempre `float`.

    Python elige el tipo más general para no perder información.
    Esto se llama **type coercion** — conversión automática de tipos.

    > Recuerda lo que vimos en L 1.1.1: la división con `/`
    > también devuelve siempre `float`, aunque los dos operandos sean `int`.
    """)
    return


@app.cell
def _():
    10 / 2
    return


@app.cell
def _():
    type(10 / 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Casting: convertir entre tipos

    **Casting** es convertir un valor de un tipo a otro.
    Python tiene funciones para eso: `int()` y `float()`.

    ### `int()` — convertir a entero

    > ⚠️ **Atención:** `int()` **trunca**, no redondea.
    > Descarta la parte decimal sin importar su valor.
    """)
    return


@app.cell
def _():
    int(7.9)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **`int(7.9)` da `7`, no `8`.**

    Aunque `.9` está muy cerca de `1`, `int()` simplemente descarta
    todo lo que está después del punto decimal.

    Verifica con otro ejemplo:
    """)
    return


@app.cell
def _():
    int(7.1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `int(7.1)` también da `7`. El resultado es el mismo
    sin importar si el decimal es `.1` o `.9`.

    ### `float()` — convertir a decimal
    """)
    return


@app.cell
def _():
    float(6)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `float(6)` da `6.0`. Python añade la parte decimal.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Ejercicio 2 — Practica con type() y casting

    Predice el resultado de cada celda antes de ejecutarla.
    """)
    return


@app.cell
def _():
    # ¿Qué tipo devuelve esta operación?
    type(6 * 7)
    return


@app.cell
def _():
    # ¿Y esta?
    type(6 * 7.0)
    return


@app.cell
def _():
    # ¿Qué pasa al convertir este float a int?
    int(6.999)
    return


@app.cell
def _():
    # ¿Y este?
    int(-3.9)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **`int(-3.9)` da `-3`, no `-4`.**

    `int()` trunca hacia el cero — descarta la parte decimal
    independientemente del signo.

    ---
    ## Exploración libre

    Prueba tus propias combinaciones de `type()`, `int()` y `float()`.
    """)
    return


@app.cell
def _():
    # ¿Qué tipo tiene el resultado de 5 // 2?
    type(5 // 2)
    return


@app.cell
def _():
    # ¿Y el de 5.0 // 2?
    type(5.0 // 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > **Nota:** `5 // 2` da `int` porque ambos operandos son `int`.
    > `5.0 // 2` da `float` porque uno de los operandos es `float`.
    > La regla int + float = float aplica también a `//`.

    ---
    **→ Siguiente lección: L 1.1.4 — Números complejos y errores de Python**

    *¿Qué pasa cuando Python no puede entender lo que escribiste?*
    """)
    return


@app.cell(hide_code=True)
def _():
    return


if __name__ == "__main__":
    app.run()
