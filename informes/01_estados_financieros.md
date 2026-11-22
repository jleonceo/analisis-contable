# Estados financieros

2025 fue el año con más ventas, más resultado y más caja de los cuatro. El balance cuadra todos los años. Su
patrimonio neto, su inmovilizado y su deuda a largo plazo se han rehecho por SQL y dan lo mismo al céntimo.

Datos a 31/07/2026. 2026 cubre de enero a julio.

## 2025 cerró con las ventas y el resultado más altos de la serie

**Pregunta.** ¿Cuánto vende la empresa y cuánto gana cada año?

**Cómo se calcula.** Las ventas son el haber menos el debe de las cuentas de ventas de mercaderías (70) en el año. El
resultado es lo que suman los ingresos (grupo 7) menos lo que suman los gastos (grupo 6). El diario no registra
impuesto sobre beneficios, así que el resultado es antes y después de impuestos a la vez.

| Año | Ventas (€) | Resultado (€) |
|---|---:|---:|
| 2023 | 1.054.769,16 | 494.909,11 |
| 2024 | 1.420.269,26 | 592.245,36 |
| 2025 | 1.947.317,98 | 1.120.974,42 |
| 2026, enero a julio | 1.834.612,84 | 406.707,28 |

**Segunda vía.** Una consulta sobre las cuentas 70 y los grupos 6 y 7 del diario da las mismas ocho cifras al céntimo.
El resultado de cada año cerrado coincide también con lo que el asiento de cierre lleva a la cuenta 129 (ver
[Fiscal y cierre](06_fiscal_y_cierre.md)).

**Cuándo engaña.** En siete meses de 2026 las ventas casi igualan las de todo 2025, pero el resultado no llega a la
mitad. La mayor parte de la diferencia está en las compras, que se cuentan en [Rentabilidad y márgenes](02_rentabilidad_y_margenes.md).

## La caja que deja la operación después de invertir creció un 51,2 % en 2025

**Pregunta.** ¿Cuánto dinero genera la actividad, cuánto se va en inversiones y cuánto en devolver deuda?

**Cómo se calcula.** El estado de flujos de efectivo por el método indirecto parte del resultado y lo ajusta por lo
que no mueve caja: amortizaciones, provisiones y cambios en clientes, proveedores y existencias. Separa tres flujos:

- **explotación**, lo que deja la actividad;
- **inversión**, lo que se paga por inmovilizado;
- **financiación**, lo que entra o sale por deuda y capital.

La **caja libre** es explotación más inversión: lo que queda después de mantener la empresa y antes de pagar la deuda.

| Año | Explotación (€) | Inversión (€) | Financiación (€) | Variación de tesorería (€) | Caja libre (€) |
|---|---:|---:|---:|---:|---:|
| 2023 | 578.025,74 | 0,00 | −19.200,00 | 558.825,74 | 578.025,74 |
| 2024 | 760.234,45 | −2.000,00 | −19.200,00 | 739.034,45 | 758.234,45 |
| 2025 | 1.149.748,40 | −3.600,00 | −19.200,00 | 1.126.948,40 | 1.146.148,40 |
| 2026, enero a julio | 426.700,24 | 0,00 | −8.000,00 | 418.700,24 | 426.700,24 |

**Segunda vía.** La variación de tesorería de cada año es el movimiento neto de las cuentas de bancos y caja (57). Una
consulta sobre esas cuentas da las cuatro cifras al céntimo, una vez quitado el asiento de apertura de 2023, que es
saldo inicial y no flujo del año. El reparto se rehace también con consultas sobre el diario:

- **financiación** es el principal de deuda devuelto cada año: 19.200,00 € de 2023 a 2025 y 8.000,00 € en 2026;
- **inversión** es el inmovilizado comprado sin IVA menos la parte financiada sin pagar: 2.000,00 € en 2024 y
  3.600,00 € en 2025;
- **explotación** es el resto de la variación, con los intereses y el IVA de las compras de inmovilizado dentro.

Las doce cifras coinciden. La caja libre es la variación más el principal devuelto.

**Cuándo engaña.** Una compra financiada por el vendedor no pasa entera por la caja. El 1 de mayo de 2025 se compra un
elemento de transporte por 18.000 €: se pagan 3.600 € más el IVA y el resto queda como deuda por arrendamiento
financiero. El estado de flujos solo cuenta como inversión lo pagado. Un cálculo que cuente los 18.000 € como pago da
una caja libre de 1.131.748,40 € en 2025, con la misma variación de tesorería.

## El balance cuadra los cuatro años y el patrimonio neto de 2025 casi cuadruplica el de 2023

**Pregunta.** ¿Qué tiene la empresa, cuánto debe y cuánto es de sus socios al cierre de cada año?

**Cómo se calcula.** El balance agrupa el saldo de cada cuenta al 31 de diciembre en cinco masas, según el plan
general de contabilidad. 2026 va al 31 de julio. El patrimonio neto incluye el resultado del año.

| Masa (€) | 2023 | 2024 | 2025 | 31/07/2026 |
|---|---:|---:|---:|---:|
| Activo no corriente | 33.399,96 | 29.399,96 | 38.399,96 | 33.149,96 |
| Activo corriente | 851.630,74 | 1.687.271,01 | 3.020.440,30 | 3.590.700,35 |
| **Total activo** | **885.030,70** | **1.716.670,97** | **3.058.840,26** | **3.623.850,31** |
| Patrimonio neto | 593.309,11 | 1.185.554,47 | 2.306.528,89 | 2.713.236,17 |
| Pasivo no corriente | 46.400,00 | 27.200,00 | 22.400,00 | 14.400,00 |
| Pasivo corriente | 245.321,59 | 503.916,50 | 729.911,37 | 896.214,14 |
| **Total patrimonio neto y pasivo** | **885.030,70** | **1.716.670,97** | **3.058.840,26** | **3.623.850,31** |

**Segunda vía.** Tres de las cinco masas se han rehecho con consultas sobre el diario y los asientos de cierre:

- **patrimonio neto**: el saldo de las cuentas 10 a 13 más, en 2026, el resultado de enero a julio;
- **activo no corriente**: el saldo del grupo 2, con su amortización acumulada;
- **pasivo no corriente**: el saldo de las deudas a largo plazo (17).

Las tres coinciden al céntimo los cuatro años. El activo corriente y el pasivo corriente no se han rehecho uno a uno:
su diferencia queda fijada por las otras tres masas, porque el balance cuadra.

**Cuándo engaña.** Al cierre de 2025, la tesorería es el 83 % del activo corriente. El diario no tiene apuntes de
dividendos en ninguno de los cuatro años. Un balance que crece así no dice si ese dinero está bien empleado. Los ratios
de liquidez y solvencia están en [tesoreria-forecast-ia](https://github.com/jleonceo/tesoreria-forecast-ia).

## Lo que no entra

- **El EBITDA.** Dos cálculos de la casa lo definen distinto y dan cifras distintas en 2024 y 2025. Uno suma al
  resultado de explotación solo la amortización; el otro suma los ajustes del estado de flujos. Hasta fijar una
  definición, no se publica.

Ficheros: `datos/d_ventas_resultado.csv`, `datos/d_flujos.csv` y `datos/d_balance_masas.csv`.
