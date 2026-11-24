"""Pruebas de comprobar.py. Solo biblioteca estándar: python -m unittest test_comprobar -v

Cada caso copia el repositorio a una carpeta temporal, estropea una cosa y exige que
comprobar.py lo detecte. El primero comprueba que el repositorio tal como está pasa.
"""
import os
import shutil
import sys
import tempfile
import unittest

RAIZ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, RAIZ)

import comprobar  # noqa: E402


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="comprobar_")
        self.repo = os.path.join(self.tmp, "repo")
        shutil.copytree(RAIZ, self.repo, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def ruta(self, rel):
        return os.path.join(self.repo, *rel.split("/"))

    def cambia(self, rel, viejo, nuevo):
        with open(self.ruta(rel), encoding="utf-8") as f:
            texto = f.read()
        self.assertIn(viejo, texto, "el caso no encuentra lo que quiere estropear en " + rel)
        with open(self.ruta(rel), "w", encoding="utf-8", newline="") as f:
            f.write(texto.replace(viejo, nuevo, 1))

    def fallos(self):
        return comprobar.comprobar(self.repo)


class TestElRepositorioPasa(Base):
    def test_tal_como_esta_no_hay_fallos(self):
        self.assertEqual(self.fallos(), [])


class TestLosDatos(Base):
    def test_un_fichero_que_falta(self):
        # Uno que solo lee la web: si fuera el de ventas, la comprobación de cifras también lo
        # acusaría y este caso no probaría nada de la de datos.
        os.remove(self.ruta("datos/c_variaciones.csv"))
        self.assertTrue(any("c_variaciones" in f for f in self.fallos()))

    def test_un_fichero_que_solo_lee_power_bi(self):
        # La tabla de cuentas solo la lee el modelo de Power BI: la web no la nombra.
        os.remove(self.ruta("datos/m_cuentas.csv"))
        self.assertTrue(any("m_cuentas" in f for f in self.fallos()))

    def test_un_fichero_sin_filas(self):
        with open(self.ruta("datos/c_clientes.csv"), encoding="utf-8") as f:
            cabecera = f.readline()
        with open(self.ruta("datos/c_clientes.csv"), "w", encoding="utf-8") as f:
            f.write(cabecera)
        self.assertTrue(any("c_clientes" in f for f in self.fallos()))


class TestLasCifrasDeLaPortada(Base):
    def test_una_venta_cambiada_en_el_readme(self):
        self.cambia("README.md", "1.834.612,84", "1.834.612,85")
        self.assertTrue(self.fallos())

    def test_un_resultado_cambiado_en_el_readme_ingles(self):
        self.cambia("README.en.md", "406,707.28", "406,707.82")
        self.assertTrue(self.fallos())

    def test_la_desviacion_cambiada_en_el_readme(self):
        self.cambia("README.md", "70.085,60", "70.085,06")
        self.assertTrue(self.fallos())

    def test_los_datos_cambian_y_el_readme_no(self):
        self.cambia("datos/d_ventas_resultado.csv", "1834612.84", "1834600.00")
        self.assertTrue(self.fallos())

    def test_el_puente_cambia_y_el_readme_no(self):
        self.cambia("datos/d_puente_presupuesto.csv", "476792.88,476792.88",
                    "476800.00,476800.00")
        self.assertTrue(self.fallos())


class TestLosEnlaces(Base):
    def test_un_enlace_roto_en_el_readme(self):
        self.cambia("README.md", "](informes/README.md)", "](informes/NO_EXISTE.md)")
        self.assertTrue(any("NO_EXISTE" in f for f in self.fallos()))

    def test_una_imagen_que_falta(self):
        os.remove(self.ruta("assets/controller.png"))
        self.assertTrue(any("controller.png" in f for f in self.fallos()))

    def test_un_recurso_roto_en_la_web(self):
        self.cambia("index.html", 'src="cuadro.js', 'src="cuadro_viejo.js')
        self.assertTrue(any("cuadro_viejo.js" in f for f in self.fallos()))

    def test_CONTROL_un_enlace_externo_no_se_comprueba(self):
        """Sin red no se puede mirar una web ajena; un enlace https no es un fallo."""
        self.cambia("README.md", "## Límites", "[otra web](https://ejemplo.invalid/x)\n\n## Límites")
        self.assertEqual(self.fallos(), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
