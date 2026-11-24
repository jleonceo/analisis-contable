English version: [README.en.md](README.en.md)

# Contabilidad de gestión con datos

Tres cuadros de mando sobre el libro diario de una pyme: uno para dirección, otro para el controller y otro para
contabilidad. Casi todas las cifras se comprueban con un segundo cálculo independiente antes de publicarse. La empresa, TechAcces
SL, es ficticia: su contabilidad se generó para el proyecto.

**Resultado:** de enero a julio de 2026 la empresa vendió 1.834.612,84 € y ganó 406.707,28 € antes de impuestos, que
son 70.085,60 € menos de lo presupuestado. Casi toda la diferencia viene de 73.690,68 € de gastos que no tenían
presupuesto.

**Herramientas:** SQL (MySQL), Python, Power BI (DAX y Power Query), HTML y JavaScript.

[![comprobaciones](https://github.com/jleonceo/management-accounting-analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/jleonceo/management-accounting-analytics/actions/workflows/ci.yml)

```bash
git clone https://github.com/jleonceo/management-accounting-analytics.git
cd management-accounting-analytics
python -m http.server
```

Después se abre `http://localhost:8000` en el navegador. La versión de Power BI está en [`powerbi/`](powerbi/).

## Las tres vistas

| Vista | Pregunta que contesta | Qué muestra |
|---|---|---|
| Dirección | ¿Cómo va la empresa? | ventas, resultado, margen bruto y flujo de caja libre de enero a julio y su evolución mensual, y el Pareto de clientes y proveedores; en Power BI, además, el balance a 31 de julio |
| Controller | ¿Dónde se desvía del presupuesto? | puente de desviaciones por partida, coste por centro y grado de cumplimiento de objetivos |
| Contabilidad | ¿Está bien llevado el libro diario? | veinte controles sobre el diario, con lo que detecta cada uno |

A 31/07/2026, nueve de los veinte controles señalan incidencias que requieren revisión manual, entre ellas la
reserva legal sin dotar y 2.273 números de asiento sin usar.

![Vista de dirección: ventas, resultado, margen bruto y flujo de caja libre de enero a julio de 2026, y el Pareto de clientes y de proveedores](assets/direccion.png)

![Vista del controller: cumplimiento de objetivos y puente del resultado presupuestado al real](assets/controller.png)

![Vista de contabilidad: las veinte comprobaciones del libro diario, primero las que tienen aviso](assets/contabilidad.png)

## Cómo se comprueba cada cifra

Las cifras salen de un programa de análisis que lee el libro diario en MySQL. Casi todas se han vuelto a calcular con
una consulta SQL escrita aparte, con el mismo resultado al céntimo. Las pocas que no tienen un segundo cálculo lo
indican en su informe. Los [informes](informes/README.md) explican, análisis por análisis, la pregunta, la fórmula, la
cifra, su comprobación y en qué casos la cifra puede llevar a error.

```mermaid
flowchart LR
    D[(Libro diario<br/>en MySQL)] --> P[Programa de<br/>análisis en Python]
    D --> S[Segundo cálculo<br/>con SQL aparte]
    P --> C{¿Coinciden<br/>al céntimo?}
    S --> C
    C -->|Sí| F[Ficheros CSV<br/>de datos/]
    C -->|No| X[No se publica]
    F --> W[Web]
    F --> B[Power BI]
    F --> G[comprobar.py<br/>en cada cambio]
    style F fill:#e8f5e9,stroke:#2e7d32,color:#1b5e20
    style X fill:#ffebee,stroke:#c62828,color:#b71c1c
```

En cada cambio que se sube, GitHub ejecuta [`comprobar.py`](comprobar.py): los ficheros que leen la web y Power BI
existen y tienen filas, las cifras de esta portada salen de los ficheros de `datos/` y los enlaces llevan a ficheros que existen.

Una revisión externa, con consultas SQL propias, señaló 16 defectos en los datos y en el cálculo. El informe
[Lo que los datos no sostienen](informes/07_lo_que_los_datos_no_sostienen.md) los mide uno a uno con el mismo diario:
cuánto mueve cada uno las cifras publicadas y qué haría falta para corregirlo. Catorce se confirman y dos se corrigen
en parte.

## Power BI

[`powerbi/contabilidad_gestion.pbip`](powerbi/contabilidad_gestion.pbip) es un proyecto de Power BI con las tres vistas
de la web y una cuarta, «Cuentas y Pareto». Sus tablas leen los 21 ficheros de `datos/`, los mismos que la web, así que
las dos muestran las mismas cifras. Se abre con Power BI Desktop y se actualiza con «Actualizar». El modelo tiene una
tabla de hechos con el real y el presupuesto de cada cuenta de resultado por mes. Se relaciona con
una tabla de cuentas y con una tabla de fechas hecha en DAX. Sobre ese modelo, las medidas calculan:

- el resultado acumulado del año mes a mes, que a 31 de julio da el mismo resultado que los estados financieros;
- el gasto de las cuentas sin presupuesto;
- el gasto frente a un presupuesto flexible, que ajusta a las ventas reales solo el gasto variable;
- un Pareto de clientes y proveedores con clases ABC, que la página pone al lado de las del fichero para que se vea que
  coinciden.

El código de cada medida, con la cifra que da y los fallos que se corrigieron, está en
[`powerbi/MEDIDAS.md`](powerbi/MEDIDAS.md).

## Qué hay en el repositorio

| Fichero | Qué es |
|---|---|
| `index.html`, `cuadro.js`, `estilo.css` | la web de los tres cuadros de mando |
| [`datos/`](datos/) | los 21 ficheros CSV que leen la web y Power BI, con `metadatos.json` (periodo que cubre cada uno) |
| [`informes/`](informes/) | seis informes por bloque, con el método y la comprobación de cada cifra, y uno con lo que los datos no sostienen |
| [`powerbi/`](powerbi/) | el proyecto de Power BI y [`MEDIDAS.md`](powerbi/MEDIDAS.md), con sus medidas DAX |
| [`comprobar.py`](comprobar.py), [`test_comprobar.py`](test_comprobar.py) | las comprobaciones que ejecuta GitHub en cada cambio y sus pruebas |
| [`assets/`](assets/) | las imágenes de las tres vistas |

## Límites

- Se publica solo el ejercicio 2026, de enero a julio. Los años de 2023 a 2025 salen de datos generados en los que las
  compras no siguen a las ventas: sus márgenes no son los de una pyme real. El segundo cálculo los sigue comprobando,
  pero no se publican.
- 2026 es un ejercicio incompleto: sus cifras son de siete meses y no se comparan con un año entero.
- El segundo cálculo se hizo sobre la base de datos MySQL del proyecto, que no se publica. El repositorio incluye los
  resultados ya calculados. Como el libro diario completo se queda en esa base, la comprobación no se puede repetir
  desde aquí.
- El EBITDA no se publica: dos cálculos del proyecto lo definen de forma diferente y dan cifras distintas.
- Junio y julio aportan el 79,20 % del resultado de los siete meses, con un volumen de ventas que el diario no
  explica. El resultado es antes de impuestos, porque el diario no registra el Impuesto sobre Sociedades. Las
  existencias solo se recuentan a fin de año. El detalle está en
  [Lo que los datos no sostienen](informes/07_lo_que_los_datos_no_sostienen.md).

## Repositorios relacionados

- [tesoreria-forecast-ia](https://github.com/jleonceo/tesoreria-forecast-ia): previsión de caja mes a mes, con su
  error medido sobre datos históricos.
- [control-interno-fraude-ia](https://github.com/jleonceo/control-interno-fraude-ia): detección de fraude contable
  en un libro de asientos.
- [accounting-agent-swarm](https://github.com/jleonceo/accounting-agent-swarm): agentes de IA que contabilizan los
  asientos de esta misma empresa.

---

*Parte del portfolio de [Juan Luis León](https://github.com/jleonceo) · [juanluisleon.vercel.app](https://juanluisleon.vercel.app) · Licencia [MIT](LICENSE)*
