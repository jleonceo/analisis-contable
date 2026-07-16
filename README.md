# Análisis financiero con Python · TechAcces SL 2024

**Juan Luis León Rodríguez · Proyecto TechAcces · Mayo 2026**

> Nota: el análisis se hizo en mayo de 2026 sobre el diario de TechAcces SL, una empresa
> **ficticia** simulada con realismo (no es una empresa real). La base de datos ha seguido
> creciendo desde entonces, así que las cifras de este informe valen como foto de esa fecha;
> lo que se transfiere es el método, no los números concretos.

---

## Problema de negocio

TechAcces SL es un e-commerce simulado de accesorios tecnológicos. A pesar de tener un margen
bruto del 91,7%, en esta foto de 2024 la empresa cierra con pérdidas de -57.742 €.

Este análisis identifica las causas, cuantifica el impacto y propone soluciones concretas con
simulación de escenarios.

---

## Resultados clave (foto de mayo de 2026)

| Métrica | Valor |
|---|---|
| **Ventas totales** | 753.263 € |
| **Margen bruto** | 690.688 € (91,7%) |
| **EBITDA** | 211.122 € (28,0%) |
| **Resultado final** | -57.742 € |
| **Con refinanciación de deuda** | +21.033 € |
| **Con todas las medidas** | +148.006 € |

---

## Conclusiones

- El negocio operativo es excelente: el problema es financiero.
- Los gastos financieros del préstamo ICO (262.583 €) destruyen el resultado.
- El 44,7% de las ventas se concentra en Q4, con tensión de tesorería en Q1-Q3.
- Solo refinanciando la deuda un 30% la empresa pasa a beneficios.

---

## Stack técnico

| Herramienta | Uso |
|---|---|
| **Python + Pandas** | Análisis y manipulación de datos |
| **SQLAlchemy + PyMySQL** | Conexión directa a MySQL sin CSV intermedios |
| **Matplotlib** | Visualizaciones y gráficos |
| **OpenPyXL** | Exportación a Excel con 5 pestañas formateadas |
| **MySQL** | Base de datos con 4.006 líneas contables de la empresa simulada |

---

## Estructura del proyecto

```
analisis-contable/
├── analisis_contable.ipynb                 # Notebook principal
├── analisis_contable.html                  # Versión navegador sin instalar nada
├── Informe_Financiero_TechAcces_2024.xlsx  # Excel entregable con 5 pestañas
├── requirements.txt                        # Dependencias
└── README.md                               # Este archivo
```

---

## Cómo ejecutar

1. Clona el repositorio.
2. Crea un archivo `.env` en la carpeta con tus credenciales MySQL:

```
DB_USER=tu_usuario
DB_PASS=tu_contraseña
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=tu_base_de_datos
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Abre el notebook en Jupyter:

```bash
jupyter notebook analisis_contable.ipynb
```

---

## Contenido del análisis

1. **Exploración inicial**: 4.006 líneas, 1.525 asientos, cuadre perfecto debe = haber.
2. **Ventas mensuales**: evolución mensual y comparativa B2C frente a B2B.
3. **Desglose de gastos**: por categoría, con porcentaje sobre el total.
4. **Cuenta de resultados**: desde ventas hasta resultado final, con gráfico waterfall.
5. **Análisis trimestral**: estacionalidad y distribución de ventas y gastos.
6. **Proyección de tesorería**: flujo neto mensual y saldo acumulado.
7. **Simulador de escenarios**: 4 escenarios con impacto en el resultado final.
8. **Exportación a Excel**: informe con 5 pestañas formateadas.

---

*Parte del portfolio de [Juan Luis León](https://github.com/jleonceo) · [juanluisleon.vercel.app](https://juanluisleon.vercel.app) · Licencia [MIT](LICENSE)*
