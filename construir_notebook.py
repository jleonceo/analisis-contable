# -*- coding: utf-8 -*-
"""
construir_notebook.py — genera `analisis_contable.ipynb` desde cero.

POR QUE EXISTE (20/07/2026):
    El notebook original se subio el 10/05/2026 por la web de GitHub y NUNCA se
    volvio a abrir (un solo commit lo ha tocado en toda su historia). Llevaba dos
    meses publicando conclusiones falsas y ni siquiera podia ejecutarse: leia
    `libro_diario_v2`, una tabla que ya no existe.

    Un notebook que se edita a mano vuelve a quedarse rancio. Este script lo
    RECONSTRUYE, asi que regenerarlo cuesta un comando.

DATOS (14/10/2026):
    El cuaderno lee `datos/diario_2024.csv` y `datos/cierre_resultado_2024.csv`,
    exportados de la base del proyecto con solo las columnas que usa (fecha,
    asiento, cuenta, debe y haber). Asi se ejecuta en cualquier maquina, sin base
    de datos ni credenciales.

QUE ARREGLA (los 4 defectos medidos):
    G1 · signos de tesoreria invertidos (`entradas = haber(572)` cuando la 572 es
         de activo y se CARGA al entrar dinero). Publicaba "deficit estructural,
         11 de 12 meses negativos"; la realidad son 2 de 12 y +739.034,45 EUR.
    G2 · las conclusiones y "soluciones" colgadas de ese error.
    G3 · el tipo FINANCIERO restado entero como gasto: 87% era devolucion de
         PRINCIPAL (cuenta 170), que es balance, no PyG. Gasto real: 2.760 EUR.
    G4 · margen bruto sin la variacion de existencias (610).
    G10· esquema muerto -> `diario_control_financiero`, cuentas de 8 digitos.

VERIFICACION INDEPENDIENTE (la regla que fallaba):
    El resultado que calcula este notebook desde el diario OPERATIVO coincide al
    centimo con el asiento de cierre de `diario_cierre` (otra tabla, otro camino):
    592.245,36 EUR distribuidos a remanente en la apertura de 2025.

USO:  python construir_notebook.py    ->  reescribe analisis_contable.ipynb
"""
import json
import os

NB = "analisis_contable.ipynb"


def md(fuente):
    return {"cell_type": "markdown", "id": f"celda-{len(celdas)}", "metadata": {},
            "source": fuente.splitlines(True)}


def code(fuente):
    return {"cell_type": "code", "execution_count": None, "id": f"celda-{len(celdas)}",
            "metadata": {}, "outputs": [], "source": fuente.splitlines(True)}


celdas = []

celdas.append(md("""\
# Análisis financiero de TechAcces SL · ejercicio 2024

**Juan Luis León Rodríguez** · datos de una empresa ficticia, generados para el proyecto.

El cuaderno levanta la cuenta de resultados y el movimiento del banco a partir del libro
diario del ejercicio, y comprueba las dos cifras por un camino independiente: el resultado
contra el asiento de cierre, y el flujo de caja contra el saldo de la cuenta del banco.

Los datos están en `datos/`: las 4.710 líneas del libro diario de 2024 y el asiento de
cierre que distribuye el resultado. El cuaderno lo genera `construir_notebook.py`.
"""))

celdas.append(code('''\
# ============================================================
# DATOS — el libro diario del ejercicio, exportado a CSV
# ============================================================
import pandas as pd

EJERCICIO = 2024

# El diario operativo del ejercicio. Al final, el resultado se cruza contra el
# asiento de cierre, que sale de otra tabla y por otro camino.
df = pd.read_csv("datos/diario_2024.csv", dtype={"cuenta": str},
                 parse_dates=["fecha"])
df["mes"] = df["fecha"].dt.month

print(f"Ejercicio {EJERCICIO}")
print(f"  Líneas   : {len(df):,}")
print(f"  Asientos : {df['num_asiento'].nunique():,}")
print(f"  Debe     : {df['debe'].sum():,.2f} EUR")
print(f"  Haber    : {df['haber'].sum():,.2f} EUR")
print(f"  Descuadre: {df['debe'].sum() - df['haber'].sum():,.2f} EUR")
''' ))

celdas.append(md("""\
## Cuenta de resultados

Tres decisiones de clasificación que cambian el resultado:

1. **El coste de las ventas incluye la variación de existencias** (600 menos el saldo
   de la 610). Sin ella, el margen sale disparado.
2. **De la deuda solo es gasto el interés** (cuenta 662). La devolución del principal
   (cuenta 170) reduce un pasivo: es balance, no pérdida.
3. **El deterioro (694) es gasto del ejercicio**, y va después del resultado de
   explotación.
"""))

celdas.append(code('''\
# ============================================================
# CUENTA DE RESULTADOS — por naturaleza de la cuenta, no por
# el lado del asiento ni por el "tipo de operación"
# ============================================================
def saldo(prefijo, lado="debe"):
    """Suma un grupo de cuentas por su PREFIJO del PGC.

    Se agrupa por prefijo y no por `tipo_operacion` a propósito: el tipo mezcla
    partidas de naturaleza distinta dentro de un mismo asiento (FINANCIERO carga a
    la vez principal e intereses).
    """
    sel = df[df["cuenta"].astype(str).str.startswith(prefijo)]
    return float(sel[lado].sum())


ventas        = saldo("700", "haber")            # ingresos por ventas
compras       = saldo("600", "debe")             # compras de mercadería
var_existenc  = saldo("610", "haber") - saldo("610", "debe")   # + = aumentan
coste_ventas  = compras - var_existenc

margen_bruto  = ventas - coste_ventas

personal      = saldo("640", "debe") + saldo("642", "debe")    # sueldos + SS empresa
otros_gastos  = sum(saldo(str(c), "debe") for c in range(620, 630))
ebitda        = margen_bruto - personal - otros_gastos

amortizacion  = saldo("680", "debe") + saldo("681", "debe")
ebit          = ebitda - amortizacion

deterioro     = saldo("694", "debe")
gasto_finan   = saldo("662", "debe")             # SOLO intereses
principal     = saldo("170", "debe")             # devolución de deuda: NO es gasto

resultado     = ebit - deterioro - gasto_finan

pct = lambda x: f"{x / ventas * 100:5.1f}%"
print(f"  (+) Ventas                    {ventas:>14,.2f} EUR")
print(f"  (-) Coste de las ventas       {coste_ventas:>14,.2f} EUR   "
      f"(compras {compras:,.2f} - variación existencias {var_existenc:,.2f})")
print(f"  {'= MARGEN BRUTO':<29} {margen_bruto:>14,.2f} EUR   {pct(margen_bruto)}")
print(f"  (-) Personal                  {personal:>14,.2f} EUR")
print(f"  (-) Otros gastos de explot.   {otros_gastos:>14,.2f} EUR")
print(f"  {'= EBITDA':<29} {ebitda:>14,.2f} EUR   {pct(ebitda)}")
print(f"  (-) Amortizaciones            {amortizacion:>14,.2f} EUR")
print(f"  {'= EBIT':<29} {ebit:>14,.2f} EUR   {pct(ebit)}")
print(f"  (-) Deterioro de créditos     {deterioro:>14,.2f} EUR")
print(f"  (-) Gastos financieros        {gasto_finan:>14,.2f} EUR")
print(f"  {'= RESULTADO':<29} {resultado:>14,.2f} EUR   {pct(resultado)}")
print()
print(f"  Memoria: devolución de principal del préstamo = {principal:,.2f} EUR.")
print(f"  Sale de caja, pero NO es gasto: cancela deuda.")
''' ))

celdas.append(md("""\
## Verificación independiente del resultado

Comprobar una cifra contra el mismo código que la calcula no demuestra nada: si el
código calcula mal de forma coherente, la cifra cuadra igual. Aquí el resultado se
comprueba contra **otra tabla y otro camino**: el asiento de cierre que distribuye el
beneficio del ejercicio.
"""))

celdas.append(code('''\
# ============================================================
# ¿Coincide con el cierre? (verificación por vía independiente)
# ============================================================
cierre = pd.read_csv("datos/cierre_resultado_2024.csv", dtype={"cuenta": str})

ref = float(cierre["debe"].sum())
print(f"  Resultado calculado aquí (diario operativo) : {resultado:>14,.2f} EUR")
print(f"  Resultado según el asiento de cierre        : {ref:>14,.2f} EUR")
print(f"  Diferencia                                  : {resultado - ref:>14,.2f} EUR")
print()
print("  OK — dos caminos distintos, misma cifra." if abs(resultado - ref) < 0.01
      else "  AVISO: no coinciden. Antes de publicar nada, averiguar por qué.")
''' ))

celdas.append(md("""\
## Tesorería

La 572 (bancos) es una cuenta de **activo**: se **carga** cuando entra dinero y se
**abona** cuando sale. Con los signos al revés, un año de superávit parece un déficit.

La comprobación que va después de la tabla lo impide: el flujo acumulado del año tiene
que ser **igual** al saldo de la cuenta. Es una igualdad exacta, sin umbrales, y con los
signos invertidos se pondría en rojo al instante.
"""))

celdas.append(code('''\
# ============================================================
# TESORERÍA — la 572 es de ACTIVO: entra por el DEBE
# ============================================================
banco = df[df["cuenta"].astype(str).str.startswith("572")]

tes = (banco.groupby("mes")
       .agg(entradas=("debe", "sum"), salidas=("haber", "sum"))
       .reindex(range(1, 13), fill_value=0.0))
tes["flujo_neto"] = tes["entradas"] - tes["salidas"]
tes["acumulado"] = tes["flujo_neto"].cumsum()

MESES = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
tes.index = MESES

print(tes.to_string(float_format=lambda v: f"{v:>13,.2f}"))
print()
negativos = int((tes["flujo_neto"] < 0).sum())
print(f"  Flujo neto del año : {tes['flujo_neto'].sum():,.2f} EUR")
print(f"  Meses en negativo  : {negativos} de 12 "
      f"({', '.join(tes.index[tes['flujo_neto'] < 0])})")
''' ))

celdas.append(code('''\
# ============================================================
# COMPROBACIÓN DE IDENTIDAD — flujo acumulado == saldo de la cuenta
# ============================================================
# Si esto falla, hay un signo mal puesto. No es una heurística ni un umbral:
# es una igualdad contable.
flujo_acumulado = float(tes["acumulado"].iloc[-1])
saldo_cuenta = float(banco["debe"].sum() - banco["haber"].sum())
desvio = abs(flujo_acumulado - saldo_cuenta)

print(f"  Flujo acumulado a 31/12 : {flujo_acumulado:>14,.2f} EUR")
print(f"  Saldo de la 572 (D - H) : {saldo_cuenta:>14,.2f} EUR")
print(f"  Desvío                  : {desvio:>14,.2f} EUR")
print()
if desvio < 0.01:
    print("  OK — el flujo cuadra con el saldo.")
else:
    raise AssertionError(
        f"Flujo y saldo no cuadran ({desvio:,.2f} EUR). Revisar los signos "
        f"antes de interpretar nada: la 572 se carga al ENTRAR dinero.")
''' ))

celdas.append(md("""\
## Qué dicen los datos

Con los datos del ejercicio 2024 de `datos/`:

- **El ejercicio se cerró con beneficio**, no con pérdidas. Y no lo digo porque lo
  calcule esta libreta: lo confirma el asiento de cierre, que llega a la misma cifra por
  un camino distinto y desde otra tabla.
- **La tesorería creció durante el año.** Solo dos meses cerraron en negativo, enero y
  julio.
- **El margen bruto ronda el 62 %**, coherente con un comercio electrónico que compra
  mercancía.
- **La deuda no pesa en el resultado**: los intereses del año son mínimos frente a las
  ventas. La devolución del principal sale de caja, pero no es gasto.

*Las cifras exactas las imprime cada celda al ejecutarse. No se repiten aquí a propósito:
un número escrito a mano en el texto se desincroniza del dato.*

**Lo que este análisis no puede decir.** Los datos son de una empresa ficticia generada
para el proyecto: sirven para enseñar el método, no para sacar conclusiones de negocio
reales.
"""))

nb = {"cells": celdas,
      "metadata": {"kernelspec": {"display_name": "Python 3",
                                  "language": "python", "name": "python3"},
                   "language_info": {"name": "python"}},
      "nbformat": 4, "nbformat_minor": 5}

with open(NB, "w", encoding="utf-8") as fh:
    json.dump(nb, fh, ensure_ascii=False, indent=1)

print(f"OK  {NB} regenerado — {len(celdas)} celdas, sin outputs incrustados.")
print("    Se ejecuta con los CSV de datos/, sin base de datos.")
