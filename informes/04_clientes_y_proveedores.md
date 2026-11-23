# Clientes y proveedores

Nueve de los diecinueve clientes con límite de crédito deben más de ese límite. Cuatro tardan de media en pagar más de quince días por
encima de lo pactado. La cartera no depende de un solo cliente: el primero reúne el 10,91 % de lo facturado. Cada cifra
de este informe se ha rehecho por SQL, también las dos que salen de una prueba estadística.

Datos a 31/07/2026. Los clientes y los proveedores van por su código de cuenta.

## Los cinco primeros clientes reúnen el 41,20 % de lo facturado

**Pregunta.** ¿Cuánto depende la empresa de unos pocos clientes?

**Cómo se calcula.** Se suma lo facturado a cada cuenta de cliente en los doce meses hasta el corte, de agosto de 2025
a julio de 2026, con IVA. La cuota de cada cliente es su importe sobre el total; el acumulado va de mayor a menor.

| Puesto | Cuota (%) | Acumulado (%) |
|---|---:|---:|
| 1 | 10,91 | 10,91 |
| 2 | 8,96 | 19,86 |
| 3 | 7,55 | 27,41 |
| 4 | 6,92 | 34,34 |
| 5 | 6,86 | 41,20 |

Son 18 clientes y 2.223.141,27 € facturados.

**Segunda vía.** Una consulta que suma el debe de cada cuenta de cliente en esos doce meses da el total y las cinco
cuotas.

**Cuándo engaña.** La venta a particulares de esos meses se cobra en el momento y va directa al banco, sin pasar por
una cuenta de cliente. Estas cuotas miden la dependencia dentro de la venta a empresas, no sobre todas las ventas.

## Cuatro clientes pagan de media más de quince días por encima de lo pactado

**Pregunta.** ¿Cuánto tarda cada cliente en pagar, frente a lo que tiene pactado?

**Cómo se calcula.** Cada cobro se casa con su factura por la referencia del documento. Los días de cada factura van de
su fecha a la del último cobro que la cancela. Por cliente se calculan la media y la mediana de esos días. Un cliente
paga tarde si su media pasa de lo pactado en más de 15 días.

| Cliente | Días pactados | Media real (días) | Mediana real (días) | Facturas cobradas |
|---|---:|---:|---:|---:|
| 43000003 | 60 | 85,72 | 87 | 232 |
| 43000005 | 60 | 86,96 | 87 | 190 |
| 43000004 | 45 | 65,08 | 66 | 179 |
| 43000006 | 45 | 64,07 | 65 | 162 |

Con la mediana, que es lo que enseña el cuadro de mando, salen dos más. El 43000002 tarda 86 días sobre 60 pactados;
el 43000014, 46 sobre 30. El 43000002 cobra 23 facturas en 6 días y el resto a más de 80, así que su media se queda en
70,55. Los otros doce clientes pagan después de lo pactado, sin llegar al margen de 15 días por ninguna de las dos
medidas. Los de 30 días pagan
con una mediana de 44 a 46 días; los de 15 días, con una de 22,5 a 25,5.

**Segunda vía.** El casado por referencia, hecho con una consulta, da las mismas facturas cobradas, la misma media y la
misma mediana en los 18 clientes. Los días pactados coinciden con la ficha de cada cliente.

**Cuándo engaña.** El manual de los análisis describe la media ponderada por lo cobrado. Lo publicado es la media
simple por factura y la mediana. El cuadro de mando enseña la mediana, que no la mueve una factura que tarde mucho.

## Nueve clientes deben más de su límite de crédito

**Pregunta.** ¿Qué clientes deben más de lo que la empresa está dispuesta a fiarles?

**Cómo se calcula.** Uso del límite = saldo de la cuenta del cliente al corte / límite de crédito de su ficha × 100.
Pasa del límite el que supera el 100 %. Un cliente con saldo a su favor no usa el límite.

| Cliente | Saldo (€) | Límite (€) | Uso del límite (%) |
|---|---:|---:|---:|
| 43000019 | 15.587,34 | 3.000,00 | 519,58 |
| 43000009 | 63.265,32 | 15.000,00 | 421,77 |
| 43000014 | 55.211,37 | 18.000,00 | 306,73 |
| 43000008 | 55.366,68 | 20.000,00 | 276,83 |
| 43000010 | 49.301,42 | 18.000,00 | 273,90 |
| 43000015 | 30.729,62 | 12.000,00 | 256,08 |
| 43000013 | 35.589,91 | 14.000,00 | 254,21 |
| 43000004 | 46.984,10 | 45.000,00 | 104,41 |
| 43000003 | 62.067,68 | 60.000,00 | 103,45 |

**Segunda vía.** El saldo de cada cuenta de cliente al corte, sacado del diario, con el límite de su ficha da los nueve
usos al céntimo.

**Cuándo engaña.** Cinco clientes tienen saldo a su favor al corte, entre 6.596,16 € y 60.977,77 €: han pagado más de
lo facturado. Su uso queda en blanco. Las dos cuentas de venta a particulares no tienen límite útil: una sin límite y
otra con límite cero. El análisis no las juzga.

## Dos cuentas de clientes no compran desde 2024

**Pregunta.** ¿Qué cliente ha dejado de comprar?

**Cómo se calcula.** Para cada cliente con al menos tres compras, su ciclo es la mediana de los días entre compras
seguidas. Ha dejado de comprar si lleva sin comprar más del doble de su ciclo.

Las dos que salen son las cuentas de venta a particulares, que solo se usaron en 2024. La última factura de una es del
31/12/2024 y la de la otra, del 07/12/2024. La venta a particulares solo pasó por cuenta de cliente en 2024; en 2023 y
desde 2025 se cobra sin ella.

**Segunda vía.** Una consulta sobre esas dos cuentas da sus 34 y 14 facturas, todas de 2024, con 577 y 601 días sin
comprar al corte.

**Cuándo engaña.** Aquí no avisa de un cliente perdido. Avisa de un cambio en la forma de contabilizar.

## Cuatro acreedores se apartaron más de un 30 % de su importe habitual en 41 meses

**Pregunta.** ¿Hay facturas de gasto recurrente que se apartan de su importe habitual?

**Cómo se calcula.** Siete acreedores de gasto recurrente (alquiler, profesionales, transporte, publicidad, suministros
y seguros) tienen un importe mensual habitual en su ficha. Se suma la base de lo que factura cada mes. Ese mes se aparta si la base pasa en más de un 30 % de lo
habitual, por arriba o por abajo.

Se aparta en 41 de los 133 meses con factura de un acreedor con importe habitual: 19 al alza y 22 a la baja. Los 41 son
de 2023 y 2024, repartidos entre cuatro acreedores.

**Segunda vía.** Una consulta que suma el gasto de los asientos de cada acreedor por mes y lo compara con el habitual
de su ficha da los 133 meses y los 41 que se apartan.

**Cuándo engaña.** El habitual es uno solo para todo el periodo. Una subida de precio pactada sale como desviación todos
los meses siguientes hasta que se actualiza la ficha.

## 17 facturas se salen de lo normal para su cliente o su proveedor

**Pregunta.** ¿Hay una factura mucho más alta de lo que suele facturar ese tercero?

**Cómo se calcula.** Dentro de cada cliente, proveedor o acreedor con al menos 10 facturas se mide la puntuación z
robusta del logaritmo del importe: 0,6745 × (logaritmo del importe − su mediana) / desviación absoluta mediana. Se marca
la factura con z por encima de 3,5 y de al menos 1.000 €. Solo cuenta hacia arriba.

**Segunda vía.** Una consulta con las medianas calculadas por tercero da las mismas 17 facturas.

**Cuándo engaña.** Una operación grande y legítima, como un pedido excepcional, sale siempre. Un tercero que factura casi
siempre lo mismo tiene una desviación pequeña: cualquier factura algo mayor salta.

Ficheros: `datos/d_concentracion_clientes.csv`, `datos/c_clientes.csv` y `datos/c_facturas_disparadas.csv`. Las 17
facturas atípicas van como recuento en `datos/o_comprobaciones.csv`.
