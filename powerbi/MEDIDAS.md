# Medidas DAX del modelo

El modelo tiene una tabla de hechos, `h_real_presupuesto_mes`, con el real y el presupuesto de cada cuenta de resultado
por mes. Se relaciona con una tabla de cuentas (`m_cuentas`) y con una tabla de fechas hecha en DAX (`Calendario`).
Las demás tablas leen los CSV de `datos/` tal como llegan. Aquí van las medidas que trabajan sobre ese modelo y las
dos que se corrigieron. El código completo está en
[`_Medidas.tmdl`](contabilidad_gestion.SemanticModel/definition/tables/_Medidas.tmdl).

Las cifras son de enero a julio de 2026 y coinciden con una consulta SQL sobre el libro diario.

## La tabla de fechas

```dax
Calendario =
VAR Primero = MIN ( h_real_presupuesto_mes[fecha] )
VAR Ultimo = EOMONTH ( MAX ( h_real_presupuesto_mes[fecha] ), 0 )
RETURN
    SELECTCOLUMNS (
        CALENDAR ( DATE ( YEAR ( Primero ), 1, 1 ), Ultimo ),
        "Fecha", [Date],
        "Año", YEAR ( [Date] ),
        "MesNumero", MONTH ( [Date] ),
        "Mes", FORMAT ( [Date], "mmm", "es-ES" )
    )
```

Se marca como tabla de fechas. Se relaciona por la fecha de cada mes. Sin ella, `TOTALYTD` no tendría sobre qué
acumular.

## El resultado sale de la tabla de hechos

El real va en el sentido de la cuenta: un gasto y un ingreso, en positivo. La columna `signo` dice cómo entra cada
cuenta en el resultado, así que la medida no tiene que deducirlo del número de cuenta.

```dax
Resultado real por cuenta =
SUMX ( h_real_presupuesto_mes, h_real_presupuesto_mes[real] * h_real_presupuesto_mes[signo] )

Resultado real acumulado del año =
TOTALYTD ( [Resultado real por cuenta], Calendario[Fecha] )
```

De enero a julio da 406.707,28 €, el mismo resultado que los estados financieros.

## Real frente a presupuesto sin mezclar ingresos y gastos

Sumar las ventas con los gastos da una cifra sin sentido, que no es el resultado. Por eso el real y el presupuesto
quedan vacíos cuando el contexto tiene ingresos y gastos a la vez:

```dax
Real =
VAR Naturalezas = CALCULATE ( DISTINCTCOUNT ( m_cuentas[naturaleza] ), h_real_presupuesto_mes )
RETURN
    IF ( Naturalezas = 1, SUM ( h_real_presupuesto_mes[real] ) )
```

`Presupuesto` sigue la misma regla. El recuento mira las filas visibles de la tabla de hechos, así que funciona también
cuando el filtro llega por la cuenta y no por la naturaleza. Por naturaleza, el gasto real es de 1.427.905,56 € frente a
1.354.774,27 € presupuestados, un 105,4 %. Los ingresos reales son de 1.834.612,84 € frente a 1.831.567,15 €, un 100,2 %.

La división tampoco puede fallar:

```dax
Cumplimiento del presupuesto % =
DIVIDE ( [Real], [Presupuesto] ) * 100
```

Una cuenta sin presupuesto da vacío en lugar de un error. Por eso la medida siguiente puede separar esas cuentas:

```dax
Gasto sin presupuesto =
VAR SinPresupuesto =
    FILTER (
        VALUES ( h_real_presupuesto_mes[cuenta] ),
        ISBLANK ( CALCULATE ( SUM ( h_real_presupuesto_mes[presupuesto] ), ALL ( Calendario ) ) )
    )
RETURN
    CALCULATE (
        SUMX ( h_real_presupuesto_mes, - h_real_presupuesto_mes[real] * h_real_presupuesto_mes[signo] ),
        KEEPFILTERS ( SinPresupuesto )
    )
```

Da 73.690,68 €: es la mayor parte de los 70.085,60 € en que el resultado se queda por debajo del presupuestado. El
`ALL ( Calendario )` hace que una cuenta cuente como «sin presupuesto» solo si no lo tiene en ningún mes, aunque se mire
un mes suelto.

## Presupuesto flexible

El objetivo de gasto de julio era de 456.332,56 € y el gasto real fue de 508.112,59 €, un 111,35 %. Pero las ventas
también subieron, al 111,11 % de su objetivo. El presupuesto flexible ajusta el objetivo de gasto a lo que se vendió de
verdad. Solo se ajusta el gasto que sube con las ventas. La regla de la empresa lo separa por cuenta: son variables
las compras (60 y 61), los transportes (624), los servicios bancarios (626) y las pérdidas por clientes (650 y 694).
Lo demás es fijo, salvo los gastos financieros (66), que quedan fuera. Es la misma regla del punto muerto. La tabla de
cuentas la lleva en la columna `comportamiento`.

```dax
Gasto con presupuesto flexible =
SUMX (
    VALUES ( h_real_presupuesto_mes[fecha] ),
    VAR Ventas =
        DIVIDE (
            CALCULATE ( SUM ( h_real_presupuesto_mes[real] ), ALL ( m_cuentas ), m_cuentas[naturaleza] = "ingreso" ),
            CALCULATE ( SUM ( h_real_presupuesto_mes[presupuesto] ), ALL ( m_cuentas ), m_cuentas[naturaleza] = "ingreso" )
        )
    VAR Variable = CALCULATE ( SUM ( h_real_presupuesto_mes[presupuesto] ), KEEPFILTERS ( m_cuentas[comportamiento] = "variable" ) )
    VAR Resto =
        CALCULATE (
            SUM ( h_real_presupuesto_mes[presupuesto] ),
            KEEPFILTERS ( m_cuentas[naturaleza] = "gasto" ),
            KEEPFILTERS ( m_cuentas[comportamiento] <> "variable" )
        )
    RETURN
        Variable * Ventas + Resto
)
```

El ajuste se hace mes a mes, porque cada mes tiene su propia relación entre ventas reales y presupuestadas. En julio,
con las ventas por encima, el gasto supera el objetivo ajustado en 7.286,54 €, un 1,45 %. En los siete meses lo supera
en 59.722,89 €, un 4,37 %, que incluye los 73.690,68 € de gasto sin presupuesto.

La versión anterior trataba todo el gasto como variable y daba 70.878,45 €. Separar el fijo no sube siempre la
desviación. En los meses de ventas por debajo del objetivo, el gasto fijo no baja con ellas y el objetivo ajustado
queda más alto.

## Pareto con clases ABC

Clientes y proveedores van por posición, sin su cuenta. Las tres medidas trabajan dentro de cada lado.

```dax
Posición en el Pareto =
VAR Lado = SELECTEDVALUE ( d_pareto_terceros[lado] )
RETURN
    IF (
        HASONEVALUE ( d_pareto_terceros[posicion] ) && NOT ISBLANK ( Lado ),
        RANKX ( FILTER ( ALL ( d_pareto_terceros ), d_pareto_terceros[lado] = Lado ),
                d_pareto_terceros[importe], [Importe del tercero], DESC, SKIP )
    )

Acumulado del Pareto % =
VAR Lado = SELECTEDVALUE ( d_pareto_terceros[lado] )
VAR Importe = [Importe del tercero]
VAR Todos = FILTER ( ALL ( d_pareto_terceros ), d_pareto_terceros[lado] = Lado )
RETURN
    IF (
        HASONEVALUE ( d_pareto_terceros[posicion] ) && NOT ISBLANK ( Lado ),
        DIVIDE ( SUMX ( FILTER ( Todos, d_pareto_terceros[importe] >= Importe ), d_pareto_terceros[importe] ),
                 SUMX ( Todos, d_pareto_terceros[importe] ) ) * 100
    )

Clase ABC =
VAR Lado = SELECTEDVALUE ( d_pareto_terceros[lado] )
VAR Total = SUMX ( FILTER ( ALL ( d_pareto_terceros ), d_pareto_terceros[lado] = Lado ), d_pareto_terceros[importe] )
VAR Previo = [Acumulado del Pareto %] - DIVIDE ( [Importe del tercero], Total ) * 100
RETURN
    IF ( NOT ISBLANK ( [Acumulado del Pareto %] ), IF ( Previo < 80, "A", IF ( Previo < 95, "B", "C" ) ) )
```

Un tercero es A mientras lo que va delante de él no llega al 80 % del total. Es B mientras no llega al 95 %. Así el que
alcanza un corte entra en esa clase. Para llegar al 80 % de lo facturado hacen falta 13 de los 18 clientes. En los
proveedores, 8 de 12. La página «Cuentas y Pareto» pone la clase de la medida al lado de la del fichero, para que se vea que
coinciden.

## Las dos medidas corregidas

Las dos promediaban porcentajes. Eso falla. Una media de porcentajes no pondera cada mes por su tamaño, así que un mes de pocas ventas pesa lo mismo que uno de muchas.

```dax
Margen bruto mensual % =
VAR Ventas = SUM ( d_margen_bruto_mensual[ventas] )
RETURN
    DIVIDE ( Ventas - SUM ( d_margen_bruto_mensual[aprovisionamientos] ), Ventas ) * 100

Margen bruto medio % =
CALCULATE ( [Margen bruto mensual %], ALL ( d_margen_bruto_mensual ) )
```

El margen de los siete meses es del 42,02 %. La media de los siete porcentajes mensuales, que es lo que daba la medida
anterior, es del 41,97 %.

```dax
Cumplimiento % =
VAR Filas =
    FILTER (
        c_objetivos,
        c_objetivos[indicador] <> "Margen_Bruto_Pct"
            && ( HASONEVALUE ( c_objetivos[periodo] ) || NOT CONTAINSSTRING ( c_objetivos[periodo], " a " ) )
    )
RETURN
    DIVIDE ( SUMX ( Filas, c_objetivos[real] ), SUMX ( Filas, c_objetivos[objetivo] ) ) * 100
```

Antes hacía la media de los cumplimientos y mezclaba meses, acumulado y margen. El margen sale ahora en puntos, real
menos objetivo: en mayo, 7,77 puntos por encima, en lugar de un cumplimiento del 124,53 %.

## Una columna por mes con formato dinámico

La matriz de objetivos ponía dos medidas por mes: el cumplimiento y los puntos de margen. En cada fila, una de las dos
salía vacía. Con siete meses y el acumulado eran dieciséis columnas, así que junio y julio quedaban fuera de la vista.
Ahora hay una sola medida. Su formato cambia según la fila:

```dax
Cumplimiento o margen =
IF (
    SELECTEDVALUE ( c_objetivos[indicador] ) = "Margen_Bruto_Pct",
    [Desviación del margen (puntos)],
    [Cumplimiento %]
)

-- cadena de formato dinámica de la misma medida
IF ( SELECTEDVALUE ( c_objetivos[indicador] ) = "Margen_Bruto_Pct", "+0.00 \p\t\o\s;-0.00 \p\t\o\s;0.00 \p\t\o\s", "0.0 \%" )
```

Al juntarlas apareció un fallo de la medida del margen. En los meses sin real, de agosto a diciembre, daba el objetivo
en negativo: de −36,97 a −42,51 puntos. Ahora devuelve vacío si el mes no tiene real.
