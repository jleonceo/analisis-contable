# 📊 Análisis Financiero con Python — TechAcces SL 2024

**Juan Luis León Rodríguez · Proyecto TechAcces · Mayo 2026**

---

## 🎯 Problema de Negocio

TechAcces SL es un e-commerce de accesorios tecnológicos con sede en Tarragona.
A pesar de tener un margen bruto del 91,7%, la empresa cierra 2024 con pérdidas de -57.742€.

Este análisis identifica las causas, cuantifica el impacto y propone soluciones concretas con simulación de escenarios.

---

## 📈 Resultados Clave

| Métrica | Valor |
|---|---|
| **Ventas totales** | 753.263 € |
| **Margen bruto** | 690.688 € (91,7%) |
| **EBITDA** | 211.122 € (28,0%) |
| **Resultado final** | -57.742 € 🔴 |
| **Con refinanciación deuda** | +21.033 € ✅ |
| **Con todas las medidas** | +148.006 € ✅ |

---

## 💡 Conclusiones

- El negocio operativo es excelente — el problema es financiero
- Los gastos financieros del préstamo ICO (262.583€) destruyen el resultado
- El 44,7% de las ventas se concentran en Q4 — tensión de tesorería en Q1-Q3
- Solo refinanciando la deuda un 30% la empresa pasa a beneficios

---

## 🛠️ Stack Técnico

| Herramienta | Uso |
|---|---|
| **Python + Pandas** | Análisis y manipulación de datos |
| **SQLAlchemy + PyMySQL** | Conexión directa a MySQL sin CSV intermedios |
| **Matplotlib** | Visualizaciones y gráficos profesionales |
| **OpenPyXL** | Exportación a Excel con 5 pestañas formateadas |
| **MySQL** | Base de datos con 4.006 líneas contables reales |

---

## 📂 Estructura del Proyecto

```
analisis-contable/
├── analisis_contable.ipynb                 # Notebook principal
├── analisis_contable.html                  # Versión navegador sin instalar nada
├── Informe_Financiero_TechAcces_2024.xlsx  # Excel entregable con 5 pestañas
├── requirements.txt                        # Dependencias
└── README.md                               # Este archivo
```

---

## ▶️ Cómo Ejecutar

1. Clona el repositorio
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

## 📊 Contenido del Análisis

1. **Exploración inicial** — 4.006 líneas, 1.525 asientos, cuadre perfecto debe=haber
2. **Ventas mensuales** — evolución mensual y comparativa B2C vs B2B
3. **Desglose de gastos** — por categoría con porcentaje sobre total
4. **Cuenta de resultados** — desde ventas hasta resultado final con gráfico waterfall
5. **Análisis trimestral** — estacionalidad y distribución de ventas y gastos
6. **Proyección de tesorería** — flujo neto mensual y saldo acumulado
7. **Simulador de escenarios** — 4 escenarios con impacto en resultado final
8. **Exportación Excel** — informe profesional con 5 pestañas formateadas

---

*Juan Luis León Rodríguez · TechAcces Portfolio 2026*
