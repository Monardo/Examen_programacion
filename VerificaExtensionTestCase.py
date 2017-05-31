import unittest
from Ejercicio2 import verificaExtension

class VerificaExtensionTestCase(unittest.TestCase):

    def test_envio_cadena_txt_lista_sin_txt_devuelve_false(self):
        self.assertEqual(False, verificaExtension('/home/user/listado.txt',['mp3','wav','mpeg']))

    def test_envio_cadena_txt_lista_txt_devuelve_true(self):
        self.assertEqual(True, verificaExtension('/home/user/listado.txt',['mp3','wav','mpeg','txt']))

    def test_envio_cadena_txt_lista_TXT_devuelve_true(self):
        self.assertEqual(True, verificaExtension('/home/user/listado.txt',['mp3','wav','mpeg','TXT']))

    def test_envio_cadena_tXt_lista_TXT_devuelve_true(self):
        self.assertEqual(True, verificaExtension('/home/user/listado.tXt',['mp3','wav','mpeg','TXT']))

    def test_envio_cadena_txt_lista_txt_devuelve_true(self):
        self.assertEqual(True, verificaExtension('/home/user/listado.txt',['txt']))

    def test_envio_cadena_sin_extension_lista_valida_devuelve_false(self):
        self.assertEqual(False, verificaExtension('/home/user/listado',['mp3','wav','mpeg','txt']))

    def test_envio_cadena_sin_extension_lista_vacia_devuelve_false(self):
        self.assertEqual(False, verificaExtension('/home/user/listado',[]))

    def test_envio_cadena_vacia_lista_vacia_devuelve_false(self):
        self.assertEqual(False, verificaExtension('',[]))
