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


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # L 1.1.4 — Errores en Python
    **Programación con Python I — Fundamentos · Módulo 1 · Unidad 1.1**

    ---

    **Errores** — cómo leerlos y qué información nos dan

    > Los errores no son un fracaso — son información.<br>
    > Aprender a leerlos es una habilidad fundamental.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Errores en Python

    Cuando Python no puede ejecutar lo que escribiste, muestra un **mensaje
    de error**. Ese mensaje tiene tres partes:

    1. **Ubicación** — archivo y número de línea donde ocurrió el error
    2. **Contexto** — la línea de código con `^` señalando el problema
    3. **Tipo y descripción** — qué tipo de error es y por qué

    Vamos a provocar errores a propósito para aprender a leerlos.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ### SyntaxError — error de sintaxis

    Ocurre cuando el código no sigue las reglas de escritura de Python.<br>
    Es el error más común al empezar.

    La celda de abajo tiene un error intencional: dos operadores juntos.<br>
    Ejecútala y lee el mensaje.
    """)
    return


app._unparsable_cell(
    r"""
    5 + * 2
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Mensaje esperado:**
    ```
    line 1
        5 + * 2
            ^
    SyntaxError: invalid syntax

    ```

    El símbolo `^` señala exactamente dónde está el problema.</br>
    En este caso: **el operador `*` no puede estar justo después del operador `+`
    sin un valor entre ellos.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ### NameError — nombre no definido

    Ocurre cuando usas un nombre de función o variable que no existe todavía.<br>
    En este caso la función `ent` en lugar de `int`
    """)
    return


@app.cell
def _(ent):
    ent(5.6)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Mensaje esperado:**
    ```
    Traceback (most recent call last):
      Cell marimo://notebook.py#cell=cell-7 , line 1, in <module>
        ent(5.6)
        ^^^
    NameError: name 'ent' is not defined. Did you mean: 'int'?
    ```

    Python te dice exactamente qué nombre no encontró.<br>
    Verás este error cuando escribas mal el nombre de una función o variable
    o la uses antes de haberla definido.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ### ZeroDivisionError — división entre cero<br>

    En python como en matemáticas la división entre cero no está definida<br>
    En esta división se escribió `0` en lugar de `0.5`
    """)
    return


@app.cell
def _():
    1 / 0
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Mensaje esperado:**
    ```
    Traceback (most recent call last):
      Cell marimo://notebook.py#cell=cell-10 , line 1, in <module>
        1 / 0
        ~~^~~
    ZeroDivisionError: division by zero

    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Cómo leer un error — resumen

    Cuando veas un error:

    1. **No lo cierres inmediatamente** — léelo completo
    2. **Busca el número de línea** — te dice dónde está el problema
    3. **Lee el tipo de error** — `SyntaxError`, `NameError`, `ZeroDivisionError`...
    4. **Lee la descripción** — suele decirte exactamente qué corregir
    5. **Corrige y vuelve a ejecutar**

    > Con práctica, leer errores se vuelve tan natural como leer el código.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## ✅ Resumen de la Unidad 1.1 — Python como calculadora

    | Lección | Temas |
    |---------|-------|
    | L 1.1.1 | 7 operadores aritméticos: `+` `-` `*` `/` `//` `**` `%` |
    | L 1.1.2 | Orden de operaciones · Paréntesis · Espaciado (PEP 8) |
    | L 1.1.3 | `int` vs `float` · `type()` · Casting: `int()` `float()` |
    | L 1.1.4 | Mensajes de error: SyntaxError, NameError, ZeroDivisionError |

    ---
    **→ Siguiente unidad: U 1.2 — Variables, nombres y legibilidad**

    *¿Cómo guardar un valor para reutilizarlo? Eso es exactamente lo que es una variable.*
    """)
    return


@app.cell(hide_code=True)
def _():
    return


if __name__ == "__main__":
    app.run()
