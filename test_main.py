import unittest
from main import Abastecer

class TestMain(unittest.TestCase):

    def setUp(self):

        self.cliente_1 = Abastecer("Alcool", 2.75, 15, "Cartão")
        self.cliente_2 = Abastecer("Gasolina", 3.29, 5, "Dinheiro")

    def tearDown(self):
        pass

    def test_valor_a_pagar(self):
        self.cliente_1.total_a_pagar()
        self.cliente_2.total_a_pagar()

        self.assertEqual(self.cliente_1.total_a_pagar(), 41.25)
        self.assertEqual(self.cliente_2.total_a_pagar(), 16.45)