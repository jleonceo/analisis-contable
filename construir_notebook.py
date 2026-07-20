# -*- coding: utf-8 -*-
"""
construir_notebook.py — genera `analisis_contable.ipynb` desde cero.

POR QUE EXISTE (20/07/2026):
    El notebook original se subio el 10/05/2026 por la web de GitHub y NUNCA se
    volvio a abrir (un solo commit lo ha tocado en toda su historia). Llevaba dos
    meses publicando conclusiones falsas y ni siquiera podia ejecutarse: leia
    `libro_diario_v2`, una tabla que ya no existe.

    Un notebook que se edita a mano vuelve a quedarse rancio. Este script lo
    RECONSTRUYE desde la base viva, asi que regenerarlo cuesta un comando y las
    cifras no pueden desincronizarse del dato.

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
    return {"cell_type": "markdown", "metadata": {}, "source": fuente.splitlines(True)}


def code(fuente):
    return {"cell_type": "code", "execution_count": None, "metadata": {},
            "outputs": [], "source": fuente.splitlines(True)}


celdas = []

celdas.append(md("""\
# Análisis financiero de TechAcces SL — ejercicio 2024

**Juan Luis León Rodríguez** · datos de una empresa ficticia, generados para el proyecto.

---

## Aviso: este cuaderno se reescribió el 20/07/2026, y por qué

La primera versión se publicó el 10 de mayo y **concluía lo contrario de lo que decían
sus propios datos**: que la empresa perdía dinero y arrastraba un déficit estructural de
tesorería. Con los mismos datos y la clasificación contable correcta, el ejercicio daba
beneficio y el banco crecía.

**Dos cosas distintas, y conviene no mezclarlas.** Una es que el método estaba mal —eso
es lo que se corrige aquí—. La otra es que **los datos ya no son los mismos**: la tabla
que leía (`libro_diario_v2`) se retiró y la base viva tiene otro contenido para 2024
(4.710 líneas frente a 4.006, 1.420.269 € de ventas frente a 753.263 €). Así que las
cifras de este cuaderno **no son "la versión corregida" de las de mayo**: son otro
cálculo sobre otros datos. Comparar unas con otras sería comparar cosas distintas, que
es justo uno de los errores que esto viene a arreglar.

Los tres errores de método, todos reales:

| | qué hacía mal | por qué importa |
|---|---|---|
| **Tesorería** | Tomaba las entradas del **haber** de la 572 y las salidas del **debe**. Está al revés: la 572 es de activo, se **carga** cuando entra dinero. | De ahí salía *"flujo negativo 11 de los 12 meses"*, y encima cuatro causas inventadas para explicarlo. Con los signos bien, el año era de superávit. |
| **Resultado** | Restaba el tipo `FINANCIERO` entero como gasto. La mayor parte es **devolución de principal** (cuenta 170), que cancela deuda: es balance, no pérdida. | Convertía un ejercicio con beneficio en *"−57.742 €"*, y de ahí colgaba todo el relato de "refinanciar el ICO". |
| **Margen bruto** | Calculaba el coste de ventas solo con la 600, ignorando la variación de existencias (610). | Daba un *"91,7 %"* de margen. Un 8 % de coste de producto en un comercio electrónico es imposible, y nadie lo miró. |

Y había un cuarto problema que lo explica todo: **el cuaderno llevaba dos meses sin
poder ejecutarse**. Leía una tabla (`libro_diario_v2`) que se había borrado, así que
sus resultados estaban congelados dentro del fichero. Un solo *commit* lo tocó en toda
su historia.

**Lo que cambia en la forma de trabajar**, más allá de los números: este cuaderno ya no
se edita a mano, lo **genera** `construir_notebook.py` desde la base viva. Y lleva
dentro una comprobación que habría cazado el error del signo el primer día —está en la
sección de tesorería—.
"""))

celdas.append(code('''\
# ============================================================
# CONEXIÓN — credenciales desde .env, nunca en el código
# ============================================================
import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

engine = create_engine(
    "mysql+pymysql://{u}:{p}@{h}:{P}/{d}".format(
        u=os.getenv("DB_USER"), p=os.getenv("DB_PASS"),
        h=os.getenv("DB_HOST"), P=os.getenv("DB_PORT"), d=os.getenv("DB_NAME"))
)

EJERCICIO = 2024

# El diario OPERATIVO. Ojo: hay tres tablas de hechos en este esquema
# (operativo, cierre y borrador). Aquí se analiza el operativo, y al final
# se cruza el resultado contra el de cierre — que es otra tabla y otro camino.
df = pd.read_sql(
    text("SELECT * FROM diario_control_financiero WHERE YEAR(fecha) = :ej"),
    engine, params={"ej": EJERCICIO})
df["fecha"] = pd.to_datetime(df["fecha"])
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

Tres decisiones de clasificación que la primera versión se saltó, y son las que
cambian el signo del resultado:

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
    partidas de naturaleza distinta dentro de un mismo asiento (el caso que rompió
    la versión anterior: FINANCIERO carga a la vez principal e intereses).
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
print(f"  Sale de caja, pero NO es gasto: cancela deuda. La versión anterior lo")
print(f"  restaba del resultado y de ahí salían las 'pérdidas'.")
''' ))

celdas.append(md("""\
## Verificación independiente del resultado

La regla que falló en la primera versión era *"comprobar cada cifra contra su fuente"*,
y es circular: si el código calcula mal de forma coherente, la cifra **cuadra con su
fuente** y el error pasa. Aquí el resultado se comprueba contra **otra tabla y otro
camino**: el asiento de cierre que distribuye el beneficio del ejercicio.
"""))

celdas.append(code('''\
# ============================================================
# ¿Coincide con el cierre? (verificación por vía independiente)
# ============================================================
cierre = pd.read_sql(
    text("SELECT cuenta, debe, haber, concepto FROM diario_cierre "
         "WHERE concepto LIKE :c"),
    engine, params={"c": "%%resultado 2024%%"})

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

Aquí estaba el error que lo estropeó todo. La 572 (bancos) es una cuenta de **activo**:
se **carga** cuando entra dinero y se **abona** cuando sale. La primera versión lo puso
al revés, y con eso convirtió un año de superávit en un "déficit estructural" — y luego
inventó cuatro causas para explicar un problema que no existía.

La comprobación que va después de la tabla es la que lo habría cazado el primer día:
el flujo acumulado del año tiene que ser **igual** al saldo de la cuenta. Es una
igualdad exacta, sin umbrales ni criterio. Con los signos invertidos daba
`−739.034,45 ≠ +739.034,45` y se habría puesto en rojo al instante.
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
# es una igualdad contable. Fue lo que faltó durante dos meses.
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

Con los datos vivos a 20/07/2026:

- **El ejercicio se cerró con beneficio**, no con pérdidas. Y no lo digo porque lo
  calcule esta libreta: lo confirma el asiento de cierre, que llega a la misma cifra por
  un camino distinto y desde otra tabla.
- **La tesorería creció durante el año.** Solo dos meses cerraron en negativo, enero y
  julio, los dos por pagos concentrados. No hay un problema de fondo que explicar.
- **El margen bruto ronda el 62 %**, coherente con un comercio electrónico que compra
  mercancía. El 91,7 % de la primera versión salía de olvidar su coste.
- **La deuda no es el problema**: los intereses del año son calderilla frente a las
  ventas. Lo que parecía un agujero era la amortización del principal, que no es gasto.

*Las cifras exactas las imprime cada celda al ejecutarse. No se repiten aquí a propósito:
un número escrito a mano en el texto se desincroniza del dato en cuanto la base cambia —
que es, literalmente, parte de lo que le pasó a la versión anterior.*

**Lo que este análisis no puede decir.** Los datos son de una empresa ficticia generada
para el proyecto: sirven para enseñar el método, no para sacar conclusiones de negocio
reales. Y las cifras se mueven, porque la base sigue viva — para reproducirlas, hay que
regenerar el cuaderno.
"""))

nb = {"cells": celdas,
      "metadata": {"kernelspec": {"display_name": "Python 3",
                                  "language": "python", "name": "python3"},
                   "language_info": {"name": "python"}},
      "nbformat": 4, "nbformat_minor": 5}

with open(NB, "w", encoding="utf-8") as fh:
    json.dump(nb, fh, ensure_ascii=False, indent=1)

print(f"OK  {NB} regenerado — {len(celdas)} celdas, sin outputs incrustados.")
print("    Ejecutarlo requiere el .env y la base viva.")
