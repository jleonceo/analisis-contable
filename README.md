# Análisis financiero con Python · TechAcces SL 2024

**Juan Luis León Rodríguez · Proyecto TechAcces · Mayo 2026**

[Español](#español) · [English](#english)

---

## Español

> Nota: el análisis se hizo en mayo de 2026 sobre el diario de TechAcces SL, una empresa
> **ficticia** simulada con realismo (no es una empresa real). La base de datos ha seguido
> creciendo desde entonces, así que las cifras de este informe valen como foto de esa fecha;
> lo que se transfiere es el método, no los números concretos.

---

### Problema de negocio

TechAcces SL es un e-commerce simulado de accesorios tecnológicos. A pesar de tener un margen
bruto del 91,7%, en esta foto de 2024 la empresa cierra con pérdidas de -57.742 €.

Este análisis identifica las causas, cuantifica el impacto y propone soluciones concretas con
simulación de escenarios.

---

### Resultados clave (foto de mayo de 2026)

| Métrica | Valor |
|---|---|
| **Ventas totales** | 753.263 € |
| **Margen bruto** | 690.688 € (91,7%) |
| **EBITDA** | 211.122 € (28,0%) |
| **Resultado final** | -57.742 € |
| **Con refinanciación de deuda** | +21.033 € |
| **Con todas las medidas** | +148.006 € |

---

### Conclusiones

- El negocio operativo es excelente: el problema es financiero.
- Los gastos financieros del préstamo ICO (262.583 €) destruyen el resultado.
- El 44,7% de las ventas se concentra en Q4, con tensión de tesorería en Q1-Q3.
- Solo refinanciando la deuda un 30% la empresa pasa a beneficios.

---

### Stack técnico

| Herramienta | Uso |
|---|---|
| **Python + Pandas** | Análisis y manipulación de datos |
| **SQLAlchemy + PyMySQL** | Conexión directa a MySQL sin CSV intermedios |
| **Matplotlib** | Visualizaciones y gráficos |
| **OpenPyXL** | Exportación a Excel con 5 pestañas formateadas |
| **MySQL** | Base de datos con 4.006 líneas contables de la empresa simulada |

---

### Estructura del proyecto

```
analisis-contable/
├── analisis_contable.ipynb                 # Notebook principal
├── analisis_contable.html                  # Versión navegador sin instalar nada
├── Informe_Financiero_TechAcces_2024.xlsx  # Excel entregable con 5 pestañas
├── requirements.txt                        # Dependencias
└── README.md                               # Este archivo
```

---

### Cómo ejecutar

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

### Contenido del análisis

1. **Exploración inicial**: 4.006 líneas, 1.525 asientos, cuadre perfecto debe = haber.
2. **Ventas mensuales**: evolución mensual y comparativa B2C frente a B2B.
3. **Desglose de gastos**: por categoría, con porcentaje sobre el total.
4. **Cuenta de resultados**: desde ventas hasta resultado final, con gráfico waterfall.
5. **Análisis trimestral**: estacionalidad y distribución de ventas y gastos.
6. **Proyección de tesorería**: flujo neto mensual y saldo acumulado.
7. **Simulador de escenarios**: 4 escenarios con impacto en el resultado final.
8. **Exportación a Excel**: informe con 5 pestañas formateadas.

### Repos relacionados

Este análisis es una pieza de un portfolio de casos de analítica. Las piezas hermanas:

- [lead-scoring-ml](https://github.com/jleonceo/lead-scoring-ml): predecir qué lead acaba comprando, con modelos de clasificación.
- [RFM-Customer-Analytics](https://github.com/jleonceo/RFM-Customer-Analytics): segmentación de clientes por recencia, frecuencia e importe.
- [accident-intelligent-agent](https://github.com/jleonceo/accident-intelligent-agent): ETL, exploración y modelo para predecir la gravedad de un accidente de tráfico.
- [accounting-agent-swarm](https://github.com/jleonceo/accounting-agent-swarm): el enjambre de agentes que contabiliza sobre esta misma empresa simulada.

---

*Parte del portfolio de [Juan Luis León](https://github.com/jleonceo) · [juanluisleon.vercel.app](https://juanluisleon.vercel.app) · Licencia [MIT](LICENSE)*

---

## English

> Note: the analysis was done in May 2026 against the ledger of TechAcces SL, a **fictional**
> company simulated to behave like a real one (it is not a real business). The database has kept
> growing since, so read these figures as a snapshot of that date. What carries over is the
> method, not the particular numbers.

> On the accounting terms: the books are Spanish, so a few words stay in Spanish. An *asiento*
> is a journal entry, and *debe* and *haber* are the debit and credit sides of it. The lender
> behind the loan below, the ICO, is Spain's state-owned credit institute.

---

### The business problem

TechAcces SL is a simulated online shop selling tech accessories. Gross margin runs at 91.7%,
and even so this 2024 snapshot closes the year -57,742 € in the red.

The analysis works out why, puts a number on each cause, and tests concrete fixes against
simulated scenarios.

---

### Headline figures (the May 2026 snapshot)

| Metric | Value |
|---|---|
| **Total sales** | 753,263 € |
| **Gross margin** | 690,688 € (91.7%) |
| **EBITDA** | 211,122 € (28.0%) |
| **Net result** | -57,742 € |
| **With the debt refinanced** | +21,033 € |
| **With every measure applied** | +148,006 € |

---

### Conclusions

- The trading side of the business is excellent. What breaks it sits below the operating line.
- The ICO loan's financing costs (262,583 €) destroy the result.
- Q4 takes 44.7% of sales, which leaves cash tight from Q1 through Q3.
- Refinancing the debt by 30% is enough on its own to put the company back in profit.

---

### Technical stack

| Tool | What it does here |
|---|---|
| **Python + Pandas** | Analysis and data wrangling |
| **SQLAlchemy + PyMySQL** | Straight to MySQL, no CSV in between |
| **Matplotlib** | Charts |
| **OpenPyXL** | Excel export, 5 formatted sheets |
| **MySQL** | The simulated company's books: 4,006 ledger lines |

---

### Project layout

```
analisis-contable/
├── analisis_contable.ipynb                 # The notebook
├── analisis_contable.html                  # Read it in a browser, nothing to install
├── Informe_Financiero_TechAcces_2024.xlsx  # The Excel deliverable, 5 sheets
├── requirements.txt                        # Dependencies
└── README.md                               # This file
```

---

### Running it

1. Clone the repository.
2. Drop a `.env` file in the folder with your MySQL credentials:

```
DB_USER=your_user
DB_PASS=your_password
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=your_database
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Open the notebook in Jupyter:

```bash
jupyter notebook analisis_contable.ipynb
```

---

### What the analysis covers

1. **First look**: 4,006 ledger lines across 1,525 journal entries, debit and credit tie out to the cent.
2. **Monthly sales**: how they move month to month, and B2C against B2B.
3. **Expense breakdown**: by category, each as a share of the total.
4. **Income statement**: from sales down to the net result, with a waterfall chart.
5. **Quarterly analysis**: seasonality, and how sales and expenses fall across the year.
6. **Cash projection**: monthly net flow and the running balance.
7. **Scenario simulator**: 4 scenarios and what each one does to the net result.
8. **Excel export**: the report, 5 formatted sheets.

### Related repositories

This analysis is one piece of an analytics portfolio. Its sibling projects:

- [lead-scoring-ml](https://github.com/jleonceo/lead-scoring-ml): predicting which lead ends up buying, with classification models.
- [RFM-Customer-Analytics](https://github.com/jleonceo/RFM-Customer-Analytics): customer segmentation by recency, frequency and monetary value.
- [accident-intelligent-agent](https://github.com/jleonceo/accident-intelligent-agent): ETL, exploration and a model to predict how severe a road accident is.
- [accounting-agent-swarm](https://github.com/jleonceo/accounting-agent-swarm): the agent swarm that does the bookkeeping for this same simulated company.

---

*Part of [Juan Luis León](https://github.com/jleonceo)'s portfolio · [juanluisleon.vercel.app](https://juanluisleon.vercel.app) · [MIT](LICENSE) licence*
