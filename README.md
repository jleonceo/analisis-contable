# Análisis financiero con Python · TechAcces SL 2024

**Juan Luis León Rodríguez · Proyecto TechAcces · cuaderno reconstruido el 20/07/2026**

[Español](#español) · [English](#english)

## Español

### Para qué sirve

Una empresa vende bien, sus productos dejan margen holgado y el año cierra en pérdidas. ¿Dónde se ha
ido el dinero? La respuesta está escrita en el libro diario, que es el registro donde queda anotado
cada movimiento de dinero de la empresa, línea a línea y por orden de fecha. Contestar recorriendo
4.710 líneas a mano no es trabajo de una tarde, y ahí es donde entra un programa.

Este repositorio contiene uno. Se conecta a la base de datos donde vive el libro diario de
TechAcces SL, una empresa ficticia simulada para el proyecto, toma el ejercicio 2024 y clasifica
cada línea por el número de cuenta al que pertenece. Con eso levanta la cuenta de resultados, que es
el resumen que baja desde las ventas hasta el beneficio del año, reconstruye el movimiento del banco
mes a mes y ejecuta dos comprobaciones que tienen que salir exactas.

Conviene fijar tres palabras del oficio antes de seguir. Toda operación se anota en dos columnas
llamadas **debe** y **haber**, y al conjunto de líneas de una misma operación se le llama
**asiento**; si las dos columnas no suman igual, hay algo mal escrito. El **EBITDA** es el beneficio
que deja la actividad antes de restarle amortizaciones, intereses e impuestos.

### El caso y el error que lo hace interesante

En mayo de 2026 la primera versión de este cuaderno contestó a la pregunta de arriba y contestó mal.
Dijo que la empresa perdía 57.742 € al año, que el culpable era el préstamo, que la tesorería
llevaba once de doce meses en negativo y que la salida pasaba por refinanciar la deuda. Ninguna de
esas cuatro afirmaciones se sostiene con los datos delante.

Los números de partida estaban bien sumados. Falló la clasificación, que es la parte de oficio:
saber qué cuenta es un gasto, qué cuenta es una devolución de deuda y por qué lado entra el dinero
cuando llega al banco. Tres decisiones tomadas de oído bastaron para que el análisis entero apuntara
al revés.

**El préstamo.** Cuando se paga la cuota salen del banco dos cosas que conviene no mezclar. El
interés es lo que cuesta el dinero prestado, resta del resultado del año y es gasto de pleno
derecho. El principal es dinero propio devuelto, así que cancela una deuda, cambia la foto del
patrimonio y deja el resultado donde estaba. Aquella versión restó las dos partidas por igual. En
2024 la empresa devolvió 19.200 € de principal y pagó 2.760 € de intereses, de modo que el 87,4 % de
lo que se contó como coste del préstamo no costaba nada. De ahí salían las pérdidas y de ahí salía
la recomendación de refinanciar.

**El signo del banco.** La cuenta 572 recoge el dinero en bancos y es una cuenta de activo, lo que
significa que se anota en el debe cuando entra dinero y en el haber cuando sale. El programa lo tomó
al revés. Con ese cambio de signo, un año de superávit pasó a leerse como un déficit de once meses,
y encima se escribieron cuatro causas para explicar un problema que no existía.

**El margen bruto.** El coste de las ventas se calculaba solo con las compras, sin la variación de
existencias, que es lo que sube o baja el almacén a lo largo del año. Salía un margen del 91,7 %, o
sea un coste de producto del 8 % en un comercio electrónico que compra mercancía y la revende. Esa
magnitud es imposible en ese negocio y nadie se paró a mirarla.

### Qué sale hoy

Antes de la tabla, un aviso que importa: estas cifras no corrigen a las de mayo. La tabla que leía
el cuaderno original (`libro_diario_v2`) se retiró de la base de datos, y el contenido de 2024 en la
base viva es otro, 4.710 líneas frente a las 4.006 de entonces. Son otro cálculo sobre otros datos,
de manera que ponerlas una al lado de la otra sería comparar cosas distintas, que es justo uno de
los errores que esta reconstrucción viene a arreglar.

Medido el 22 de julio de 2026, repitiendo consulta a consulta cada cálculo del cuaderno contra la
misma base de datos y con los criterios exactos de su código:

| Comprobación | Resultado |
|---|---|
| Líneas del ejercicio 2024 | 4.710, en 1.743 asientos |
| Debe y haber | 5.536.643,47 € cada uno, descuadre 0,00 € |
| Ventas | 1.420.269,26 € |
| Margen bruto | 884.998,05 €, el 62,3 % |
| EBITDA | 609.005,36 €, el 42,9 % |
| Resultado del ejercicio | 592.245,36 €, de beneficio |
| El mismo resultado según el asiento de cierre | 592.245,36 €, diferencia 0,00 € |
| Flujo del banco en el año | 739.034,45 €, igual al saldo de la cuenta |
| Meses con salida neta de dinero | 2 de 12, enero y julio |

### Las dos comprobaciones

Comprobar una cifra volviendo a mirar de dónde salió no comprueba nada, porque un cálculo mal hecho
de forma coherente cuadra siempre consigo mismo. La comprobación honrada consiste en llegar al mismo
número por otro camino y desde otro sitio. Aquí se hace dos veces.

El resultado del ejercicio se obtiene sumando el diario de movimientos y se contrasta contra el
asiento de cierre, que vive en otra tabla y lo escribió otro proceso en otro momento; los dos dan
592.245,36 € con diferencia de cero. Después, el dinero que entró y salió del banco mes a mes tiene
que sumar exactamente el saldo de la cuenta bancaria, que son 739.034,45 €. Esa segunda igualdad no
admite umbrales ni interpretación, y es la que habría cazado el error de los signos el primer día,
porque con las entradas y las salidas cambiadas daba −739.034,45 € frente a +739.034,45 €. Cuando
falla, el cuaderno se detiene con un aviso en lugar de seguir imprimiendo conclusiones.

### Cómo funciona por dentro

1. **Credenciales.** Lee un fichero `.env` con el usuario y la contraseña de la base de datos,
   fichero que no se publica jamás.
2. **Consulta.** Pide al diario operativo todas las líneas contables del ejercicio.
3. **Clasificación.** Los números de cuenta van por familias, y empiezan por 700 las ventas, por 600
   las compras, por 572 el banco y por 640 los sueldos. El programa suma por esa primera parte del
   número y levanta la cuenta de resultados de arriba abajo, sin que nadie tenga que decirle a mano
   qué es cada una de las 4.710 líneas.
4. **Contraste.** Va a la tabla de cierre y compara el resultado.
5. **Tesorería.** Agrupa los movimientos del banco por mes y comprueba la igualdad del saldo.

Hay una decisión de método que conviene señalar, porque es la que evita que todo esto vuelva a
pasar. Este cuaderno no se edita a mano: lo reescribe entero `construir_notebook.py`. Un documento
que se toca a mano se queda viejo en silencio, mientras que uno que se regenera cuesta un comando y
no puede desincronizarse de los datos que dice resumir.

### Qué falta y qué no cuadra todavía

La reconstrucción del 20/07 se quedó con lo que podía verificar, o sea la cuenta de resultados, la
tesorería y las dos igualdades. El análisis por trimestres, los gráficos, el simulador de cuatro
escenarios y la exportación a Excel que traía la versión de mayo no se rehicieron.

- El Excel `Informe_Financiero_TechAcces_2024.xlsx` sigue siendo el de mayo, y repite en su primera
  pestaña las cifras que el cuaderno actual desmiente dos ficheros más allá.
- El fichero `analisis_contable.html`, que existe para leer los resultados sin instalar nada, se
  exportó del cuaderno nuevo antes de ejecutarlo, así que hoy no muestra ningún resultado.
- Ejecutar el cuaderno pide una base MySQL propia y un fichero de credenciales que el repositorio no
  trae ni debe traer. Sin eso se puede leer, pero no ejecutar.

### Cuándo no sirve

Los datos son de una empresa inventada, generada para el proyecto. Valen para aprender el método, y
cualquier conclusión de negocio que se saque de ellos es literatura.

Son además cifras de un día concreto, porque la base de datos sigue creciendo por debajo. Quien
quiera reproducirlas tendrá que regenerar el cuaderno y aceptar de antemano que le salgan otras.

Tampoco es una herramienta de auditoría, ni pretende serlo. Mira un solo ejercicio, un puñado de
familias de cuentas y dos igualdades, cuando un cierre de verdad lleva muchas más.

### Estructura del proyecto

```
analisis-contable/
├── construir_notebook.py                   # El generador. Su cabecera cuenta qué estaba mal y por qué
├── analisis_contable.ipynb                 # El cuaderno, regenerado desde la base viva
├── analisis_contable.html                  # El cuaderno para el navegador, exportado sin ejecutar
├── Informe_Financiero_TechAcces_2024.xlsx  # El Excel de mayo, con las cifras viejas
├── requirements.txt                        # Dependencias
├── .env.example                            # Plantilla de credenciales
└── README.md                               # Este archivo
```

### Herramientas

| Herramienta | Para qué se usa aquí |
|---|---|
| **Python + pandas** | Agrupar las líneas contables y montar las tablas |
| **SQLAlchemy + PyMySQL** | Leer la base de datos sin ficheros intermedios |
| **MySQL** | Donde vive el libro diario de la empresa simulada |
| **Jupyter** | El formato del cuaderno, con texto y programa en el mismo documento |

### Cómo ejecutar

1. Clona el repositorio.
2. Copia `.env.example` a `.env` y rellena tus credenciales de MySQL:

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

4. Regenera el cuaderno desde tu base de datos y ábrelo:

```bash
python construir_notebook.py
jupyter notebook analisis_contable.ipynb
```

### Repos relacionados

Este análisis es una pieza de un portfolio de casos de analítica. Las piezas hermanas:

- [lead-scoring-ml](https://github.com/jleonceo/lead-scoring-ml): predecir qué lead acaba comprando, con modelos de clasificación.
- [RFM-Customer-Analytics](https://github.com/jleonceo/RFM-Customer-Analytics): segmentación de clientes por recencia, frecuencia e importe.
- [accident-intelligent-agent](https://github.com/jleonceo/accident-intelligent-agent): ETL, exploración y modelo para predecir la gravedad de un accidente de tráfico.
- [accounting-agent-swarm](https://github.com/jleonceo/accounting-agent-swarm): el enjambre de agentes que contabiliza sobre esta misma empresa simulada.

*Parte del portfolio de [Juan Luis León](https://github.com/jleonceo) · [juanluisleon.vercel.app](https://juanluisleon.vercel.app) · Licencia [MIT](LICENSE)*

## English

### What it is for

A company sells well, its products leave a comfortable margin and the year still closes at a loss.
Where did the money go? The answer is written in the general ledger, which is the record where every
movement of money is noted down line by line and in date order. Answering by walking through 4,710
lines by hand is not an afternoon's work. That is where a program earns its keep.

This repository holds one. It connects to the database where the ledger of TechAcces SL lives, a
fictional company simulated for the project, takes the 2024 financial year and sorts every line by
the account number it belongs to. From there it builds the income statement, which is the summary
running from sales down to the profit for the year, reconstructs the bank movement month by month
and runs two checks that have to come out exact.

Three words of the trade are worth pinning down first. Every transaction is written in two columns,
called *debe* and *haber* in Spanish books and debit and credit in English ones, and the set of
lines belonging to one transaction is an *asiento*, a journal entry; if the two columns do not add
up to the same figure, something was written wrong. **EBITDA** is the profit the business activity
leaves before subtracting depreciation, interest and tax.

### The case and the mistake that makes it worth reading

In May 2026 the first version of this notebook answered the question above, and answered it wrong.
It said the company was losing 57,742 € a year, that the loan was to blame, that cash flow had been
negative for eleven of twelve months and that the way out was refinancing the debt. None of those
four statements holds up against the data.

The underlying figures added up correctly. What failed was the classification, which is the part
that takes trade knowledge: which account is an expense, which account is a repayment of debt, and
which side the money enters on when it reaches the bank. Three decisions taken by ear were enough to
point the whole analysis backwards.

**The loan.** Paying an instalment takes two different things out of the bank, and mixing them is
expensive. Interest is what the borrowed money costs, it reduces the result for the year and it is
an expense in its own right. Principal is your own money handed back, so it cancels a debt, changes
the shape of the balance sheet and leaves the result where it was. That version subtracted both
alike. In 2024 the company repaid 19,200 € of principal and paid 2,760 € of interest, so 87.4% of
what was counted as the cost of the loan cost nothing at all. That is where the losses came from,
and where the advice to refinance came from.

**The sign on the bank account.** Account 572 holds the money in banks and is an asset account,
which means it is debited when money comes in and credited when money goes out. The program had it
the other way round. With the sign reversed, a year in surplus read as an eleven-month deficit, and
four causes were then written up to explain a problem that did not exist.

**Gross margin.** The cost of sales was worked out from purchases alone, leaving out the change in
inventory, which is what the warehouse gains or loses over the year. The margin came out at 91.7%,
that is, a product cost of 8% in an online shop that buys goods and resells them. That magnitude is
impossible in such a business and nobody stopped to look at it.

### What comes out today

One warning before the table: these figures do not correct May's. The table the original notebook
read (`libro_diario_v2`) was retired from the database, and the 2024 content in the live database is
different, 4,710 lines against the 4,006 of that day. They are another calculation over other data,
so setting them side by side would compare two different things, which is one of the very errors
this reconstruction sets out to fix.

Measured on 22 July 2026 by repeating every calculation of the notebook, query by query, against the
same database and with the exact criteria of its code:

| Check | Result |
|---|---|
| Lines in the 2024 financial year | 4,710, across 1,743 journal entries |
| Debit and credit | 5,536,643.47 € each, 0.00 € out of balance |
| Sales | 1,420,269.26 € |
| Gross margin | 884,998.05 €, 62.3% |
| EBITDA | 609,005.36 €, 42.9% |
| Result for the year | 592,245.36 €, a profit |
| The same result per the closing entry | 592,245.36 €, 0.00 € difference |
| Bank flow over the year | 739,034.45 €, equal to the account balance |
| Months with net cash outflow | 2 of 12, January and July |

### The two checks

Checking a figure by looking again at where it came from checks nothing, because a calculation that
is wrong in a consistent way always agrees with itself. An honest check reaches the same number by
another route and from somewhere else. Here it is done twice.

The result for the year comes from adding up the operating journal and is contrasted against the
closing entry, which lives in another table and was written by another process at another time; both
give 592,245.36 € with zero difference. Then the money that came into and left the bank month by
month has to add up to exactly the balance of the bank account, 739,034.45 €. That second equality
admits no thresholds and no interpretation. It is the one that would have caught the sign error on
day one, because with inflows and outflows swapped it gave −739,034.45 € against +739,034.45 €.
When it fails, the notebook stops with a warning instead of carrying on printing conclusions.

### How it works inside

1. **Credentials.** It reads a `.env` file with the database user and password, a file that is never
   published.
2. **Query.** It asks the operating journal for every accounting line of the year.
3. **Classification.** Account numbers run in families: sales start with 700, purchases with 600, the
   bank with 572 and wages with 640. The program adds up by that first part of the number and builds
   the income statement from the top down, without anyone having to say by hand what each of the
   4,710 lines is.
4. **Contrast.** It goes to the closing table and compares the result.
5. **Cash.** It groups bank movements by month and checks the balance identity.

One decision of method is worth flagging, because it is what keeps this from happening again. The
notebook is not edited by hand: `construir_notebook.py` rewrites it whole. A document touched by
hand goes stale in silence, whereas one that is regenerated costs a single command and cannot drift
away from the data it claims to summarise.

### What is missing and what still does not add up

The July reconstruction kept what it could verify, that is, the income statement, the cash movement
and the two identities. The quarterly analysis, the charts, the four-scenario simulator and the
Excel export that the May version carried were not rebuilt.

- The Excel file `Informe_Financiero_TechAcces_2024.xlsx` is still May's, and its first sheet repeats
  the figures that the current notebook contradicts two files away.
- The file `analisis_contable.html`, which exists so the results can be read without installing
  anything, was exported from the new notebook before running it, so today it shows no results at all.
- Running the notebook needs your own MySQL database and a credentials file that the repository does
  not carry and should not carry. Without that it can be read but not executed.

### When it does not apply

The data belongs to an invented company, generated for the project. It is good for learning the
method, and any business conclusion drawn from it is fiction.

They are also the figures of one particular day, because the database keeps growing underneath.
Anyone reproducing them will have to regenerate the notebook and accept in advance that different
numbers will come out.

This is not an audit tool either. It looks at one financial year, a handful of account families and
two identities, where a real year-end close carries many more.

### Project layout

```
analisis-contable/
├── construir_notebook.py                   # The generator. Its header tells what was wrong and why
├── analisis_contable.ipynb                 # The notebook, regenerated from the live database
├── analisis_contable.html                  # The notebook for the browser, exported without running
├── Informe_Financiero_TechAcces_2024.xlsx  # May's Excel, carrying the old figures
├── requirements.txt                        # Dependencies
├── .env.example                            # Credentials template
└── README.md                               # This file
```

### Tools

| Tool | What it does here |
|---|---|
| **Python + pandas** | Grouping the accounting lines and building the tables |
| **SQLAlchemy + PyMySQL** | Reading the database with no intermediate files |
| **MySQL** | Where the simulated company's ledger lives |
| **Jupyter** | The notebook format, text and program in one document |

### Running it

1. Clone the repository.
2. Copy `.env.example` to `.env` and fill in your MySQL credentials:

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

4. Regenerate the notebook from your database and open it:

```bash
python construir_notebook.py
jupyter notebook analisis_contable.ipynb
```

### Related repositories

This analysis is one piece of an analytics portfolio. Its sibling projects:

- [lead-scoring-ml](https://github.com/jleonceo/lead-scoring-ml): predicting which lead ends up buying, with classification models.
- [RFM-Customer-Analytics](https://github.com/jleonceo/RFM-Customer-Analytics): customer segmentation by recency, frequency and monetary value.
- [accident-intelligent-agent](https://github.com/jleonceo/accident-intelligent-agent): ETL, exploration and a model to predict how severe a road accident is.
- [accounting-agent-swarm](https://github.com/jleonceo/accounting-agent-swarm): the agent swarm that does the bookkeeping for this same simulated company.

*Part of [Juan Luis León](https://github.com/jleonceo)'s portfolio · [juanluisleon.vercel.app](https://juanluisleon.vercel.app) · [MIT](LICENSE) licence*
