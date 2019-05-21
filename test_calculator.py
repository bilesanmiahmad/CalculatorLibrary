import calculator
import unittest2 as unittest


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(5, 3)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)
    
    def test_division(self):
        assert 2 == calculator.divide(100, 50)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(20, 0)