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
    # L 1.1.2 — Orden de operaciones y espaciado
    **Programación con Python I — Fundamentos · Módulo 1 · Unidad 1.1**

    ---

    Cuando una expresión tiene varias operaciones, Python sigue un orden
    de precedencia — igual que en matemáticas. En esta lección vas a ver
    cómo funciona ese orden y cómo controlarlo con paréntesis.

    > **Antes de ejecutar cada celda, intenta predecir el resultado.**
    > Anticiparlo te ayudará a comprender mejor cómo funciona el orden de las operaciones en Python.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## ¿Cuánto da esta expresión?

    Antes de ejecutar: ¿cuánto crees que da `5 + 2 * -3`?

    - Si sumas primero: `(5 + 2) * -3 = 7 * -3 = -21`
    - Si multiplicas primero: `5 + (2 * -3) = 5 + (-6) = -1`

    Ejecuta la celda y observa cuál elige Python.
    """)
    return


@app.cell
def _():
    5 + 2 * -3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Resultado: `-1`**

    Python multiplicó primero. Sigue el orden de precedencia de las matemáticas:

    | Precedencia | Operadores | Nombre |
    |:---------:|------------|--------|
    | 1 (más alta) | `()` | Paréntesis |
    | 2 | `**` | Potenciación |
    | 3 | `*`  `/`  `//`  `%` | Multiplicación y división |
    | 4 (más baja) | `+`  `-` | Suma y resta |

    > **Nota:** el signo negativo delante del `3` no es resta —
    > es parte del número `-3`. Python lo entiende perfectamente.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Los paréntesis tienen la precedencia más alta

    Si quieres que Python sume primero, usa paréntesis.
    Antes de ejecutar: ¿cuánto da `(5 + 2) * -3`?
    """)
    return


@app.cell
def _():
    (5 + 2) * -3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Resultado: `-21`**

    Con paréntesis Python suma primero: `5 + 2 = 7`, luego `7 * -3 = -21`.

    La misma expresión, distinto resultado — solo por los paréntesis.

    > **Regla práctica:** cuando tengas dudas sobre el orden de evaluación,
    > usa paréntesis. Hacen el código más claro y evitan errores.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Ejercicio 1 — Practica el orden de operaciones

    Predice el resultado de cada expresión antes de ejecutarla.
    Escribe tu predicción mentalmente (o en papel) y luego verifica.
    """)
    return


@app.cell
def _():
    # Ejercicio 1a
    # Pista: primero la potenciación, luego la resta, luego la división
    (100 - 5**3) / 5
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Razonamiento:**
    1. `5**3 = 125`  (potenciación primero)
    2. `100 - 125 = -25`  (resta)
    3. `-25 / 5 = -5.0`  (división — siempre decimal con `/`)
    """)
    return


@app.cell
def _():
    # Ejercicio 1b
    # Pista: el módulo tiene la misma precedencia que la multiplicación
    6 + 15 % 4
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Razonamiento:**
    1. `15 % 4 = 3`  (módulo antes que suma)
    2. `6 + 3 = 9`
    """)
    return


@app.cell
def _():
    # Ejercicio 1c
    # Pista: potenciaciones primero, luego división entera, luego suma
    2**2 + 24//4
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Razonamiento:**
    1. `2**2 = 4`  (potenciación)
    2. `24//4 = 6`  (división entera)
    3. `4 + 6 = 10`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 💡 Potenciación de una potencia.
    """)
    return


@app.cell
def _():
    # Cuál será el resultado de:
    2 ** 2 ** 3
    return


@app.cell
def _():
    # 2**2**3   # Python lo trata como: 2**(2**3)  →  2**8  →  256
    # (2**2)**3 # se evalúa como:       4**3        →  64
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Python sigue las convenciones estándar en matemáticas. <br>
    Las operaciones con la misma precedencia se evalúan en general de izquierda a derecha.<br>
    Pero qué pasa con expresiones como: 2 ** 2 ** 3

    `2 ** 2 ** 3`  equivale a $2^{2^3}$ <br>

    El orden de evaluación de $2^{2^3}$ en matemáticas es de arriba abajo.<br>
    Lo que equivale a evaluar de derecha a izquierda en Python. Es decir:


    `2 ** 2 ** 3` $=$ `2 ** (2 ** 3)`   $=2^{2^3}=256$

    En cambio:


    `(2 ** 2) ** 3`  $=(2^2)^3=64$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Espaciado: código que se puede leer

    Los espacios alrededor de los operadores **no afectan el resultado**,
    pero sí afectan la legibilidad. Ejecuta estas dos celdas:
    """)
    return


@app.cell
def _():
    # Sin espacios — funciona, pero es difícil de leer
    5+2*-3
    return


@app.cell
def _():
    # Con espacios — mismo resultado, mucho más claro
    5 + 2 * -3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Las dos expresiones dan el mismo resultado: `-1`.

    **Convención Python (PEP 8):** un espacio antes y después de cada operador.

    Adopta esta convención desde hoy. El código que escribes ahora
    lo vas a leer más adelante — querrás entenderlo rápido.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Exploración libre

    Escribe tus propias expresiones. Predice antes de ejecutar.
    """)
    return


@app.cell
def _():
    # ¿Cuánto da 2 + 3 * 4?
    2 + 3 * 4
    return


@app.cell
def _():
    # ¿Y (2 + 3) * 4?
    (2 + 3) * 4
    return


@app.cell
def _():
    # ¿Cuánto da 10 - 2**3 + 1?
    10 - 2**3 + 1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    **→ Siguiente lección: L 1.1.3 — Tipos numéricos: int, float, type() y casting**

    *¿Cuál es la diferencia entre `8` y `8.0`? ¿Y por qué le importa a Python?*
    """)
    return


@app.cell(hide_code=True)
def _():
    return


if __name__ == "__main__":
    app.run()
