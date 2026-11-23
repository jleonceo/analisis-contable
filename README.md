English version: [README.en.md](README.en.md)

# Contabilidad de gestión con datos

Tres cuadros de mando sobre el libro diario de una pyme: uno para dirección, otro para el controller y otro para
contabilidad. Casi todas las cifras se comprueban con un segundo cálculo independiente antes de publicarse. La empresa, TechAcces
SL, es ficticia: su contabilidad se generó para el proyecto.

**Resultado:** de enero a julio de 2026 la empresa vendió 1.834.612,84 € y ganó 406.707,28 €, que son 70.085,60 € menos
de lo presupuestado. Tres partidas que parecían ahorrar 100.479,60 € tenían su gasto imputado a otro centro de coste.

**Herramientas:** SQL (MySQL), Python, Power BI (DAX y Power Query), HTML y JavaScript.

```bash
git clone https://github.com/jleonceo/management-accounting-analytics.git
cd management-accounting-analytics
python -m http.server
```

Después se abre `http://localhost:8000` en el navegador. La versión de Power BI está en [`powerbi/`](powerbi/).

## Las tres vistas

| Vista | Pregunta que contesta | Qué muestra |
|---|---|---|
| Dirección | ¿Cómo va la empresa? | ventas, resultado, margen bruto y flujo de caja libre de enero a julio, su evolución mensual y el balance a 31 de julio |
| Controller | ¿Dónde se desvía del presupuesto? | puente de desviaciones por partida, coste por centro y grado de cumplimiento de objetivos |
| Contabilidad | ¿Está bien llevado el libro diario? | veinte controles sobre el diario, con lo que detecta cada uno |

A 31/07/2026, nueve de los veinte controles señalan incidencias que requieren revisión manual, entre ellas la
reserva legal sin dotar y 2.273 números de asiento sin usar.

## Cómo se comprueba cada cifra

Las cifras salen de un programa de análisis que lee el libro diario en MySQL. Casi todas se han vuelto a calcular con
una consulta SQL escrita aparte, con el mismo resultado al céntimo. Las pocas que no tienen un segundo cálculo lo
indican en su informe. Los [informes](informes/README.md) explican, análisis por análisis, la pregunta, la fórmula, la
cifra, su comprobación y en qué casos la cifra puede llevar a error.

Una revisión independiente, con consultas SQL propias, detectó las tres partidas que se citan al principio. El puente
del presupuesto mostraba en ellas un gasto inferior al presupuestado: ese gasto estaba imputado a otro centro de coste.
El detalle está en [Presupuesto y coste por centro](informes/03_presupuesto_objetivos_y_centros.md).

## Power BI

[`powerbi/contabilidad_gestion.pbip`](powerbi/contabilidad_gestion.pbip) es un proyecto de Power BI con las mismas
tres vistas. Sus 19 tablas leen los mismos ficheros de `datos/` que la web, así que las dos muestran las mismas cifras.
Se abre con Power BI Desktop y se actualiza con «Actualizar».

## Qué hay en el repositorio

| Fichero | Qué es |
|---|---|
| `index.html`, `cuadro.js`, `estilo.css` | la web de los tres cuadros de mando |
| [`datos/`](datos/) | los 19 ficheros CSV que leen la web y Power BI, con `metadatos.json` (periodo que cubre cada uno) |
| [`informes/`](informes/) | seis informes por bloque, con el método y la comprobación de cada cifra |
| [`powerbi/`](powerbi/) | el proyecto de Power BI |

## Límites

- Se publica solo el ejercicio 2026, de enero a julio. Los años de 2023 a 2025 salen de datos generados en los que las
  compras no siguen a las ventas: sus márgenes no son los de una pyme real. El segundo cálculo los sigue comprobando,
  pero no se publican.
- 2026 es un ejercicio incompleto: sus cifras son de siete meses y no se comparan con un año entero.
- El segundo cálculo se hizo sobre la base de datos MySQL del proyecto, que no se publica. El repositorio incluye los
  resultados ya calculados. Como el libro diario completo se queda en esa base, la comprobación no se puede repetir
  desde aquí.
- El EBITDA no se publica: dos cálculos del proyecto lo definen de forma diferente y dan cifras distintas.

## Repositorios relacionados

- [tesoreria-forecast-ia](https://github.com/jleonceo/tesoreria-forecast-ia): previsión de caja mes a mes, con su
  error medido sobre datos históricos.
- [control-interno-fraude-ia](https://github.com/jleonceo/control-interno-fraude-ia): detección de fraude contable
  en un libro de asientos.
- [accounting-agent-swarm](https://github.com/jleonceo/accounting-agent-swarm): agentes de IA que contabilizan los
  asientos de esta misma empresa.

---

*Parte del portfolio de [Juan Luis León](https://github.com/jleonceo) · [juanluisleon.vercel.app](https://juanluisleon.vercel.app) · Licencia [MIT](LICENSE)*
