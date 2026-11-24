Versión en español: [README.md](README.md)

# Management accounting with data

Three dashboards built on a small business's general ledger: one for management, one for the controller and one for
accounting. Almost every figure is checked against an independent second calculation before it is published. The
company, TechAcces SL, is fictional: its books were generated for the project.

**Result:** from January to July 2026 the company sold €1,834,612.84 and earned €406,707.28 before tax, which is
€70,085.60 less than budgeted. Almost all of the gap comes from €73,690.68 of spending that had no budget.

**Tools:** SQL (MySQL), Python, Power BI (DAX and Power Query), HTML and JavaScript.

[![comprobaciones](https://github.com/jleonceo/management-accounting-analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/jleonceo/management-accounting-analytics/actions/workflows/ci.yml)

```bash
git clone https://github.com/jleonceo/management-accounting-analytics.git
cd management-accounting-analytics
python -m http.server
```

Then open `http://localhost:8000` in a browser. The Power BI version is in [`powerbi/`](powerbi/).

The dashboards and the reports are written in Spanish.

## The three views

| View | Question it answers | What it shows |
|---|---|---|
| Management | How is the company doing? | sales, result, gross margin and free cash flow from January to July and their month-by-month trend, and the Pareto of customers and suppliers; in Power BI, also the balance sheet at 31 July |
| Controller | Where does it deviate from the budget? | variance bridge by budget line, cost by cost centre and degree of target achievement |
| Accounting | Is the general ledger well kept? | twenty checks on the ledger, with what each one detects |

At 31/07/2026, nine of the twenty checks flag issues that need manual review, among them the unfunded legal reserve
and 2,273 unused journal entry numbers.

![Management view: sales, result, gross margin and free cash flow from January to July 2026, and the customer Pareto](assets/direccion.png)

![Controller view: target achievement and the bridge from budgeted to actual result](assets/controller.png)

![Accounting view: the twenty general ledger checks, those with a warning first](assets/contabilidad.png)

## How each figure is checked

The figures come from an analysis program that reads the general ledger in MySQL. Almost all of them have been
recalculated with a separately written SQL query, with the same result to the cent. The few without a second
calculation say so in their report. The [reports](informes/README.md) explain, analysis by analysis, the question, the
formula, the figure, how it was checked and when the figure can mislead.

On every change that is pushed, GitHub runs [`comprobar.py`](comprobar.py): the files the web page and Power BI read exist
and have rows, the figures on this page come from the files in `datos/`, and the links lead to files that exist.

An external review, with its own SQL queries, pointed out 16 defects in the data and the calculations. The report
[Lo que los datos no sostienen](informes/07_lo_que_los_datos_no_sostienen.md) (what the data does not support)
measures each one against the same ledger: how much it moves the published figures and what it would take to fix it.
Fourteen are confirmed and two are partly corrected.

## Power BI

[`powerbi/contabilidad_gestion.pbip`](powerbi/contabilidad_gestion.pbip) is a Power BI project with the three views of
the web page and a fourth one, «Cuentas y Pareto» (accounts and Pareto). Its tables read the 21 files in `datos/`, the
same ones as the web page, so both show the same figures. It opens in Power BI Desktop and updates with «Actualizar»
(Refresh).

The model has a fact table with the actual and budgeted amount of each income statement account by month. It is
related to an accounts table and to a date table built in DAX. On top of that model, the measures calculate:

- the year-to-date result month by month, which at 31 July gives the same result as the financial statements;
- the spending on accounts with no budget;
- spending against a flexible budget, which adjusts the spending target to actual sales;
- a Pareto of customers and suppliers with ABC classes, which the page shows next to those in the file so that they can
  be seen to match.

The code of each measure, with the figure it gives and the errors that were fixed, is in
[`powerbi/MEDIDAS.md`](powerbi/MEDIDAS.md) (in Spanish).

## What is in the repository

| File | What it is |
|---|---|
| `index.html`, `cuadro.js`, `estilo.css` | the web page with the three dashboards |
| [`datos/`](datos/) | the 21 CSV files read by the web page and Power BI, with `metadatos.json` (the period each one covers) |
| [`informes/`](informes/) | six reports by block, with the method and the check behind each figure, and one on what the data does not support |
| [`powerbi/`](powerbi/) | the Power BI project and [`MEDIDAS.md`](powerbi/MEDIDAS.md), with its DAX measures |
| [`comprobar.py`](comprobar.py), [`test_comprobar.py`](test_comprobar.py) | the checks GitHub runs on every change, and their tests |
| [`assets/`](assets/) | the images of the three views |

## Limits

- Only the 2026 financial year, January to July, is published. The years 2023 to 2025 come from generated data in
  which purchases do not follow sales: their margins are not those of a real small business. The second calculation
  still checks them, but they are not published.
- 2026 is an incomplete year: its figures cover seven months and are not compared with a full year.
- The second calculation ran on the project's MySQL database, which is not published. The repository includes the
  results already calculated. Since the full general ledger stays in that database, the check cannot be repeated from
  here.
- EBITDA is not published: two calculations in the project define it differently and give different figures.
- June and July bring 79.20% of the seven-month result, with a sales volume the ledger does not explain. The result
  is before tax, because the ledger does not record corporate income tax. Inventory is only counted at year end. The
  detail is in [Lo que los datos no sostienen](informes/07_lo_que_los_datos_no_sostienen.md).

## Related repositories

- [tesoreria-forecast-ia](https://github.com/jleonceo/tesoreria-forecast-ia): month-by-month cash forecasting, with
  its error measured on historical data.
- [control-interno-fraude-ia](https://github.com/jleonceo/control-interno-fraude-ia): accounting fraud detection in a
  ledger.
- [accounting-agent-swarm](https://github.com/jleonceo/accounting-agent-swarm): AI agents that post the journal
  entries of this same company.

---

*Part of [Juan Luis León](https://github.com/jleonceo)'s portfolio · [juanluisleon.vercel.app](https://juanluisleon.vercel.app) · Licence [MIT](LICENSE)*
