import marimo

__generated_with = "0.24.0"
app = marimo.App(
    width="medium",
    app_title="Notebook",
    css_file="/usr/local/_marimo/custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # L 1.2.2 — Casting y Asignación Compuesta
    **Programación con Python I — Fundamentos · Módulo 1 · Unidad 1.2**

    ---

    En L 1.2.1 viste que Python cambia el tipo de una variable automáticamente al asignarle un valor de tipo diferente — **tipado dinámico**.

    En esta lección vas a aprender a controlar el tipo tú mismo con **casting**, y a escribir reasignaciones de forma más corta con el operador **`+=`**.

    **Casting** es convertir un valor de un tipo a otro de forma explícita.
    Ya vimos `int()` y `float()` en L 1.1.3 aplicados a valores literales.
    Aquí los usamos con variables.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Tipado dinámico: el tipo sigue al valor

    Sigue la secuencia y observa cómo cambia el tipo de `y`:
    """)
    return


@app.cell
def _():
    y = 10          # y empieza como int
    y = y - 10.0    # y se convierte en float al restar un float,
    y
    return (y,)


@app.cell
def _(y):
    type(y)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > `y` pasó de `int` a `float` con solo asignarle un valor diferente.
    > El tipo cambió automáticamente — Python lo dedujo del valor.
    > Esto es el **tipado dinámico** que ya conoces.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Casting explícito: `int()` y `float()`

    El casting te da **control directo** sobre el tipo — no tienes que esperar que Python lo deduzca.

    Ya usaste `int()` y `float()` con literales en L 1.1.3.
    Aquí los aplicamos sobre variables.

    ### De float a int

    Usamos `int()` para convertir `x` de vuelta a entero.
    """)
    return


@app.cell
def _():
    x = 1.7        # x es float
    x_entero = int(x)
    x_entero
    return x, x_entero


@app.cell
def _(x_entero):
    type(x_entero)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > `int()` **trunca** — descarta los decimales sin redondear.
    > `int(1.7)` da `1`, no `2`.

    > **Nota:** el casting no modifica la variable original.
    > `int(x)` convierte el valor temporalmente.
    > Para que el cambio persista hay que asignarlo:
    > `x = int(x)` o, como hicimos aquí, `x_entero = int(x)`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Verifica que `x` sigue siendo float después del casting:
    """)
    return


@app.cell
def _(x):
    x
    return


@app.cell
def _(x):
    type(x)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > `x` no cambió — el casting solo afectó a `x_entero`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### De int a float

    La dirección contraria también funciona:
    """)
    return


@app.cell
def _():
    z = 5          # z es int
    z_decimal = float(z)
    z_decimal
    return (z_decimal,)


@app.cell
def _(z_decimal):
    type(z_decimal)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > `float(5)` da `5.0` — añade el punto decimal.
    > Útil cuando quieres asegurarte de que una operación
    > posterior produzca resultado decimal.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Casting en una expresión

    El casting puede aplicarse directamente dentro de una expresión, sin necesidad de una variable intermedia:
    """)
    return


@app.cell
def _():
    # Antes de ejecutar: ¿cuánto da esto? ¿int o float?
    int(7 / 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > `7 / 2 = 3.5` (float), luego `int(3.5) = 3` (trunca).
    > El casting se aplica **después** de evaluar la expresión.
    """)
    return


@app.cell
def _():
    # ¿Y esto?
    float(7 // 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > `7 // 2 = 3` (int), luego `float(3) = 3.0`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Asignación compuesta: `+=`

    En L 1.2.1 aprendiste a reasignar una variable:

    ```python
    A = A + 1
    ```

    Esta operación es tan frecuente que Python ofrece una forma más corta.
    Estas dos expresiones hacen **exactamente lo mismo**:

    | Forma larga | Forma corta |
    |---|---|
    | `A = A + 1` | `A += 1` |
    | `A = A + 5` | `A += 5` |

    La lectura natural de `A += 1` es: *"aumenta A en 1"*.
    """)
    return


@app.cell
def _():
    # Antes de ejecutar: ¿cuánto vale A al final?
    A = 3.0
    A += 1
    A
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > `A` empieza en `3.0`. `A += 1` equivale a `A = A + 1 = 4.0`.
    > El tipo sigue siendo `float` porque `A` ya era float.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    El valor a la derecha de `+=` puede ser cualquier expresión,
    no solo un literal:
    """)
    return


@app.cell
def _():
    # Antes de ejecutar: ¿cuánto vale total?
    incremento = 7
    total = 100
    total += incremento
    total
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > `total = 100 + 7 = 107`.
    > `incremento` no cambia — solo se usa su valor.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Ejercicio: predice antes de ejecutar
    """)
    return


@app.cell
def _():
    # Paso 1
    puntos = 50

    # Paso 2 — ¿cuánto vale puntos?
    puntos += 25

    # Paso 3 — ¿cuánto vale puntos?
    puntos += puntos
    puntos
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > **Paso 3:** `puntos += puntos` equivale a `puntos = puntos + puntos`.
    > En ese momento `puntos` vale `75`, así que `75 + 75 = 150`.
    > El lado derecho se evalúa **antes** de que `puntos` cambie.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Resumen

    | Concepto | Ejemplo | Resultado |
    |---|---|---|
    | Casting a `int` | `int(1.7)` | `1` — trunca, no redondea |
    | Casting a `float` | `float(5)` | `5.0` |
    | Casting en expresión | `int(7 / 2)` | `3` |
    | Asignación compuesta | `x += 1` | equivale a `x = x + 1` |

    > **Regla clave del casting:** el casting no modifica la variable original
    > a menos que asignes el resultado explícitamente.

    ---
    **→ Siguiente lección: L 1.2.3 — Nombres de variables y variables múltiples**

    *¿Qué nombres puede tener una variable en Python? ¿Y cuáles están prohibidos?*
    """)
    return


@app.cell(hide_code=True)
def _():
    return


if __name__ == "__main__":
    app.run()
