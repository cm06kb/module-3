import unittest
from calculator import *

class TddInPythonExample(unittest.TestCase):
    def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        self.assertEqual(4, calc.add(2,2))
        self.assertEqual(0, calc.add(-2,2))
        self.assertEqual(-4, calc.add(-2,-2))
    def test_calculator_multiply_method_returns_correct_result(self):
        calc = Calculator()
        self.assertEqual(4, calc.multiply(2,2))
        self.assertEqual(-4, calc.multiply(-2,2))
        self.assertEqual(4, calc.multiply(-2,-2))

if __name__=="__main__":
    unittest.main()

    