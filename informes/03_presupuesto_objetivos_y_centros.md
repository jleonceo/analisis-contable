# Presupuesto y coste por centro

De enero a julio de 2026 los ingresos cumplen su objetivo y el gasto lo supera en un 5,40 %. El resultado real queda
70.085,60 € por debajo del presupuestado. Tres partidas parecen gastar menos de lo previsto, 100.479,60 € entre las
tres. Su gasto está apuntado en otro centro y reaparece en el escalón de partidas sin presupuesto. Cada cifra de este informe se ha rehecho
por SQL.

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

**Cómo se calcula.** Una partida es una cuenta en un centro de coste. Para cada partida con presupuesto, su efecto
sobre el resultado es lo presupuestado menos lo real si es un gasto, o lo real menos lo presupuestado si es un ingreso.
Todo lo apuntado en una cuenta o un centro sin presupuesto se suma en un escalón aparte. Se cuentan solo los meses
terminados.

| Escalón | Efecto sobre el resultado (€) | Resultado acumulado (€) |
|---|---:|---:|
| Resultado presupuestado | | 476.792,88 |
| Transportes, almacén y logística | +40.975,01 | 517.767,89 |
| Publicidad, comercial | +34.479,59 | 552.247,48 |
| Arrendamientos, administración | +25.025,00 | 577.272,48 |
| Ventas de mercaderías | +3.045,69 | 580.318,17 |
| Compras de mercaderías, almacén y logística | −1.389,00 | 578.929,17 |
| Suministros, administración | +384,64 | 579.313,81 |
| Seguridad Social, recursos humanos | −0,10 | 579.313,71 |
| Partidas sin presupuesto | −172.606,43 | 406.707,28 |
| **Resultado real** | | **406.707,28** |

Los sueldos, con presupuesto, coinciden al céntimo con lo real y no mueven el resultado.

**Segunda vía.** Tres consultas independientes dan el resultado presupuestado, el real y el escalón sin presupuesto, al
céntimo. El real es el mismo que el de [Estados financieros](01_estados_financieros.md).

**Cuándo engaña.** El real de una partida es el de esa cuenta en ese centro. Un gasto apuntado en otro centro sale como
ahorro en su partida y como gasto sin presupuesto en el escalón final. Les pasa a las tres partidas que parecen ahorrar:

- **arrendamientos**: presupuestados en administración; los 25.025,00 € reales están en almacén;
- **publicidad**: presupuestada en comercial, que recibe 3.795,00 €; en administración hay 33.731,02 €;
- **transporte**: presupuestado en almacén, que recibe 8.703,30 €; en administración hay 40.159,73 €.

Ninguna de las tres ahorra de verdad. El gasto de las partidas con presupuesto no es el gasto total del
cumplimiento de objetivos, que incluye todo el grupo 6.

## La venta a empresas pasó a ser el 78,56 % de los ingresos en 2026

**Pregunta.** ¿Cuánto factura cada línea de negocio?

**Cómo se calcula.** Las ventas de mercaderías de cada año, separadas por la línea de negocio que lleva cada apunte.

| Año | B2B (€) | B2C (€) |
|---|---:|---:|
| 2023 | 361.280,43 | 693.488,73 |
| 2024 | 508.518,25 | 911.751,01 |
| 2025 | 723.404,28 | 1.223.913,70 |
| 2026, enero a julio | 1.441.253,19 | 393.359,65 |

**Segunda vía.** Las dos líneas de cada año suman las ventas del año, comprobadas al céntimo con una consulta sobre las
cuentas 70.

**Lo que no se publica.** El margen de cada línea. Todo el gasto del diario está en la línea común, sin asignar a B2B
ni a B2C, salvo dos apuntes de amortización de 2023 que no llevan línea. La única base de reparto con dato son las ventas. Repartir el gasto común en proporción a las ventas da a
las dos líneas el mismo margen que la empresa entera: el 57,57 % en 2025. Esa cifra no informa de nada, así que no se
enseña.

## El coste de cada centro se lee dentro de su año

**Pregunta.** ¿Cuánto cuesta cada centro de coste?

**Cómo se calcula.** La suma del grupo 6 de cada año, por el centro que lleva cada apunte.

| Centro (€) | 2023 | 2024 | 2025 | 2026, enero a julio |
|---|---:|---:|---:|---:|
| Almacén y logística | 303.995,63 | 372.392,89 | 550.167,42 | 1.098.627,63 |
| Administración | 107.215,21 | 247.157,04 | 13.429,40 | 176.490,21 |
| Recursos humanos | 135.882,92 | 208.473,97 | 254.863,86 | 148.670,58 |
| Comercial | 7.166,25 | 0,00 | 7.882,88 | 3.795,00 |
| Sin centro | 5.600,04 | 0,00 | 0,00 | 322,14 |

**Segunda vía.** Una consulta agrupada por año y centro da las veinte cifras al céntimo.

**Cuándo engaña.** El reparto de una misma cuenta entre centros cambia de un año a otro. Administración pasa de
247.157,04 € en 2024 a 13.429,40 € en 2025. Comparar un centro entre años mide la forma de imputar, no lo que cuesta.

## El coste de personal se publica solo en total

**Pregunta.** ¿Cuánto cuesta la plantilla cada año?

**Cómo se calcula.** Sueldos y salarios (640) más Seguridad Social a cargo de la empresa (642). Las personas son las
que estuvieron en plantilla algún día del año.

| Año | Personas | Sueldos (€) | Seguridad Social (€) | Coste total (€) |
|---|---:|---:|---:|---:|
| 2023 | 8 | 104.605,82 | 31.277,10 | 135.882,92 |
| 2024 | 10 | 160.488,00 | 47.985,97 | 208.473,97 |
| 2025 | 9 | 196.200,04 | 58.663,82 | 254.863,86 |
| 2026, enero a julio | 9 | 114.450,00 | 34.220,58 | 148.670,58 |

**Segunda vía.** Las cuentas 640 y 642 de cada año y el número de fichas de empleado con alta antes de fin de año y sin
baja antes de su inicio dan las dieciséis cifras.

**Lo que no se publica.** El coste por departamento. Con menos de cinco personas en un grupo, el coste del grupo deja
ver el sueldo de alguien.

Ficheros: `datos/c_objetivos.csv`, `datos/d_puente_presupuesto.csv`, `datos/c_presupuesto_real.csv`,
`datos/c_ingresos_linea.csv`, `datos/c_coste_centro.csv` y `datos/c_coste_laboral.csv`.
