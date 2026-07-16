import marimo

__generated_with = "0.23.14"
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
    # L 1.2.1 — Variables:<br> asignación y reasignación
    **Programación con Python I — Fundamentos · Módulo 1 · Unidad 1.2**

    ---

    Una **variable** es un nombre que se asigna a un valor. Es como una etiqueta pegada a un objeto.<br>
    En lugar de escribir el valor directamente cada vez,
    le das un nombre y ese nombre lo puedes usar en cualquier parte.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > **Cómo funciona la salida automática de una celda:** <br>
    > La expresión o valor de la última línea de la celda se presenta en la salida automática de la celda.
    >
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Asignar un valor a una variable

    La sintaxis es: `nombre = valor`

    Ejecuta la celda de abajo. Observa que **no aparece ningún resultado**.<br>
    Python asigna el nombre de variable *`edad`* al valor *`21`* pero no muestra nada.
    """)
    return


@app.cell
def _():
    edad = 21
    peso = 65.5
    return edad, peso


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Sin salida — eso es correcto. La última línea de la celda no contiene una expresión.<br>
    La variable `edad` ahora se refiere al objeto `21 (tipo int)` - un valor int<br>
    La variable `peso` se refiere al objeto `65.5 (tipo float)` - un valor float<br>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > Cuando asignas una variable (`edad = 21`), no aparece ningún resultado.<br>
    > Si quieres presentar el valor de una variable escribe el nombre en la última línea de la celda y ejecútala.
    """)
    return


@app.cell
def _(edad):
    edad
    return


@app.cell
def _(peso):
    peso
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## `x + 1` no cambia `x`

    Antes de ejecutar: ¿cuánto crees que vale `x` después de esta celda?
    """)
    return


@app.cell
def _():
    x = 2
    x + 1
    return (x,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    El resultado es `3`. Pero ahora pregunta: ¿cambió `x`?
    """)
    return


@app.cell
def _(x):
    # ¿Cuánto vale x ahora?
    x
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **`x` sigue siendo `2`.**

    `x + 1` calculó `3`, lo mostró, y lo descartó.
    No modificó `x`.

    > El signo `=` en Python **no** es una igualdad matemática.<br>
    > Es una instrucción: *"asigna esta variable a este valor"*.<br>
    > `x + 1` no es una instrucción de asignación — solo calcula.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Reasignación: `y = y + 1`

    Asignemos la variable `y` al valor `3.0 (tipo float)`.<br>
    Para cambiar el valor de `y`, hay que asignarlo explícitamente.<br>
    Python evalúa el lado derecho primero, luego reasigna `y` al resultado.
    """)
    return


@app.cell
def _():
    y = 3.0
    y = y + 1
    y
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > Por ahora, lo importante es entender el concepto: <br>
    > **asignar guarda, expresión sin asignar no guarda**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > **Nota importante sobre molab:** En este entorno, cada variable solo puede definirse en **una única celda**. Si intentas asignar el mismo nombre de variable en celdas distintas, el sistema generará un error.

    >**¿Por qué?** Porque molab utiliza un modelo de ejecución basado en dependencias. Al asegurar que cada variable tenga un único origen, garantizamos que el cuaderno siempre refleje un estado coherente y predecible. Si necesitas actualizar un valor, hazlo siempre dentro de la celda donde se definió originalmente.

    Observa lo que sucede cuando asignas una variable `L` a un valor 10 y luego tratas de incrementarlo en otra celda
    """)
    return


@app.cell
def _():
    L = 10
    L
    return (L,)


@app.cell
def _():
    L = L + 20
    return (L,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Tipado dinámico: las variables pueden cambiar de tipo

    En Python, una variable no tiene un tipo fijo.
    El tipo de la variable sigue al tipo del valor al que se asigna.

    *Observa lo que sucede cuando asignas una variable `w` a un valor `3 tipo int` y reasignas `w` a un valor `2.0 tipo float` mostrando el tipo en otra celda.*
    """)
    return


@app.cell
def _():
    # Ahora asignamos w a un int, luego a un float
    w = 3
    w = 2.0         # Descomenta y vuelve a ejecutar 
    w
    return (w,)


@app.cell
def _(w):
    type(w)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `w` pasó de ser `int` a ser `float` simplemente por asignarle un valor diferente.
    Python lo permite sin ningún error — es el **tipado dinámico**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > **Nota sobre molab:** *En molab si cambias el valor de `x` en una celda, todas las celdas que han usado `x` se actualizan automáticamente. Eso hace que el cuaderno sea más predecible y seguro.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 3

    Predice cada resultado antes de ejecutar.
    ---
    """)
    return


@app.cell
def _():
    # Paso 1: definir z
    z = 20
    z
    return (z,)


@app.cell
def _(z):
    # Paso 2: z + 1 — ¿cambia z?
    z + 1
    return


@app.cell
def _(z):
    # Paso 3: verificar que z no cambió
    z
    return


@app.cell
def _():
    # Paso 4: cambiar z1 a float y reasignar a un int
    z1 = 24 / 6       # Asigna z1 a un valor float 24 / 6 
                      # (/ siempre da float)
    #z1 = 24 * 6      # Descomenta y vuelve a ejecutar 

    #z1 = z1 + 1.0
    z1
    return (z1,)


@app.cell
def _(z1):
    # Paso 5: ¿qué tipo tiene z1 ahora?
    type(z1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Resumen

    | Expresión | ¿Guarda el resultado? | Salida |
    |-----------|----------------------|--------|
    | `x = 2`   | ✅ Sí — en `x`       | Sin salida |
    | `x + 1`   | ❌ No                | Muestra el resultado |
    | `x = x + 1` | ✅ Sí — en `x`    | Sin salida |
    | `x`       | —                    | Muestra el valor de `x` |

    ---
    **→ Siguiente lección: L 1.2.2 — Casting y Actividad 1**

    *Vamos a ver cómo convertir tipos explícitamente y a completar la primera actividad integradora.*
    """)
    return


@app.cell(hide_code=True)
def _():
    return


if __name__ == "__main__":
    app.run()
