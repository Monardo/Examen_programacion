
import unittest
from Ejercicio1 import devuelveDivisores

class DevuelveDivisoresTestCase(unittest.TestCase):

    def test_envio_cadena_vacia_devuelve_lista_vacia(self):
        self.assertEqual([], devuelveDivisores("", [1, 2, 3]))


    def test_envio_numero_negativo_devuelve_lista_vacia(self):
        self.assertEqual([], devuelveDivisores(-1, [1, 2, 3]))


    def test_envio_cero_devuelve_listavacia(self):
        self.assertEqual([], devuelveDivisores(0, [1, 2, 3]))


    def test_envio_cero_y_listavacia_devuelve_listavacia(self):
        self.assertEqual([], devuelveDivisores(0, []))


    def test_envio_uno_y_listavalida_devuelve_1(self):
        self.assertEqual([1], devuelveDivisores(1, [1, 2]))


    def test_envio_dos_y_listavalida_devuelve_1y2negativo(self):
        self.assertEqual([1, -2], devuelveDivisores(2, [1, -2]))


    def test_envio_ocho_y_listavalida_devuelve_1_2_4negativo(self):
        self.assertEqual([1, 2, -4], devuelveDivisores(8, [1, 7, 2, -4, 6, 9]))


    def test_envio_331_y_listavalida_devuelve_1_331(self):
        self.assertEqual([1, 331], devuelveDivisores(331, [1, 2, 3, 7, 147, 331, 518]))