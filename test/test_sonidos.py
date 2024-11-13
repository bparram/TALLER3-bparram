import unittest
from unittest.mock import MagicMock
from models.huron import Huron
from models.boa_constrictor import Boa_Constrictor

class TestSonidoAnimales(unittest.TestCase):

    def test_sonido_huron(self):
        hmock = MagicMock(spec=Huron)
        hmock.hacer_sonido.return_value = "¡Eek Eek!"
        self.assertEqual(hmock.hacer_sonido(),"¡Eek Eek!")
        return print("El huron hace sonido correctamente")

    def test_sonido_boa(self):
        bmock = MagicMock(spec=Boa_Constrictor)
        bmock.hacer_sonido.return_value = "¡Eek Eek!"
        self.assertEqual(bmock.hacer_sonido(),"¡Eek Eek!")
        return print("La boa hace sonido correctamente")


class TestCalcularFlete(unittest.TestCase):

    def test_formato_valor_flete_huron(self):
        fletehuron_mock = MagicMock(spec= Huron)
        fletehuron_mock.peso = 10.0
        fletehuron_mock.impuestos = 15.6
        fletehuron_mock.calcular_flete = Huron.calcular_flete.__get__(fletehuron_mock,Huron)
        resultado = fletehuron_mock.calcular_flete()
        self.assertIsInstance(resultado,float)
        return print("el resultado tiene el formato correcto")

    def test_formato_valor_flete_boa(self):
        fleteboa_mock = MagicMock(spec= Boa_Constrictor)
        fleteboa_mock.peso = 25.0
        fleteboa_mock.impuestos = 30.6
        fleteboa_mock.calcular_flete = Huron.calcular_flete.__get__(fleteboa_mock,Huron)
        resultado = fleteboa_mock.calcular_flete()
        self.assertIsInstance(resultado,float)
        return print("el resultado tiene el formato correcto")

class TestAlimentarBoas(unittest.TestCase):

    def test_alimentar_un_raton(self):
        boa1 = Boa_Constrictor(nombre="Boa", edad=4, peso=15.5, pais_origen="Brasil", impuestos=5.0, contar_ratones=3)
        ratones_iniciales = boa1.contar_ratones
        boa1.agregar_raton()
        self.assertEqual(boa1.contar_ratones, ratones_iniciales + 1)
        return print("Las boas comen de a un solo raton")

    def test_alimentar_boa_demasiados_ratones(self):
        boa10 = Boa_Constrictor(nombre="Boa", edad=4, peso=15.5, pais_origen="Brasil", impuestos=5.0, contar_ratones=10)
        with self.assertRaises(ValueError) as texto:
            boa10.agregar_raton()  
        self.assertEqual(str(texto.exception), "Demasiados ratones!")

