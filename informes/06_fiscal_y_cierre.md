# Fiscal y cierre

El cierre de cada ejercicio traspasa el resultado entero y la apertura siguiente lo recoge. El IVA soportado y la nómina
están bien contabilizados en todos los asientos que se pueden juzgar. Falta dotar la reserva legal: 11.680,00 €. Cada
cifra de este informe se ha rehecho por SQL.

Datos a 31/07/2026.

## Falta dotar la reserva legal entera

**Pregunta.** ¿Ha destinado la sociedad a reserva legal lo que pide la ley?

**Cómo se calcula.** La Ley de Sociedades de Capital (artículo 274.1) obliga a llevar a reserva legal el 10 % del
beneficio de cada ejercicio, hasta que la reserva llegue al 20 % del capital. En cada reparto del resultado, lo que
falta es el menor de dos importes: el 10 % del beneficio o lo que queda hasta el 20 % del capital. A eso se resta lo
que el reparto lleva a la reserva.

El capital es de 58.400,00 €, así que el tope de la reserva es de 11.680,00 €. No se ha dotado nada.
El diario no tiene ningún apunte en la cuenta de reserva legal (112). El 10 % del beneficio de 2023, 49.490,91 €, ya bastaba para dotarla entera.

**Segunda vía.** Una consulta sobre las cuentas de capital (100) y de reserva legal (112), en el diario y en los
asientos de cierre, da el 20 % del capital menos la reserva: 11.680,00 €. Esta cifra se comprueba cada vez que se
regeneran los datos.

**La otra mitad de la prueba.** La sociedad no está en causa de disolución por pérdidas (artículo 363.1.e): al corte,
su patrimonio neto es 46 veces el capital.

## El cierre traspasa el resultado entero y la apertura lo recoge

**Pregunta.** ¿El cierre de cada año deja a cero las cuentas de gastos e ingresos, lleva el resultado a la cuenta del
resultado del ejercicio (129) y la apertura siguiente lo saca entero?

**Cómo se calcula.** Para cada ejercicio cerrado se compara lo que el asiento de cierre abona a la cuenta 129 con el
resultado del año calculado con el diario. Después, lo que la apertura del año siguiente carga a esa cuenta.

| Ejercicio | Resultado del diario (€) | Llevado a la 129 en el cierre (€) | Sacado de la 129 en la apertura siguiente (€) |
|---|---:|---:|---:|
| 2023 | 494.909,11 | 494.909,11 | 494.909,11 |
| 2024 | 592.245,36 | 592.245,36 | 592.245,36 |
| 2025 | 1.120.974,42 | 1.120.974,42 | 1.120.974,42 |

Cada asiento de cierre y de apertura cuadra. La apertura lleva el resultado al remanente.

**Segunda vía.** Una consulta sobre la tabla de cierres, agrupada por ejercicio y por tipo, da las seis cifras de la
129 y el cuadre de cada asiento.

**Cuándo engaña.** La prueba mira que el cierre sea coherente con el diario: un gasto que durante el año se llevó a
una cuenta equivocada, con su contrapartida bien puesta, llega al cierre cuadrado y el cierre lo traspasa sin que esta
prueba lo vea. Las aperturas no llevan siempre la misma fecha: la de 2024 es del
01/01/2024 y las de 2025 y 2026, del 31 de diciembre del año anterior.

## Ninguna compra que se puede juzgar lleva mal calculado su IVA soportado

**Pregunta.** En cada compra, ¿el IVA soportado es la base por el tipo?

**Cómo se calcula.** En cada asiento con IVA soportado (472) al debe, la base son los cargos a gastos (6) o a
inmovilizado (2) y la cuota, el cargo a la 472. Hay aviso si la cuota se aparta de base × tipo en más de un céntimo.

Son 752 asientos. De los 737 que traen tipo y base, ninguno se aparta y todas sus líneas de base y de cuota van al 21 %.
Los otros 15 no se pueden juzgar: no traen tipo de IVA o no tienen base en gastos ni en inmovilizado. Si se les supone
el 21 %, tres de ellos, de finales de 2023, se apartan 1,00 €.

**Segunda vía.** Una consulta con la misma regla da los 752 asientos, los 15 sin juzgar y ninguno fuera.

**Cuándo engaña.** La prueba toma un solo tipo por asiento. En 313 asientos la línea del proveedor o la del banco lleva
un 0 % de IVA; aquí no cambia nada, porque en los asientos juzgados las bases y las cuotas van todas al 21 %. Con bases a varios tipos, la
prueba daría avisos falsos.

## La nómina cuadra los 43 meses

**Pregunta.** ¿Cuadran la Seguridad Social y las retenciones con los sueldos? ¿Se paga lo que se debe al personal?

**Cómo se calcula.** Por cada mes con nómina se miran tres cosas:

- la Seguridad Social a cargo de la empresa (642) sobre los sueldos (640) está entre el 25 % y el 40 %;
- la retención de IRPF (4751) es igual a los sueldos por el porcentaje de retención de cada línea;
- la cuenta de remuneraciones pendientes de pago (465) queda a cero.

La Seguridad Social de la empresa es el 29,90 % de los sueldos todos los meses. Ninguna retención se aparta y la 465
queda a cero cada mes.

**Segunda vía.** Tres consultas sobre los asientos de nómina dan los 43 meses dentro de las tres reglas.

**Cuándo engaña.** El rango del 25 % al 40 % es amplio: la cuota real depende del convenio y la categoría de cada
persona. La prueba no comprueba que cada persona cotice por su base.

## Lo que no entra

- **La liquidación trimestral del IVA.** Sus diferencias trimestre a trimestre piden un criterio contable que todavía no
  está escrito.
- **Las retenciones declaradas a Hacienda.** Su comprobación depende de una configuración fiscal de la empresa que está
  sin confirmar.

Fichero: `datos/o_comprobaciones.csv`.
