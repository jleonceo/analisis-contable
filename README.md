English version: [README.en.md](README.en.md)

# Análisis financiero con Python · TechAcces SL 2024

Levanta la cuenta de resultados y el movimiento del banco de una empresa a partir de su libro diario, y comprueba
las dos cifras por un camino independiente.

**Resultado:** el ejercicio 2024 cierra con 592.245,36 € de beneficio, sobre 1.420.269,26 € de ventas. La cifra
coincide al céntimo con el asiento de cierre, que sale de otra tabla.

```bash
pip install -r requirements.txt
jupyter notebook analisis_contable.ipynb
```

TechAcces SL es una empresa ficticia, con su contabilidad generada para el proyecto. Los datos van en `datos/`.

## Qué calcula

| Concepto | 2024 |
|---|---|
| Líneas del libro diario | 4.710, en 1.743 asientos |
| Debe y haber | 5.536.643,47 € cada uno, sin descuadre |
| Ventas | 1.420.269,26 € |
| Margen bruto | 884.998,05 €, el 62,3 % |
| EBITDA | 609.005,36 €, el 42,9 % |
| Resultado del ejercicio | 592.245,36 € |
| Flujo neto del banco | 739.034,45 €, con 2 meses de 12 en negativo |

El **EBITDA** es el beneficio de la actividad antes de amortizaciones, intereses e impuestos.

## Cómo funciona

1. Lee las líneas del libro diario de 2024: fecha, asiento, cuenta, debe y haber.
2. Clasifica cada línea por la familia de su cuenta en el Plan General Contable: 700 ventas, 600 compras, 640
   sueldos, 572 bancos, y así con las demás.
3. Monta la cuenta de resultados de las ventas al resultado.
4. Agrupa los movimientos del banco por mes.

Tres decisiones de clasificación cambian el resultado y están en el código:
- el coste de las ventas incluye la variación de existencias, no solo las compras;
- de la cuota del préstamo, solo el interés es gasto; la devolución del principal cancela deuda y no resta del
  resultado;
- la cuenta del banco es de activo: el dinero que entra va al debe y el que sale, al haber.

## Las dos comprobaciones

Comprobar una cifra contra el mismo cálculo que la produjo no demuestra nada, así que el cuaderno llega a cada
resultado por un segundo camino:
- el resultado del ejercicio, sumado desde el libro diario, coincide con el asiento de cierre, que vive en otra tabla:
  diferencia de 0,00 €;
- el flujo acumulado del banco en el año coincide con el saldo de la cuenta. Si no coincidiera, el cuaderno se
  detiene con un error en lugar de seguir.

## Límites

- Los datos son de una empresa inventada. Sirven para enseñar el método; las conclusiones de negocio no aplican a
  ninguna empresa real.
- Mira un solo ejercicio y dos igualdades contables. No es una auditoría.
- Los datos de `datos/` son una extracción de la base del proyecto con solo las columnas que usa el cuaderno.

## Ficheros

| Fichero | Qué contiene |
|---|---|
| `analisis_contable.ipynb` | el análisis, ya ejecutado |
| `construir_notebook.py` | el programa que genera el cuaderno |
| `datos/diario_2024.csv` | el libro diario de 2024 |
| `datos/cierre_resultado_2024.csv` | el asiento de cierre que distribuye el resultado |
| `requirements.txt` | las bibliotecas necesarias |

## Repositorios relacionados

- [tesoreria-forecast-ia](https://github.com/jleonceo/tesoreria-forecast-ia): previsión de caja mes a mes, con su
  error medido contra el pasado.
- [control-interno-fraude-ia](https://github.com/jleonceo/control-interno-fraude-ia): detección de fraude contable
  en un libro de asientos.
- [accounting-agent-swarm](https://github.com/jleonceo/accounting-agent-swarm): agentes de IA que contabilizan sobre
  esta misma empresa.

---

*Parte del portfolio de [Juan Luis León](https://github.com/jleonceo) · [juanluisleon.vercel.app](https://juanluisleon.vercel.app) · Licencia [MIT](LICENSE)*
