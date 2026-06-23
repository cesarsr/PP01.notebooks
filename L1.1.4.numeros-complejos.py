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
    # L 1.1.4 — Números complejos
    **Programación con Python I — Fundamentos · Módulo 1 · Unidad 1.1**

    ---

    **Números complejos** — el tercer tipo numérico de Python
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Números complejos: el tipo `complex`

    Python soporta números complejos de forma nativa.
    Un número complejo tiene una parte real y una parte imaginaria.

    En matemáticas la parte imaginaria usa **i**.
    Python usa **j** — la convención de la ingeniería.
    """)
    return


@app.cell
def _():
    (2+3j)
    return


@app.cell
def _():
    type(2+3j)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - `(2+3j)` es un número complejo: parte real `2`, parte imaginaria `3j`
    - Su tipo es `<class 'complex'>` — el tercer tipo numérico de Python

    Puedes operar con números complejos igual que con `int` y `float`:
    """)
    return


@app.cell
def _():
    (2+3j) + (1-1j)
    return


@app.cell
def _():
    (2+3j) * (1-1j)
    return


@app.cell
def _():
    (2+3j) / (1-5j)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Python calcula con números complejos sin ningún problema.

    > **¿Cuándo se usan?**
    > En ingeniería eléctrica, procesamiento de señales y física.
    > Si no trabajas en esas áreas, con saber que existen es suficiente.

    ---
    ## Resumen de los tres tipos numéricos de Python

    | Tipo | Nombre completo | Ejemplo | `type()` |
    |------|----------------|---------|----------|
    | `int` | Integer (entero) | `6` | `<class 'int'>` |
    | `float` | Floating point (decimal) | `6.0` | `<class 'float'>` |
    | `complex` | Complex (complejo) | `2+3j` | `<class 'complex'>` |
    """)
    return


if __name__ == "__main__":
    app.run()
