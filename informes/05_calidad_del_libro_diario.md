# Calidad del libro diario

El diario cuadra al céntimo y ninguna comprobación de estructura encuentra nada. Siete comprobaciones dan aviso: piden
que una persona mire una lista concreta de apuntes, cuentas o meses. Cada cifra de este informe se ha rehecho por SQL
y coincide.

Datos a 31/07/2026. Son 6.399 asientos de enero de 2023 a julio de 2026.

## Lo que está en orden

| Qué se comprueba | Cómo | Resultado |
|---|---|---|
| ¿Cuadra todo? | debe menos haber, por asiento y en total, sin tolerancia | 0 asientos descuadrados; 22.029.536,94 € al debe y al haber |
| ¿Las vistas dicen lo mismo que la tabla? | la vista de cuadre y la de sumas y saldos contra la tabla del diario, cuenta a cuenta y asiento a asiento | 0 diferencias |
| ¿Aparece un centro de coste que no existe? | los centros del diario contra la lista de cuatro centros de la empresa | 0 valores fuera de la lista |
| ¿Cada cuenta está en el plan? | las cuentas del diario y de los asientos de cierre contra el plan de cuentas | 0 cuentas fuera del plan |
| ¿Se carga una cuenta de agrupación? | apuntes en una cuenta de la que cuelgan otras del plan | 0 apuntes |
| ¿Hay un asiento a punto de entrar en un mes cerrado? | las 19 líneas de borrador, 6 pendientes y 13 ya promovidas, contra los 36 meses cerrados | 0 líneas en un mes cerrado |
| ¿Hay fechas imposibles? | fecha posterior al corte, vencimiento anterior a la fecha, cobro anterior a la factura | 0 líneas |
| ¿Hay una combinación de cuentas nueva? | la primera fecha de cada par de cuenta al debe y cuenta al haber | 185 pares; ninguno nuevo en julio de 2026 |

**Segunda vía.** Cada fila se ha rehecho con una consulta directa sobre las tablas del diario, del plan y de los
periodos. Todas dan lo mismo.

**Cuándo engaña.** Que el diario cuadre no dice que cada importe esté en su cuenta. Un apunte a la cuenta equivocada,
con su contrapartida bien, cuadra igual. La comprobación de las vistas solo mira esas dos.

## 2.273 números de asiento sin usar

**Pregunta.** ¿Faltan números de asiento o se repite alguno con dos fechas?

**Cómo se calcula.** Del primer número de asiento al último, se cuentan los que no aparecen. Aparte, los números con más
de una fecha.

La numeración va del 1 al 8.672 con 6.399 números usados. Ninguno tiene dos fechas.

**Segunda vía.** Una consulta del primero, el último y los números distintos da los mismos 2.273 huecos.

**Cuándo engaña.** Un hueco no prueba un asiento borrado: muchos programas reservan números que después no usan. Lo útil
es mirar si aparecen huecos nuevos de un mes a otro.

## 27 veces un campo analítico se vació de golpe en un mes

**Pregunta.** ¿Qué parte del diario trae los campos que usa el análisis y en qué mes cae de golpe?

**Cómo se calcula.** Para siete series se mide, mes a mes, el porcentaje de líneas con el campo relleno:

- en los gastos y los ingresos, el centro de coste, la línea de negocio, el canal y la categoría de producto;
- en las facturas de clientes y de proveedores, el vencimiento;
- en clientes, proveedores y acreedores, la referencia del documento.

Hay aviso cuando una serie cae más de 5 puntos frente al mes anterior.

**Segunda vía.** Las siete series rehechas por SQL, comparando cada mes con el anterior, dan las mismas 27 caídas.

**Cuándo engaña.** Un mes con pocas líneas cambia mucho de porcentaje con una sola línea vacía. El aviso solo mide caídas.
Un campo que siempre llega medio vacío no avisa.

## Once cuentas con saldo llevan seis meses sin moverse

**Pregunta.** ¿Qué cuentas tienen saldo pero no se han movido en los últimos seis meses?

**Cómo se calcula.** Una cuenta está dormida si tiene saldo al corte y su último apunte, sin contar aperturas ni
cierres, es anterior al 31/01/2026. El saldo se mide con los asientos de cierre incluidos.

**Segunda vía.** Una consulta sobre el saldo de cada cuenta y su último apunte da las mismas once.

**Cuándo engaña.** El capital, las reservas y el remanente solo se mueven con el cierre: salen dormidas por naturaleza.
Las existencias solo se regularizan a fin de año, así que a mitad de año también salen.

## Diez cuentas se han usado tres veces o menos

**Pregunta.** ¿Hay cuentas que casi nunca se usan?

**Cómo se calcula.** Cuentas con tres apuntes o menos en toda la historia del diario, sin contar aperturas ni cierres.

**Segunda vía.** Un recuento de apuntes por cuenta da las mismas diez.

**Cuándo engaña.** Un gasto anual, como un seguro, tiene pocos apuntes por naturaleza. El aviso sirve para mirar si ese
apunte suelto es una cuenta mal tecleada.

## Nueve cuentas tuvieron el saldo al revés algún mes y seis lo tienen al corte

**Pregunta.** ¿Hay cuentas con el saldo del signo que no les toca?

**Cómo se calcula.** Se compara el saldo de cada fin de mes con la naturaleza de la cuenta en el plan, deudora o
acreedora. Se marca cuando va al revés por más de 1.000 €. Quedan fuera el resultado del ejercicio y los grupos 6 y 7,
que pueden tener los dos signos.

**Segunda vía.** Una consulta con el saldo acumulado de cada cuenta mes a mes da las mismas nueve y seis.

**Cuándo engaña.** Un saldo al revés un solo mes puede ser legítimo: un cobro que llega antes que su factura. Importa el
que dura. Las cinco cuentas de cliente con saldo a su favor al corte están en esta lista (ver
[Clientes y proveedores](04_clientes_y_proveedores.md)).

## 70 apuntes en 20 cuentas se salen de lo habitual para su cuenta

**Pregunta.** ¿Hay un apunte muy fuera de lo habitual para su cuenta?

**Cómo se calcula.** Los apuntes se agrupan por cuenta, tipo de operación, canal y lado del asiento. Dentro de cada
grupo de al menos 10 apuntes se mide la puntuación z robusta del logaritmo de 1 más el importe: 0,6745 × (valor − su
mediana) / desviación absoluta mediana. Se marca el apunte con z por encima de 3,5 y de al menos 1.000 €, solo hacia
arriba.

**Segunda vía.** Una consulta con las medianas calculadas por grupo da los mismos 70 apuntes en las mismas 20 cuentas.
Con el logaritmo del importe, sin sumar 1, salen 68: dos apuntes están justo en el umbral. El manual de los análisis
dice «logaritmo del importe» y el cálculo publicado usa el de 1 más el importe.

**Cuándo engaña.** Una operación grande y legítima, como una compra de inmovilizado, sale siempre.

## 11 tipos de asiento solo aparecen una o dos veces

**Pregunta.** ¿Qué tipos de asiento hay y cuáles no se parecen a ninguno?

**Cómo se calcula.** El tipo de un asiento es el conjunto de sus cuentas, a tres dígitos, con su lado: una venta a
crédito es «cliente al debe, IVA repercutido y ventas al haber». Un tipo es raro si aparece en dos asientos o menos. Se
cuentan los asientos del diario sin el de apertura de 2023.

Hay 40 tipos. Los diez más usados reúnen el 91,89 % de los asientos.

**Segunda vía.** Una consulta que forma el tipo de cada asiento y cuenta sus asientos da los 40 tipos, los 11 raros y el mismo
porcentaje.

**Cuándo engaña.** Un tipo raro puede ser una operación legítima que ocurre poco, como una compra de inmovilizado.

## Lo que se mira en otros informes

- **Las 17 facturas fuera de lo normal para su tercero** están en [Clientes y proveedores](04_clientes_y_proveedores.md).
- **La reserva legal sin dotar, el cierre, el IVA soportado y la nómina** están en [Fiscal y cierre](06_fiscal_y_cierre.md).

Fichero: `datos/o_comprobaciones.csv`, con las 20 comprobaciones, su estado y lo que encuentra cada una.
