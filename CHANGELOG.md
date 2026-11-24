# Registro de cambios

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
- Portada nueva, en español y en inglés (`c22ee02`).
- Se retira el cuaderno de 2024 (`analisis_contable.ipynb`), con su libro diario y su script de construcción
  (`daac5c6`). Sigue disponible en la versión 1.0.

## 1.0 · 13 de noviembre de 2026

Primera versión etiquetada. Recoge lo publicado entre el 10 de mayo y el 13 de noviembre de 2026: un cuaderno de
Python que levanta la cuenta de resultados y el movimiento del banco de 2024 a partir del libro diario de la empresa y
comprueba las dos cifras por un camino independiente. Su última versión se ejecuta sin base de datos, con el libro
diario en `datos/` (`5d7e9bc`), y su portada lleva un esquema de cómo funciona por dentro (`d07af5b`, `ec41fb6`).
