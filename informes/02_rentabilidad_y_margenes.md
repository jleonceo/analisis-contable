# Rentabilidad y márgenes

De enero a julio de 2026 el margen bruto fue del 42,02 % y el de explotación, del 22,23 %. Ningún mes llegó al 50 % de
margen bruto. Los márgenes y el punto muerto se han rehecho por SQL. La rentabilidad del capital no tiene segunda vía y
por eso no va a la portada.

Datos a 31/07/2026. Se publica solo el ejercicio 2026, de enero a julio. Los años anteriores salen de un dato generado
en el que las compras no siguen a las ventas. Por eso sus márgenes no son los de una pyme real.

## El margen bruto no llegó al 50 % en ningún mes de 2026

**Pregunta.** ¿Qué parte de cada euro vendido queda después de pagar la mercancía?

**Cómo se calcula.** Margen bruto = (ventas − aprovisionamientos) / ventas × 100. Los aprovisionamientos son las
compras de mercaderías (60) más la variación de existencias (61). Se calcula para el periodo y para cada mes.

| Periodo | Margen bruto (%) | Margen de explotación (%) |
|---|---:|---:|
| 2026, enero a julio | 42,02 | 22,23 |

Por meses, va del 38,07 % de abril al 46,57 % de febrero. Las ventas de junio y de julio son casi cinco veces las de
mayo, pero el margen de esos meses se queda en la misma franja.

**Segunda vía.** Una consulta sobre las cuentas 60, 61 y 70 rehace el margen bruto del periodo y coincide. Los
aprovisionamientos de los siete meses suman lo mismo que los del periodo.

**Cuándo engaña.** Las existencias solo se regularizan a fin de año. Un mes con mucha compra para almacén sale con
poco margen aunque esa mercancía se venda después. Por eso el margen de un mes suelto pesa menos que el del periodo.

## El margen de explotación se queda en el 22,23 %

**Pregunta.** ¿Qué parte de las ventas queda después de todos los gastos de la actividad?

**Cómo se calcula.** Margen de explotación = resultado de explotación / ventas × 100. El resultado de explotación es
el del periodo sin los gastos financieros (66); la empresa no tiene ingresos financieros.

**Segunda vía.** Resultado más gastos financieros, dividido por las ventas, todo con consultas sobre el diario: da la
cifra de la tabla.

## El punto muerto de los siete meses es de 798.608,80 €

**Pregunta.** ¿Cuánto hay que vender para cubrir todos los gastos de la actividad?

**Cómo se calcula.** Punto muerto = costes fijos / (1 − costes variables / ventas). Cada gasto se clasifica como fijo
o variable:

- **variables**, los que suben con las ventas: compras, variación de existencias, transportes, servicios bancarios y
  pérdidas o provisiones por clientes que no pagan;
- **fijos**, el resto de la explotación: alquiler, reparaciones, profesionales, seguros, publicidad, suministros,
  personal y amortización.

Los gastos financieros quedan fuera: el punto muerto es de explotación.

| Periodo | Ventas (€) | Costes fijos (€) | Costes variables (€) | Punto muerto (€) |
|---|---:|---:|---:|---:|
| 2026, enero a julio | 1.834.612,84 | 314.331,06 | 1.112.512,36 | 798.608,80 |

**Segunda vía.** Con consultas por cuenta se rehacen los costes fijos y los variables con esa clasificación. Ventas
menos fijos menos variables da el resultado del periodo más sus gastos financieros. La fórmula, aplicada a esas cifras,
da el punto muerto.

**Cuándo engaña.** La clasificación es una regla que fija la empresa. Si una parte del transporte fuera fija, el punto
muerto cambiaría. Se mide sobre siete meses: no es lo que hay que vender en un año.

## La rentabilidad del capital se publica sin segunda vía

**Pregunta.** ¿Cuánto gana la empresa por cada euro de sus socios y de dónde sale esa rentabilidad?

**Cómo se calcula.** Con la descomposición de DuPont, la rentabilidad del capital (ROE, resultado sobre patrimonio
neto medio) es el producto de tres factores:

- **margen neto**, resultado / ventas;
- **rotación**, ventas / activo medio;
- **apalancamiento**, activo medio / patrimonio neto medio.

| Periodo | Margen neto (%) | Rotación (veces) | Apalancamiento (veces) | Rentabilidad del capital (%) |
|---|---:|---:|---:|---:|
| 2026, enero a julio | 22,17 | 0,5887 | 1,2875 | 16,80 |

**Segunda vía.** El margen neto coincide con una consulta sobre el diario. El activo medio y el patrimonio medio del
cálculo no se han podido rehacer. Por eso la rentabilidad del capital va en el detalle del cuadro de mando con su aviso
y no en las cifras de arriba.

**Cuándo engaña.** No está anualizada: son siete meses de resultado sobre un patrimonio medio.

Ficheros: `datos/d_margenes.csv`, `datos/d_margen_bruto_mensual.csv`, `datos/d_punto_muerto.csv` y
`datos/d_rentabilidad.csv`.
