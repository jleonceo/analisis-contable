Versión en español: [README.md](README.md)

# Financial analysis with Python · TechAcces SL 2024

Builds a company's income statement and bank movement from its general ledger, and checks both figures by an
independent route.

**Result:** the 2024 financial year closes with a profit of €592,245.36 on €1,420,269.26 of sales. The figure
matches to the cent the closing entry, which comes from another table.

```bash
pip install -r requirements.txt
jupyter notebook analisis_contable.ipynb
```

TechAcces SL is a fictional company whose books were generated for the project. The data is in `datos/`.

## What it calculates

| Item | 2024 |
|---|---|
| Ledger lines | 4,710, across 1,743 journal entries |
| Debit and credit | €5,536,643.47 each, fully balanced |
| Sales | €1,420,269.26 |
| Gross margin | €884,998.05, 62.3 % |
| EBITDA | €609,005.36, 42.9 % |
| Result for the year | €592,245.36 |
| Net bank flow | €739,034.45, with 2 of 12 months negative |

**EBITDA** is the profit from the business activity before depreciation, interest and tax.

## How it works

1. It reads the 2024 ledger lines: date, entry, account, debit and credit.
2. It classifies each line by its account family in the Spanish chart of accounts: 700 sales, 600 purchases, 640
   wages, 572 banks, and so on.
3. It builds the income statement from sales down to the result.
4. It groups the bank movements by month.

Three classification decisions change the result and are in the code:
- the cost of sales includes the change in inventory, not just purchases;
- of a loan instalment, only the interest is an expense; repaying the principal cancels debt and does not reduce
  the result;
- the bank account is an asset: money coming in goes to the debit side and money going out to the credit side.

## The two checks

Checking a figure against the same calculation that produced it proves nothing, so the notebook reaches each
result by a second route:
- the result for the year, added up from the ledger, matches the closing entry, which lives in another table:
  a €0.00 difference;
- the bank's cumulative flow over the year matches the account balance. If it did not, the notebook would stop with
  an error instead of carrying on.

## Limits

- The data belongs to an invented company. It teaches the method; its business conclusions apply to no real
  company.
- It looks at one financial year and two accounting identities. It is not an audit.
- The data in `datos/` is an extract of the project database with only the columns the notebook uses.

## Files

| File | What it holds |
|---|---|
| `analisis_contable.ipynb` | the analysis, already run |
| `construir_notebook.py` | the program that generates the notebook |
| `datos/diario_2024.csv` | the 2024 ledger |
| `datos/cierre_resultado_2024.csv` | the closing entry that allocates the result |
| `requirements.txt` | the libraries it needs |

## Related repositories

- [tesoreria-forecast-ia](https://github.com/jleonceo/tesoreria-forecast-ia): monthly cash forecasting, with its
  error measured against the past.
- [control-interno-fraude-ia](https://github.com/jleonceo/control-interno-fraude-ia): accounting fraud detection in
  a ledger.
- [accounting-agent-swarm](https://github.com/jleonceo/accounting-agent-swarm): AI agents doing the bookkeeping for
  this same company.

---

*Part of [Juan Luis León](https://github.com/jleonceo)'s portfolio · [juanluisleon.vercel.app](https://juanluisleon.vercel.app) · Licence [MIT](LICENSE)*
