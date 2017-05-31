import unittest
from Ejercicio3 import devuelveMatrizTriangular


class DevuelveMatrizTriangularTestCase (unittest.TestCase):

    def test_envio_numero_negativo_devuelve_lista_vacia(self):
        self.assertEqual([], devuelveMatrizTriangular(-1))


    def test_envio_cero_devuelve_lista_vacia(self):
        self.assertEqual([], devuelveMatrizTriangular(0))


    def test_envio_uno_devuelve_lista_vacia(self):
        self.assertEqual([], devuelveMatrizTriangular(1))


    #def test_envio_dos_devuelve_lista_de_dos(self):
        #self.assertEqual([[2,3],[0,5]], devuelveMatrizTriangular(2))


    #def test_envio_tres_devuelve_lista_de_tres(self):
        #self.assertEqual([[x,x,x],[0,x,x],[0,0,x]], devuelveMatrizTriangular(3))

    # def test_envio_cuatro_devuelve_lista_de_cuatro(self):
        #self.assertEqual([[x,x,x,x],[0,x,x,x],[0,0,x,x],[0,0,0,x]], devuelveMatrizTriangular(4))

    def test_envio_cadena_de_cuatro_devuelve_lista_vacia(self):
        self.assertEqual([], devuelveMatrizTriangular("4"))


    def test_envio_cadena_PEPE_devuelve_lista_vacia(self):
        self.assertEqual([], devuelveMatrizTriangular("PEPE"))


    def test_envio_float_devuelve_lista_vacia(self):
        self.assertEqual([], devuelveMatrizTriangular(2.5))
