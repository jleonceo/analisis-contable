# Estados financieros

De enero a julio de 2026 la empresa vendió 1.834.612,84 € y ganó 406.707,28 €. El balance cuadra al 31 de julio. Su
patrimonio neto, su inmovilizado y su deuda a largo plazo se han rehecho por SQL y dan lo mismo al céntimo.

Datos a 31/07/2026. Se publica solo el ejercicio 2026, de enero a julio. Los años anteriores salen de un dato generado
en el que las compras no siguen a las ventas, y sus márgenes no son los de una pyme real.

## La empresa ganó 22 céntimos de cada euro vendido de enero a julio

**Pregunta.** ¿Cuánto vende la empresa y cuánto gana?

**Cómo se calcula.** Las ventas son el haber menos el debe de las cuentas de ventas de mercaderías (70) en el periodo.
El resultado es lo que suman los ingresos (grupo 7) menos lo que suman los gastos (grupo 6). El diario no registra
impuesto sobre beneficios, así que el resultado es antes y después de impuestos a la vez.

| Periodo | Ventas (€) | Resultado (€) |
|---|---:|---:|
| 2026, enero a julio | 1.834.612,84 | 406.707,28 |

**Segunda vía.** Una consulta sobre las cuentas 70 y los grupos 6 y 7 del diario da las dos cifras al céntimo.

**Cuándo engaña.** Son siete meses: no es el resultado de un año. La mayor parte del gasto está en las compras, que se
cuentan en [Rentabilidad y márgenes](02_rentabilidad_y_margenes.md).

## La operación dejó 426.700,24 € de caja libre en siete meses

**Pregunta.** ¿Cuánto dinero genera la actividad, cuánto se va en inversiones y cuánto en devolver deuda?

**Cómo se calcula.** El estado de flujos de efectivo por el método indirecto parte del resultado y lo ajusta por lo
que no mueve caja: amortizaciones, provisiones y cambios en clientes, proveedores y existencias. Separa tres flujos:

- **explotación**, lo que deja la actividad;
- **inversión**, lo que se paga por inmovilizado;
- **financiación**, lo que entra o sale por deuda y capital.

La **caja libre** es explotación más inversión: lo que queda después de mantener la empresa y antes de pagar la deuda.

| Periodo | Explotación (€) | Inversión (€) | Financiación (€) | Variación de tesorería (€) | Caja libre (€) |
|---|---:|---:|---:|---:|---:|
| 2026, enero a julio | 426.700,24 | 0,00 | −8.000,00 | 418.700,24 | 426.700,24 |

**Segunda vía.** La variación de tesorería es el movimiento neto de las cuentas de bancos y caja (57) de enero a julio.
Una consulta sobre esas cuentas da la cifra al céntimo. El reparto se rehace también con consultas sobre el diario:

- **financiación** es el principal de deuda devuelto: 8.000,00 €;
- **inversión** es el inmovilizado comprado sin IVA menos la parte financiada sin pagar: no hubo compras en el periodo;
- **explotación** es el resto de la variación, con los intereses dentro.

La caja libre es la variación más el principal devuelto.

**Cuándo engaña.** Una compra financiada por el vendedor no pasa entera por la caja. El estado de flujos solo cuenta
como inversión lo pagado: si una parte queda como deuda con el vendedor, la inversión sale menor que el precio.

## El balance cuadra al 31 de julio de 2026

**Pregunta.** ¿Qué tiene la empresa, cuánto debe y cuánto es de sus socios?

**Cómo se calcula.** El balance agrupa el saldo de cada cuenta al 31 de julio de 2026 en cinco masas, según el plan
general de contabilidad. El patrimonio neto incluye el resultado de enero a julio.

| Masa | 31/07/2026 (€) |
|---|---:|
| Activo no corriente | 33.149,96 |
| Activo corriente | 3.590.700,35 |
| **Total activo** | **3.623.850,31** |
| Patrimonio neto | 2.713.236,17 |
| Pasivo no corriente | 14.400,00 |
| Pasivo corriente | 896.214,14 |
| **Total patrimonio neto y pasivo** | **3.623.850,31** |

**Segunda vía.** Tres de las cinco masas se han rehecho con consultas sobre el diario y los asientos de cierre:

- **patrimonio neto**: el saldo de las cuentas 10 a 13 más el resultado de enero a julio;
- **activo no corriente**: el saldo del grupo 2, con su amortización acumulada;
- **pasivo no corriente**: el saldo de las deudas a largo plazo (17).

Las tres coinciden al céntimo. El activo corriente y el pasivo corriente no se han rehecho uno a uno: su diferencia
queda fijada por las otras tres masas, porque el balance cuadra.

**Cuándo engaña.** El diario no tiene apuntes de dividendos. Un balance con tanta tesorería no dice si ese dinero está
bien empleado. Los ratios de liquidez y solvencia están en
[tesoreria-forecast-ia](https://github.com/jleonceo/tesoreria-forecast-ia).

## Lo que no entra

- **Los ejercicios de 2023 a 2025.** Salen de un dato generado en el que las compras no siguen a las ventas: sus
  márgenes no son los de una pyme real. Los controles del exportador los siguen comprobando, pero no se publican.
- **El EBITDA.** Dos cálculos de la casa lo definen distinto y dan cifras distintas. Uno suma al resultado de
  explotación solo la amortización; el otro suma los ajustes del estado de flujos. Hasta fijar una definición, no se
  publica.

Ficheros: `datos/d_ventas_resultado.csv`, `datos/d_flujos.csv` y `datos/d_balance_masas.csv`.
