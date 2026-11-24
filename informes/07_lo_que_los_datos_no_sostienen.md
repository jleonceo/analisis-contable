# Lo que los datos no sostienen

Una revisión externa del repositorio señaló 16 defectos. Este informe mide cada uno con el mismo libro diario y dice
cuánto mueve las cifras publicadas y qué haría falta para corregirlo. Catorce se confirman y dos se corrigen en parte.
Los que más pesan son cuatro. Junio y julio aportan el 79,20 % del resultado con un volumen que no encaja con el resto
del año. Falta el Impuesto sobre Sociedades, que restaría unos 93.500 € al resultado de los siete meses. El puente del
presupuesto atribuía la desviación a las partidas equivocadas. Las existencias no se recuentan a mitad de año.

La versión 3.0 corrige tres puntos en el propio repositorio. El puente del presupuesto compara ahora cada cuenta con su
presupuesto. Power BI da el margen en puntos. Además, tiene un modelo con tabla de hechos y tabla de fechas. Las
secciones de esos puntos cuentan lo que se midió y lo que cambió.

Datos a 31/07/2026. Cada cifra de este informe se ha obtenido con una consulta SQL sobre el diario, distinta del
programa que genera los cuadros de mando.

## Lo que cambia las cifras de la portada

### Junio y julio concentran casi todo el resultado del periodo

De enero a mayo, la empresa vendió entre 91.218,81 € y 133.729,50 € al mes. En junio facturó 612.580,14 € y en julio
643.755,30 €. Esos dos meses suman el 68,48 % de las ventas y el 79,20 % del resultado de los siete meses.

Los asientos de junio y julio, 1.070 en total, los registró un proceso de carga distinto del que generó los de enero a
mayo. Los informes de [rentabilidad](02_rentabilidad_y_margenes.md) y de
[presupuesto](03_presupuesto_objetivos_y_centros.md) mencionan el salto, pero no lo explican.

No hay clientes nuevos. Los 18 que facturan en junio y julio ya lo hacían antes. Lo que cambia es el
tamaño de cada venta. El mayor cliente del mes no pasaba de 15.035,01 € hasta mayo y en junio llega a 76.843,88 €.
También sube la publicidad, de menos de 900 € al mes a 15.768,42 € en junio y 17.962,60 € en julio. La plantilla y el
coste de personal, en cambio, no se mueven.

Sin esos dos meses, el periodo de enero a mayo deja 578.277,40 € de ventas y 84.589,19 € de resultado. Un controller
presentaría las dos lecturas y no daría por bueno el resultado de siete meses hasta revisar la carga de junio y julio.

### El presupuesto se desvía por las partidas sin presupuesto

El resultado real se quedó 70.085,60 € por debajo del presupuestado. Hasta la versión 2.1, el puente del cuadro del
controller comparaba cada cuenta dentro de su centro de coste. Así presentaba tres partidas como ahorro, por
100.479,60 € entre las tres: transportes, publicidad y arrendamientos. Tenían presupuesto en un centro. La mayor parte
de su gasto, 98.915,75 €, se apuntó en otro. El puente la llevaba a «partidas sin presupuesto».

Comparada cada cuenta con su presupuesto sin separar por centro, la lectura cambia:

- transportes: 815,28 € por debajo de lo presupuestado;
- publicidad: 748,57 € por debajo;
- arrendamientos: exactamente lo presupuestado;
- **gastos que no tenían presupuesto:** 73.690,68 €, sobre todo servicios profesionales (28.760,35 €) y seguros
  (37.368,19 €), además de amortizaciones, intereses y otros menores.

La desviación del resultado se explica casi entera por ese último grupo. Para la dirección, la lectura es que
el presupuesto se quedó corto porque no recogía esos gastos. Las tres partidas solo tienen un problema de imputación
a centros, que no cambia el resultado. Desde la versión 3.0, el puente compara cada cuenta con su presupuesto sumando
todos sus centros y enseña esta lectura.

### Falta el Impuesto sobre Sociedades

Ni en los tres ejercicios cerrados ni en 2026 tiene el diario un solo apunte de gasto por impuesto sobre beneficios
(cuenta 630) o de deuda con Hacienda por ese impuesto (cuenta 4752), de modo que nunca se ha registrado. El resultado publicado es, por tanto, un resultado
antes de impuestos, aunque los informes lo llamen resultado.

Con la cifra de negocios del año anterior entre 1 y 10 millones de euros, la empresa es de reducida dimensión y en
2026 tributa al 23 %, según la [Agencia Tributaria](https://sede.agenciatributaria.gob.es/Sede/impuesto-sobre-sociedades/que-base-imponible-se-determina-sociedades/tipo-impositivo.html)
(consultada el 24/11/2026). Si la base imponible coincidiera con el resultado contable, el gasto devengado de enero a
julio sería de 93.542,67 € y el resultado después de impuestos, de 313.164,61 €. La base real no se puede saber con el
diario: depende de ajustes fiscales que no están contabilizados.

Un profesional registraría cada mes la provisión del impuesto estimado. Al cierre, el gasto definitivo.

### Las existencias no se recuentan a mitad de año

Las existencias solo se tocan el 31 de diciembre. A 31/07/2026, el almacén sigue valorado en
96.000,00 €, la cifra del cierre de 2025. El margen bruto del 42,02 % supone, por tanto, que el stock no ha cambiado
en siete meses.

El stock real a 31 de julio no se puede saber con el diario. Lo que sí se puede decir es cuánto pesa: cada 10.000 € de
diferencia en el stock mueve el margen bruto de los siete meses en 0,55 puntos. Un cierre intermedio estimaría las
existencias con un recuento o con el margen habitual sobre las ventas.

## Lo que está mal contabilizado pero no cambia el resultado

### Cinco clientes tienen saldo a su favor

A 31/07/2026, cinco cuentas de clientes tienen saldo acreedor por 111.813,95 € en total; la mayor, 60.977,77 €. Un
cliente con saldo a su favor ha pagado más de lo que se le ha facturado. Es un anticipo. En el balance va al pasivo, en
anticipos de clientes (cuenta 438), una cuenta que el diario no usa nunca.

Mientras sigan en clientes, el saldo de clientes sale menor de lo que la empresa tiene por cobrar. Los otros trece clientes con
saldo deben 474.744,74 €: esa es la cifra que hay que gestionar. La corrección es un asiento de reclasificación al
cierre de cada periodo.

### Las aperturas de 2025 y 2026 llevan la fecha del día anterior

El asiento de apertura de 2024 tiene fecha del 1 de enero. Los de 2025 y 2026 tienen fecha del 31 de diciembre del año
anterior, la misma que el cierre. El informe de [fiscal y cierre](06_fiscal_y_cierre.md) lo cita como nota. Cada
apertura traspasa el resultado del año anterior a remanente. Con esa fecha, un balance a 31 de diciembre de 2024 o de
2025 enseña el beneficio del año ya llevado a remanente, como si la junta lo hubiera aplicado ese mismo día. La
corrección es cambiar la fecha de esos dos asientos al 1 de enero.

## Lo que está mal medido en el control de gestión

### El semáforo de julio no tiene en cuenta que se vendió más

En julio el gasto llegó al 111,35 % de su objetivo y el semáforo lo marca en rojo. Las ventas llegaron al 111,11 %. El
presupuesto flexible ajusta el objetivo de gasto a lo que se vendió de verdad, pero solo en el gasto que sube con las
ventas: compras y transportes, según la regla de la empresa que separa el gasto fijo del variable. Con ese ajuste,
julio gastó 7.286,54 € de más, un 1,45 %. Lo que el semáforo marca como un 11 % de exceso se queda en algo más del 1 %.

En el acumulado de los siete meses, el gasto supera su objetivo ajustado en 59.722,89 €, un 4,37 %. Una primera
versión trataba todo el gasto como variable y daba 70.878,45 €. Separar el fijo baja la desviación del acumulado,
porque en los meses de ventas por debajo del objetivo el gasto fijo no baja con ellas. Desde la versión 3.0.1, Power BI
calcula el presupuesto flexible con esa separación. El semáforo sigue comparando con el objetivo fijo.

### El cumplimiento del margen se mide como cociente de porcentajes

En mayo el margen bruto fue del 39,44 % frente a un objetivo del 31,67 %. Hasta la versión 2.1, Power BI lo publicaba
como un cumplimiento del 124,53 %. Dividir un porcentaje entre otro no significa nada para el negocio. Lo que se publica
en control de gestión es la diferencia: 7,77 puntos por encima del objetivo. Desde la versión 3.0, Power BI da esa
diferencia. El fichero `c_objetivos.csv` conserva la columna del cociente.

### El reparto entre centros no sirve para decidir

De enero a julio, el centro de almacén reúne el 76,94 % del gasto porque recibe todas las compras de mercaderías,
1.063.649,33 €. Toda la nómina, 148.670,58 € con la Seguridad Social, está en el centro de recursos humanos, aunque en la
ficha de empleados nadie trabaja en ese departamento. Con ese reparto, el coste por centro mide dónde se
apuntó el gasto y no qué área lo consume. Para corregirlo hay que repartir la nómina por el departamento de cada
persona, un dato que no está en los asientos.

### La comprobación de la Seguridad Social admite cualquier cuota razonable

La comprobación de la nómina da por buena una cuota de empresa entre el 25 % y el 40 % de los sueldos. La de 2026 es
del 29,90 %, el mismo tipo medio que figura en la ficha de cada empleado. Es un rango demasiado amplio. Un error de varios
puntos pasaría sin aviso. La comprobación útil compara la cuota con el tipo de la ficha.

## El bloque de personas

El repositorio apenas publica el coste de personal y una comprobación de nómina. Con lo que hay en el diario y en
la ficha de empleados se pueden dar tres datos:

- la plantilla: nueve personas, todas en la empresa de enero a julio, que suman 8,8 jornadas completas porque una
  trabaja al 80 %. La revisión externa suponía que la cifra contaba a quien pasó algún día por la empresa;
- el peso del personal sobre las ventas: un 8,10 % de enero a julio;
- la discrepancia entre la nómina y la ficha: el diario carga 16.350,00 € de sueldos cada mes, sin pagas
  extraordinarias. La ficha da 18.166,67 € al mes con doce pagas o 15.571,43 € con catorce. La nómina contabilizada no
  cuadra con ninguna de las dos.

La rotación y el absentismo no se publican: con nueve personas, cada dato identifica a alguien. Por la misma razón, el
coste no se da por departamento.

## Los límites del propio repositorio

- Hasta la versión 2.1, Power BI era un visor de los ficheros ya calculados, sin relaciones ni tabla de fechas, y dos
  de sus medidas promediaban porcentajes. La versión 3.0 añade un modelo con tabla de hechos, tabla de cuentas y tabla
  de fechas. Corrige además esas dos medidas. El margen de los siete meses es del 42,02 %; la media de los siete
  porcentajes mensuales, que es lo que daba antes, es del 41,97 %. Las demás tablas siguen leyendo los ficheros ya calculados. Las medidas están
  en [`MEDIDAS.md`](../powerbi/MEDIDAS.md).
- **Las cifras no se pueden rehacer desde aquí.** El libro diario completo está en una base de datos que no se publica,
  como dice el [README](../README.md).
  La comprobación automática mira que los ficheros existan y que la portada coincida con ellos. Nada contable.

## Qué haría falta para cerrar cada punto

| Prioridad | Punto | Qué hace falta |
|---|---|---|
| Alta | Junio y julio | revisar la carga de esos dos meses contra sus documentos |
| Alta | Impuesto sobre Sociedades | provisión mensual del impuesto y gasto definitivo al cierre |
| Alta | Puente del presupuesto | presupuestar los gastos que no tenían partida; el puente por cuenta está hecho en la 3.0 |
| Alta | Existencias | estimar el stock en cada cierre intermedio |
| Media | Clientes con saldo a su favor | reclasificar a anticipos al cierre de cada periodo |
| Media | Fecha de las aperturas | cambiar la fecha de dos asientos |
| Media | Presupuesto flexible | llevarlo al semáforo; en Power BI ya es una medida, y el margen va en puntos desde la 3.0 |
| Media | Nómina y centros | repartir la nómina por departamento y cuadrarla con la ficha |
| Baja | Seguridad Social | comparar la cuota con el tipo de la ficha |
| Baja | Reproducibilidad | no tiene arreglo mientras el diario no se publique |
