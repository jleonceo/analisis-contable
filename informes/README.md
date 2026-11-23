# Informes por bloque

Cada informe explica un bloque de análisis del cuadro de mando: qué pregunta contesta cada análisis, cómo se calcula,
qué da sobre los datos a 31/07/2026 y cómo se ha comprobado esa cifra por otro camino. Están escritos para quien
quiere revisar el método antes de fiarse de una cifra.

Van del más general al más concreto:

| Informe | Qué contesta |
|---|---|
| [Estados financieros](01_estados_financieros.md) | cuánto vende y gana la empresa, qué caja genera y cómo está su balance |
| [Rentabilidad y márgenes](02_rentabilidad_y_margenes.md) | qué parte de las ventas se queda como margen y cuánto hay que vender para no perder |
| [Presupuesto y coste por centro](03_presupuesto_objetivos_y_centros.md) | dónde se aparta 2026 del presupuesto y de los objetivos; qué cuesta cada centro |
| [Clientes y proveedores](04_clientes_y_proveedores.md) | cuánto depende la empresa de pocos clientes, quién paga tarde y quién pasa de su límite |
| [Calidad del libro diario](05_calidad_del_libro_diario.md) | si el diario cuadra y qué apuntes hay que revisar a mano |
| [Fiscal y cierre](06_fiscal_y_cierre.md) | si el cierre, la reserva legal, el IVA soportado y la nómina están bien contabilizados |

## Cómo se ha comprobado cada cifra

Las cifras salen de un programa de análisis que lee el libro diario en MySQL. Cada una se ha vuelto a calcular con una
consulta SQL escrita aparte, sobre las tablas del diario y no sobre lo que produce el programa. Cuando las dos vías dan
lo mismo, el informe lo dice en la línea «Segunda vía». Cuando no se ha podido rehacer, lo dice también, con el motivo.

Las cifras de ventas, resultado, margen bruto, margen neto, variación de tesorería, ingresos por línea, objetivos de
2026, resultado real del presupuesto y reserva legal se comprueban además cada vez que se regeneran los datos. Si alguna no coincide al céntimo, los ficheros de
`datos/` no se escriben.

## Lo que hay que saber antes de leer

- **La empresa es ficticia.** TechAcces es una distribuidora inventada; sus datos se generaron para practicar.
- **2026 llega hasta julio.** Sus cifras son de siete meses y no se comparan con un año entero sin decirlo.
- **La rentabilidad se publica solo de 2026.** Los ejercicios de 2023 a 2025 salen de un dato generado en el que las
  compras no siguen a las ventas: sus márgenes no son los de una pyme real. Los controles los siguen comprobando.
- **Los clientes van por su código de cuenta.** El nombre de un cliente, un proveedor o una persona no se publica.
- **El fraude, la previsión de caja, la antigüedad de saldos y los ratios de liquidez** están en otros dos
  repositorios, [control-interno-fraude-ia](https://github.com/jleonceo/control-interno-fraude-ia) y
  [tesoreria-forecast-ia](https://github.com/jleonceo/tesoreria-forecast-ia). Aquí no se repiten.
