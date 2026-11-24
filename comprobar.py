"""Comprueba que el repositorio cuenta lo mismo que sus datos.

Tres comprobaciones, solo con la biblioteca estándar de Python:

1. Los ficheros que lee la web (la lista FICHEROS de cuadro.js) y los que lee el modelo de
   Power BI (cada LeerCsv de sus tablas) existen en datos/ y tienen al menos una fila además
   de la cabecera.
2. Las cifras de la portada salen de los datos: las ventas y el resultado de 2026 de
   d_ventas_resultado.csv, y la diferencia entre el resultado presupuestado y el real de
   d_puente_presupuesto.csv. Tienen que aparecer, con su formato, en README.md (español)
   y en README.en.md (inglés).
3. Los enlaces e imágenes de los README y los recursos de index.html llevan a ficheros que
   existen. Los enlaces a otras webs no se comprueban.

Uso: python comprobar.py      (sale con 0 si todo está bien y con 1 si algo falla)
"""
import csv
import os
import re
import sys
from decimal import Decimal

RAIZ = os.path.dirname(os.path.abspath(__file__))
ANO = "2026"


def _leer(raiz, rel):
    with open(os.path.join(raiz, rel), encoding="utf-8") as f:
        return f.read()


def _filas(raiz, nombre):
    with open(os.path.join(raiz, "datos", nombre + ".csv"), encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def _es(importe):
    """1834612.84 -> 1.834.612,84"""
    return "{:,.2f}".format(importe).replace(",", "#").replace(".", ",").replace("#", ".")


def _en(importe):
    """1834612.84 -> 1,834,612.84"""
    return "{:,.2f}".format(importe)


def ficheros_de_la_web(raiz):
    m = re.search(r"const FICHEROS = \[([^\]]*)\]", _leer(raiz, "cuadro.js"))
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


TABLAS_POWER_BI = os.path.join("powerbi", "contabilidad_gestion.SemanticModel", "definition", "tables")


def ficheros_de_power_bi(raiz):
    carpeta = os.path.join(raiz, TABLAS_POWER_BI)
    nombres = []
    for fichero in sorted(os.listdir(carpeta)) if os.path.isdir(carpeta) else []:
        if fichero.endswith(".tmdl"):
            nombres += re.findall(r'LeerCsv\("([^"]+)\.csv"\)', _leer(carpeta, fichero))
    return nombres


def comprobar_datos(raiz):
    fallos = []
    web, power_bi = ficheros_de_la_web(raiz), ficheros_de_power_bi(raiz)
    if not web:
        return ["cuadro.js: no se encuentra la lista FICHEROS"]
    if not power_bi:
        return ["powerbi: ninguna tabla lee un CSV con LeerCsv"]
    for nombre in sorted(set(web) | set(power_bi)):
        ruta = os.path.join("datos", nombre + ".csv")
        if not os.path.isfile(os.path.join(raiz, ruta)):
            fallos.append(ruta + ": no existe")
        elif not _filas(raiz, nombre):
            fallos.append(ruta + ": no tiene filas")
    return fallos


def cifras_de_los_datos(raiz):
    ventas = [f for f in _filas(raiz, "d_ventas_resultado") if f["ano"] == ANO]
    puente = _filas(raiz, "d_puente_presupuesto")
    presupuestado = [f for f in puente if f["partida"] == "Resultado presupuestado"]
    real = [f for f in puente if f["partida"] == "Resultado real"]
    if len(ventas) != 1 or len(presupuestado) != 1 or len(real) != 1:
        return None
    return {
        "ventas de " + ANO: Decimal(ventas[0]["ventas"]),
        "resultado de " + ANO: Decimal(ventas[0]["resultado"]),
        "resultado presupuestado menos real": Decimal(presupuestado[0]["acumulado"])
        - Decimal(real[0]["acumulado"]),
    }


def comprobar_cifras(raiz):
    try:
        cifras = cifras_de_los_datos(raiz)
    except (OSError, KeyError) as exc:
        return ["cifras: no se pueden leer los datos (%s)" % exc]
    if cifras is None:
        return ["cifras: d_ventas_resultado.csv o d_puente_presupuesto.csv no tienen la fila esperada"]
    fallos = []
    for readme, formato in (("README.md", _es), ("README.en.md", _en)):
        texto = _leer(raiz, readme)
        for nombre, importe in cifras.items():
            if formato(importe) not in texto:
                fallos.append("%s: no dice %s (%s), que es lo que dan los datos"
                              % (readme, nombre, formato(importe)))
    return fallos


ENLACE_MD = re.compile(r"\]\(([^)\s]+)\)")
RECURSO_HTML = re.compile(r'(?:href|src)="([^"]+)"')


def _destinos(texto, patron):
    for destino in patron.findall(texto):
        if re.match(r"^[a-z][a-z0-9+.-]*:", destino, re.I) or destino.startswith(("#", "//")):
            continue  # otra web, correo o ancla de la misma página
        yield re.split(r"[?#]", destino)[0]


def comprobar_enlaces(raiz):
    fallos = []
    for fichero, patron in (("README.md", ENLACE_MD), ("README.en.md", ENLACE_MD),
                            ("index.html", RECURSO_HTML)):
        for destino in _destinos(_leer(raiz, fichero), patron):
            if destino and not os.path.exists(os.path.join(raiz, *destino.split("/"))):
                fallos.append("%s: enlaza %s, que no existe" % (fichero, destino))
    return fallos


def comprobar(raiz=RAIZ):
    return comprobar_datos(raiz) + comprobar_cifras(raiz) + comprobar_enlaces(raiz)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    fallos = comprobar()
    for fallo in fallos:
        print("FALLA  " + fallo)
    print("Comprobaciones: %s" % ("todo en orden" if not fallos else "%d fallo(s)" % len(fallos)))
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
