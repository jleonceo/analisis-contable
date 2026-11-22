# Rentabilidad y márgenes

El margen bruto pasó del 75,50 % en 2025 al 42,02 % de enero a julio de 2026. En esos siete meses las compras casi
quintuplican las del mismo periodo de 2025, mientras las ventas se duplican. Los márgenes y el punto muerto se han
rehecho por SQL. La rentabilidad del capital no tiene segunda vía y por eso no va a la portada.

Datos a 31/07/2026. 2026 cubre de enero a julio.

## El margen bruto no llegó al 50 % en ningún mes de 2026

**Pregunta.** ¿Qué parte de cada euro vendido queda después de pagar la mercancía?

**Cómo se calcula.** Margen bruto = (ventas − aprovisionamientos) / ventas × 100. Los aprovisionamientos son las
compras de mercaderías (60) más la variación de existencias (61). Se calcula por año y por mes.

| Año | Margen bruto (%) | Margen de explotación (%) |
|---|---:|---:|
| 2023 | 67,13 | 47,24 |
| 2024 | 62,31 | 41,89 |
| 2025 | 75,50 | 57,68 |
| 2026, enero a julio | 42,02 | 22,23 |

Por meses, de 2023 a 2025 solo hubo cuatro por debajo del 50 %: agosto de 2023 y agosto, octubre y diciembre de 2024.
En 2026 están por debajo los siete, entre el 38,07 % de abril y el 46,57 % de febrero.

**Segunda vía.** Una consulta sobre las cuentas 60, 61 y 70 rehace el margen bruto de cada año y coincide en los
cuatro. Los aprovisionamientos de los doce meses de cada año suman lo mismo que los del año.

**Cuándo engaña.** Las existencias solo se regularizan a fin de año. Un mes con mucha compra para almacén sale con
poco margen aunque esa mercancía se venda después. Por eso el margen de un mes suelto pesa menos que el de un año.

## El margen de explotación de 2026 es menos de la mitad que el de 2025

**Pregunta.** ¿Qué parte de las ventas queda después de todos los gastos de la actividad?

**Cómo se calcula.** Margen de explotación = resultado de explotación / ventas × 100. El resultado de explotación es
el del año sin los gastos financieros (66); la empresa no tiene ingresos financieros. La tabla de arriba da sus cifras.

**Segunda vía.** Resultado más gastos financieros, dividido por las ventas, todo con consultas sobre el diario: da las
cuatro cifras de la tabla.

## En 2025 bastaba con vender 434.235,40 € para no perder

**Pregunta.** ¿Cuánto hay que vender para cubrir todos los gastos de la actividad?

**Cómo se calcula.** Punto muerto = costes fijos / (1 − costes variables / ventas). Cada gasto se clasifica como fijo
o variable:

- **variables**, los que suben con las ventas: compras, variación de existencias, transportes, servicios bancarios y
  pérdidas o provisiones por clientes que no pagan;
- **fijos**, el resto de la explotación: alquiler, reparaciones, profesionales, seguros, publicidad, suministros,
  personal y amortización.

Los gastos financieros quedan fuera: el punto muerto es de explotación.

| Año | Ventas (€) | Costes fijos (€) | Costes variables (€) | Punto muerto (€) |
|---|---:|---:|---:|---:|
| 2023 | 1.054.769,16 | 194.885,51 | 361.638,54 | 296.566,36 |
| 2024 | 1.420.269,26 | 270.442,69 | 554.821,21 | 443.818,02 |
| 2025 | 1.947.317,98 | 322.332,14 | 501.827,42 | 434.235,40 |
| 2026, enero a julio | 1.834.612,84 | 314.331,06 | 1.112.512,36 | 798.608,80 |

**Segunda vía.** Con consultas por cuenta se rehacen los costes fijos y los variables de los cuatro años con esa
clasificación. Ventas menos fijos menos variables da el resultado de cada año más sus gastos financieros. La fórmula,
aplicada a esas cifras, da los cuatro puntos muertos.

**Cuándo engaña.** La clasificación es una regla que fija la empresa. El transporte de 2026 se multiplica por
tres frente a 2025 y entra como variable. Si una parte fuera fija, el punto muerto cambiaría. El de 2026 se mide sobre
siete meses: no es lo que hay que vender en un año.

## La rentabilidad del capital se publica sin segunda vía

**Pregunta.** ¿Cuánto gana la empresa por cada euro de sus socios y de dónde sale esa rentabilidad?

**Cómo se calcula.** Con la descomposición de DuPont, la rentabilidad del capital (ROE, resultado sobre patrimonio
neto medio) es el producto de tres factores:

- **margen neto**, resultado / ventas;
- **rotación**, ventas / activo medio;
- **apalancamiento**, activo medio / patrimonio neto medio.

| Año | Margen neto (%) | Rotación (veces) | Apalancamiento (veces) | Rentabilidad del capital (%) |
|---|---:|---:|---:|---:|
| 2023 | 46,92 | 2,2128 | 1,4721 | 152,84 |
| 2024 | 41,70 | 1,1949 | 1,3743 | 68,48 |
| 2025 | 57,57 | 0,9062 | 1,3377 | 69,78 |
| 2026, enero a julio | 22,17 | 0,5887 | 1,2875 | 16,80 |

**Segunda vía.** El margen neto coincide con una consulta sobre el diario los cuatro años. El activo medio y el
patrimonio medio del cálculo no se han podido rehacer: la media de inicio y cierre de año no da las cifras de la tabla.
Por eso la rentabilidad del capital va en el detalle del cuadro de mando con su aviso y no en las cifras de arriba.

**Cuándo engaña.** La de 2026 no está anualizada: siete meses de resultado sobre un patrimonio medio. Sobre el
patrimonio al cierre, en lugar del medio, la de 2025 sería del 48,60 %.

## Las compras de enero a julio de 2026 casi quintuplican las del mismo periodo de 2025

**Pregunta.** ¿Qué cuentas han cambiado más frente al año anterior?

**Cómo se calcula.** Para cada cuenta se compara su movimiento del 1 de enero al corte con el mismo tramo del año
anterior. Variación = actual − anterior, en el sentido de la naturaleza de la cuenta. Se publica una lista por importe
de la variación.

La de más peso son las compras de mercaderías: 1.063.649,33 € de enero a julio de 2026 frente a 215.559,88 € en el mismo
tramo de 2025. Son 848.089,45 € más, un 393,44 %. Las ventas del mismo tramo pasan de 856.302,45 € a 1.834.612,84 €.

**Segunda vía.** Una consulta sobre la cuenta de compras en los dos tramos da las tres cifras al céntimo.

**Cuándo engaña.** El tramo del año en curso compara bien con el del año pasado solo si los dos se graban al mismo
ritmo. La lista enseña lo que cambió. El motivo no está en el diario.

Ficheros: `datos/d_margenes.csv`, `datos/d_margen_bruto_mensual.csv`, `datos/d_punto_muerto.csv`,
`datos/d_rentabilidad.csv` y `datos/c_variaciones.csv`.
