import unittest
from Ejercicio4 import devuelveGanador

class DevuelveGanadorTestCase(unittest.TestCase):

    def test_envio_lista_vacia_devuelve_cadena_vacia(self):
        self.assertEqual('""', devuelveGanador([]))


    def test_envio_lista_valida_de_una_partida_devuelve_a(self):
        self.assertEqual('a', devuelveGanador([("a", 1, "b", 0)]))


    def test_envio_lista_valida_de_tres_partidas_devuelve_c(self):
        self.assertEqual('c', devuelveGanador([("a",1,"b",0),("a",1,"c",2),("c",3,"b",0)]))


    def test_envio_lista_valida_de_tres_partidas_empate_devuelve_c(self):
        self.assertEqual('c', devuelveGanador([("a",1,"b",1),("a",1,"c",1),("c",1,"b",1)]))


    def test_envio_lista_valida_de_cuatro_devuelve_a(self):
        self.assertEqual('a', devuelveGanador([("a",1,"b",-2),("a",1,"c",1),("c",1,"b",1),("d",1,"a",9)]))
