# Registro de cambios

## 3.1 · 24 de noviembre de 2026

- El informe 07 publica una cuenta de resultados de gestión con el Impuesto sobre Sociedades estimado al 23 %: el
  resultado de enero a julio después de impuestos sería de unos 313.165 €, y el de enero a mayo, sin los dos meses por
  revisar, de unos 65.134 €.

## 3.0.2 · 24 de noviembre de 2026

- La medida del presupuesto flexible deja fuera los gastos financieros, como ya decía `MEDIDAS.md`. Antes los sumaba
  con el gasto fijo. No cambia ninguna cifra, porque esos gastos no tienen presupuesto (`b0ed4f5`).

## 3.0.1 · 24 de noviembre de 2026

Correcciones tras una segunda revisión externa.

- El informe 03 seguía con el puente del presupuesto de la versión 2.1, por centro. Ahora va por cuenta, como los datos
  publicados en la 3.0 (`9e52fac`).
- El presupuesto flexible de Power BI solo ajusta a las ventas el gasto variable, con la regla de la empresa que separa
  el gasto fijo del variable. La desviación de los siete meses pasa de 70.878,45 € a 59.722,89 €. El informe 07 y
  `MEDIDAS.md` lo explican.
- La web enseña el Pareto de clientes y el de proveedores lado a lado, sin selector.
- La portada lleva otra vez un esquema de cómo se comprueba cada cifra, que se había perdido en la 2.0.

## 3.0 · 24 de noviembre de 2026

Power BI deja de ser un visor de ficheros y pasa a tener un modelo propio con sus medidas DAX. Llega el Pareto de
clientes y proveedores.

- Tres ficheros nuevos en `datos/`: la tabla de hechos con el real y el presupuesto de 2026 por mes y cuenta, la
  tabla de cuentas y el Pareto con la clase ABC de cada cliente y proveedor. Sale `d_concentracion_clientes.csv`
  (`aaaab64`).
- El puente del presupuesto compara cada cuenta con su presupuesto sumando todos sus centros. Antes lo hacía dentro de
  cada centro y presentaba como ahorro gasto apuntado en otro centro (`aaaab64`).
- La web enseña el Pareto en la vista de Dirección. Las imágenes de la portada se rehacen con las cifras de ahora
  (`aaaab64`).
- Power BI tiene una tabla de hechos, una tabla de cuentas y un calendario en DAX, con una página nueva, «Cuentas y
  Pareto». Las medidas que promediaban porcentajes se corrigen y el margen va en puntos. El código de cada medida está en
  [`powerbi/MEDIDAS.md`](powerbi/MEDIDAS.md) (`5f57ebd`).
- `comprobar.py` revisa también los ficheros que lee Power BI (`5f57ebd`).
- La portada y los informes 04 y 07 cuentan el modelo nuevo y los puntos ya corregidos (`181f351`).

## 2.1 · 24 de noviembre de 2026

Un informe nuevo que mide los defectos de los datos y del cálculo, sin cambiar los datos publicados.

- El informe [Lo que los datos no sostienen](informes/07_lo_que_los_datos_no_sostienen.md) recoge los 16 puntos de una
  revisión externa del repositorio. Mide cada uno con el libro diario, dice cuánto mueve las cifras publicadas y qué
  haría falta para corregirlo (`a4417e4`).
- La portada da el resultado como antes de impuestos y explica la desviación del presupuesto por los gastos que no
  tenían presupuesto. La sección de límites enlaza el informe nuevo (`a4417e4`).

## 2.0 · 24 de noviembre de 2026

El repositorio deja de ser un cuaderno de Python sobre un año y pasa a ser un cuadro de mando de contabilidad de
gestión, con web, Power BI e informes. Cambia también de nombre: `analisis-contable` pasa a
`management-accounting-analytics`.

- Una página web con tres vistas del libro diario, para dirección, para el controller y para contabilidad. Lee los 19
  ficheros CSV de `datos/` (`daac5c6`).
- Un informe por bloque en `informes/`, con la pregunta que contesta cada análisis, su fórmula, la cifra y cómo se
  comprueba. El estado de flujos de efectivo se comprobó además por otra vía (`daac5c6`, `a5d3425`).
- Un proyecto de Power BI en `powerbi/` con las mismas tres vistas sobre los mismos ficheros (`81eb952`, `1959632`,
  `d53b66e`). Lee los datos del repositorio en GitHub, así que se actualiza desde cualquier ordenador (`3b8c0ef`).
- Solo se publica 2026, de enero a julio. Las cifras de los ejercicios anteriores ya no salen; de ellos se cuenta el
  cierre, sin importes (`57b4ccf`, `22bb51d`).
- Portada nueva, en español y en inglés (`c22ee02`), con una imagen de cada vista (`8a899d8`).
- Comprobaciones en GitHub en cada cambio: los ficheros de la web, las cifras de la portada frente a los datos y los
  enlaces, con sus pruebas (`7663494`).
- Se retira el cuaderno de 2024 (`analisis_contable.ipynb`), con su libro diario y su script de construcción
  (`daac5c6`). Sigue disponible en la versión 1.0.

## 1.0 · 13 de noviembre de 2026

Primera versión etiquetada. Recoge lo publicado entre el 10 de mayo y el 13 de noviembre de 2026: un cuaderno de
Python que levanta la cuenta de resultados y el movimiento del banco de 2024 a partir del libro diario de la empresa y
comprueba las dos cifras por un camino independiente. Su última versión se ejecuta sin base de datos, con el libro
diario en `datos/` (`5d7e9bc`), y su portada lleva un esquema de cómo funciona por dentro (`d07af5b`, `ec41fb6`).
