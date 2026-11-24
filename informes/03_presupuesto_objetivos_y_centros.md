# Presupuesto y coste por centro

De enero a julio de 2026 los ingresos cumplen su objetivo y el gasto lo supera en un 5,40 %. El resultado real queda
70.085,60 € por debajo del presupuestado. Las cuentas con presupuesto apenas se desvían: la diferencia la explican
73.690,68 € de gastos que no tenían presupuesto. Cada cifra de este informe se ha rehecho por SQL.

Datos a 31/07/2026. El presupuesto y los objetivos solo existen para 2026.

## El gasto pasó de su objetivo en 5 de los 7 meses

**Pregunta.** ¿Van los ingresos y el gasto de cada mes al ritmo de su objetivo?

**Cómo se calcula.** Cumplimiento = real / objetivo × 100, mes a mes y acumulado. Los ingresos reales son las ventas
de mercaderías (70) del mes; el gasto real, todo el grupo 6. Los objetivos vienen fijados por la empresa.

| Mes de 2026 | Ingresos reales (€) | Cumplimiento de ingresos (%) | Gasto real (€) | Cumplimiento de gasto (%) |
|---|---:|---:|---:|---:|
| Enero | 91.218,81 | 94,34 | 80.280,55 | 105,67 |
| Febrero | 104.855,50 | 91,74 | 86.610,99 | 104,05 |
| Marzo | 119.528,45 | 97,09 | 103.549,49 | 98,79 |
| Abril | 133.729,50 | 100,00 | 114.017,45 | 101,97 |
| Mayo | 128.945,14 | 107,53 | 109.229,73 | 96,54 |
| Junio | 612.580,14 | 92,19 | 426.104,76 | 104,07 |
| Julio | 643.755,30 | 111,11 | 508.112,59 | 111,35 |
| **Enero a julio** | **1.834.612,84** | **100,17** | **1.427.905,56** | **105,40** |

Por línea de negocio, de enero a julio, la venta a empresas (B2B) llega al 101,21 % de su objetivo y la venta a
particulares (B2C) al 96,51 %.

**Segunda vía.** Una consulta que suma el diario de cada mes y lo divide por el objetivo de la tabla de objetivos da los
catorce cumplimientos mensuales, los dos acumulados y los dos de cada línea.

**Cuándo engaña.** Junio y julio facturan más de cuatro veces lo de cualquier mes anterior; su objetivo también es
más alto. Un cumplimiento cercano al 100 % no dice si el objetivo era razonable.

## Las partidas sin presupuesto dejan el resultado por debajo de lo previsto

**Pregunta.** ¿Qué partidas explican la diferencia entre el resultado presupuestado y el real?

**Cómo se calcula.** Una partida es una cuenta, sumando todos los centros de coste. Para cada cuenta con presupuesto, su
efecto sobre el resultado es lo presupuestado menos lo real si es un gasto, o lo real menos lo presupuestado si es un
ingreso. Lo apuntado en una cuenta sin presupuesto se suma en un escalón aparte. Se cuentan solo los meses terminados.

| Escalón | Efecto sobre el resultado (€) | Resultado acumulado (€) |
|---|---:|---:|
| Resultado presupuestado | | 476.792,88 |
| Ventas de mercaderías | +3.045,69 | 479.838,57 |
| Compras de mercaderías | −1.389,00 | 478.449,57 |
| Transportes | +815,28 | 479.264,85 |
| Publicidad, propaganda y relaciones públicas | +748,57 | 480.013,42 |
| Suministros | +384,64 | 480.398,06 |
| Seguridad Social a cargo de la empresa | −0,10 | 480.397,96 |
| Partidas sin presupuesto | −73.690,68 | 406.707,28 |
| **Resultado real** | | **406.707,28** |

Los arrendamientos y los sueldos coinciden al céntimo con lo presupuestado y no mueven el resultado. El escalón sin
presupuesto reúne siete cuentas. Las que más pesan son los seguros, con 37.368,19 €, y los servicios de profesionales,
con 28.760,35 €. Las otras cinco son las dos amortizaciones, los intereses, otros gastos financieros y las
reparaciones.

**Segunda vía.** Consultas independientes dan el real y el presupuesto de cada cuenta y el escalón sin presupuesto, al
céntimo. El real es el mismo que el de [Estados financieros](01_estados_financieros.md).

**Cuándo engaña.** Al sumar los centros, el puente no enseña dónde se apuntó cada gasto. Tres cuentas tienen el
presupuesto en un centro y el gasto en otro:

- **arrendamientos**: presupuestados en administración; los 25.025,00 € reales están en almacén;
- **publicidad**: presupuestada en comercial, que recibe 3.795,00 €; en administración hay 33.731,02 €;
- **transporte**: presupuestado en almacén, que recibe 8.703,30 €; en administración hay 40.159,73 €.

Comparadas dentro de cada centro, esas tres cuentas parecerían ahorrar 100.479,60 €, que es lo que contaba este informe
hasta la versión 3.0. El gasto de las cuentas con presupuesto tampoco es el gasto total del cumplimiento de objetivos,
que incluye todo el grupo 6.

## La venta a empresas pasó a ser el 78,56 % de los ingresos en 2026

**Pregunta.** ¿Cuánto factura cada línea de negocio?

**Cómo se calcula.** Las ventas de mercaderías de enero a julio, separadas por la línea de negocio que lleva cada
apunte.

| Periodo | B2B (€) | B2C (€) |
|---|---:|---:|
| 2026, enero a julio | 1.441.253,19 | 393.359,65 |

**Segunda vía.** Las dos líneas suman las ventas del periodo, comprobadas al céntimo con una consulta sobre las
cuentas 70.

**Lo que no se publica.** El margen de cada línea. Todo el gasto del diario está en la línea común, sin asignar a B2B
ni a B2C. La única base de reparto con dato son las ventas. Repartir el gasto común en proporción a las ventas da a
las dos líneas el mismo margen que la empresa entera. Esa cifra no informa de nada, así que no se enseña.

## Almacén y logística reúne tres de cada cuatro euros de gasto

**Pregunta.** ¿Cuánto cuesta cada centro de coste?

**Cómo se calcula.** La suma del grupo 6 de enero a julio, por el centro que lleva cada apunte.

| Centro | 2026, enero a julio (€) |
|---|---:|
| Almacén y logística | 1.098.627,63 |
| Administración | 176.490,21 |
| Recursos humanos | 148.670,58 |
| Comercial | 3.795,00 |
| Sin centro | 322,14 |

**Segunda vía.** Una consulta agrupada por centro da las cinco cifras al céntimo.

**Cuándo engaña.** El centro es el que lleva cada apunte. Una misma cuenta se reparte entre varios centros: el
transporte y la publicidad caen sobre todo en administración, aunque su presupuesto esté en almacén y en comercial.

## El coste de personal se publica solo en total

**Pregunta.** ¿Cuánto cuesta la plantilla?

**Cómo se calcula.** Sueldos y salarios (640) más Seguridad Social a cargo de la empresa (642). Las personas son las
que estuvieron en plantilla algún día del periodo.

| Periodo | Personas | Sueldos (€) | Seguridad Social (€) | Coste total (€) |
|---|---:|---:|---:|---:|
| 2026, enero a julio | 9 | 114.450,00 | 34.220,58 | 148.670,58 |

**Segunda vía.** Las cuentas 640 y 642 y el número de fichas de empleado con alta antes del corte y sin baja antes del
1 de enero dan las cuatro cifras.

**Lo que no se publica.** El coste por departamento. Con menos de cinco personas en un grupo, el coste del grupo deja
ver el sueldo de alguien.

Ficheros: `datos/c_objetivos.csv`, `datos/d_puente_presupuesto.csv`, `datos/c_presupuesto_real.csv`,
`datos/c_ingresos_linea.csv`, `datos/c_coste_centro.csv` y `datos/c_coste_laboral.csv`.
