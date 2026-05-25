# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.23.8",
# ]
# ///

import marimo

__generated_with = "0.23.5"
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
    # L 1.1.1 — Python como calculadora: operaciones básicas
    **Programación con Python I — Fundamentos · Módulo 1 · Unidad 1.1**

    ---

    Ejecuta cada celda con **Ctrl + Enter** y observa los resultados.
    Por ahora no necesitas entender todo el código — solo ejecuta y observa.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Parte 1 — Una operación, un resultado

    En Python puedes escribir una operación matemática y ver el resultado
    directamente. Ejecuta cada celda y observa qué aparece.
    """)
    return


@app.cell
def _():
    5 + 2
    return


@app.cell
def _():
    5 - 2
    return


@app.cell
def _():
    5 * 2
    return


@app.cell
def _():
    5 / 2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **¿Notaste algo?**
    `5 / 2` dio `2.5`, no `2`.
    En Python la división **siempre devuelve un número decimal**,
    aunque el resultado sea exacto. `10 / 2` da `5.0`, no `5`.
    Eso es intencional — lo veremos en detalle más adelante.

    Ahora prueba los otros dos operadores: exponente y módulo.
    """)
    return


@app.cell
def _():
    5 ** 2
    return


@app.cell
def _():
    5 % 2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **El operador `**` es el exponente.** `5 ** 2` es 5 al cuadrado = 25.

    **El operador `%` es el módulo** — devuelve el *residuo* de una división entera.
    `5 % 2` pregunta: ¿cuánto sobra de dividir 5 entre 2?
    5 = 2 × 2 + **1** → el residuo es **1**.

    Y el séptimo operador: la división entera `//`.
    """)
    return


@app.cell
def _():
    5 // 2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `5 // 2` da `2` — la parte entera de la división, sin decimales.
    No redondea: `17 // 3` da `5`, no `6`.

    ---
    ## Parte 2 — Ver varios resultados a la vez: `print()`

    Hasta ahora cada celda tenía una sola operación.
    Pero a veces quieres ver varios resultados juntos.
    Para eso existe la función `print()`.

    Ejecuta esta celda y observa la diferencia:
    """)
    return


@app.cell
def _():
    # Sin print(): solo se muestra el último valor
    5 + 2
    5 - 2
    5 * 2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ¿Viste? Solo apareció el resultado de `5 * 2`.
    Las dos primeras operaciones se ejecutaron pero no se mostraron.

    Con `print()` puedes mostrar todos los resultados que quieras:
    """)
    return


@app.cell
def _():
    print(5 + 2)
    print(5 - 2)
    print(5 * 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `print(valor)` muestra el valor en pantalla.
    Puedes poner cualquier operación o valor dentro de los paréntesis.

    Ahora veamos cómo `//` y `%` trabajan juntos en un problema real:
    """)
    return


@app.cell
def _():
    # ¿Cuántos grupos de 3 puedo hacer con 17 elementos?
    total = 17
    tamaño_grupo = 3

    print("Grupos completos:", total // tamaño_grupo)   # 5
    print("Sobrantes:       ", total % tamaño_grupo)    # 2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Resumen — Los 7 operadores aritméticos de Python

    | Operador | Nombre | Ejemplo | Resultado |
    |:--------:|--------|---------|:---------:|
    | `+`  | Suma             | `5 + 2`  | `7`   |
    | `-`  | Resta            | `5 - 2`  | `3`   |
    | `*`  | Multiplicación   | `5 * 2`  | `10`  |
    | `/`  | División         | `5 / 2`  | `2.5` |
    | `**` | Exponente        | `5 ** 2` | `25`  |
    | `%`  | Módulo (residuo) | `5 % 2`  | `1`   |
    | `//` | División entera  | `5 // 2` | `2`   |

    ---
    ## ✏️ Ejercicio 1 — Convertir horas a días

    Dadas **100 horas**, ¿cuántos días completos son y cuántas horas sobran?

    *Pista: un día tiene 24 horas. Usa `//` para los días y `%` para las horas sobrantes.*
    """)
    return


@app.cell
def _():
    horas = 100

    dias = horas // 24
    horas_sobrantes = horas % 24

    print(f"{horas} horas = {dias} días y {horas_sobrantes} horas sobrantes")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## ✏️ Ejercicio 2 — Repartir minutos en bloques

    Tienes **500 minutos** de video y los quieres dividir en bloques de **45 minutos**.
    ¿Cuántos bloques completos puedes armar y cuántos minutos sobran?
    """)
    return


@app.cell
def _():
    minutos_totales = 500
    duracion_bloque = 45

    bloques = minutos_totales // duracion_bloque
    minutos_sobrantes = minutos_totales % duracion_bloque

    print(f"{minutos_totales} minutos en bloques de {duracion_bloque}:")
    print(f"  Bloques completos : {bloques}")
    print(f"  Minutos sobrantes : {minutos_sobrantes}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 🏆 Reto — Una expresión para cada resultado

    Usando solo los números `2`, `3` y `4` (puedes repetirlos),
    escribe expresiones que produzcan exactamente los resultados del 1 al 6.
    Puedes usar cualquier operador.

    Ejemplo: `2 + 3 - 4` = **1** ✓

    Modifica las expresiones de abajo para obtener cada resultado:
    """)
    return


@app.cell
def _():
    print("Resultado 1:", 2 + 3 - 4)        # = 1  ✓ (ya está)
    print("Resultado 2:", 2 * 3 - 4)        # = 2  ✓
    print("Resultado 3:", 4 + 3 - 2 - 2)    # modifica esta
    print("Resultado 4:", 2 + 4 - 3 + 4-3)  # modifica esta
    print("Resultado 5:", 2 + 3 * 4 // 4)   # modifica esta
    print("Resultado 6:", 2 * 3 * 4 // 4)   # modifica esta
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## ✅ Lo que aprendiste en esta lección

    - Python tiene **7 operadores aritméticos**: `+` `-` `*` `/` `**` `%` `//`
    - La salida directa muestra el **último valor** de la celda
    - `print()` muestra **todos los valores** que necesites
    - `/` siempre devuelve decimal — `//` devuelve solo la parte entera
    - `%` devuelve el **residuo** de la división — útil para distribución y paridad
    - `//` y `%` trabajan en equipo

    ---
    **→ Siguiente lección: L 1.1.2 — Orden de operaciones**

    *¿Por qué `5 + 2 * 3` da `11` y no `21`? Lo vemos en la próxima lección.*
    """)
    return


@app.cell(hide_code=True)
def _():
    return


if __name__ == "__main__":
    app.run()
