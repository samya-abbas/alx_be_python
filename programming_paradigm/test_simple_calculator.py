import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(10, -7), 3)
        self.assertAlmostEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)


    def test_subtract(self):
        # Test subtraction with two positive numbers
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        # Test subtraction with two negative numbers
        self.assertEqual(self.calc.subtract(-10, -5), -5)
        self.assertEqual(self.calc.subtract(-5, -10), 5)
        # Test subtraction with a mix of positive and negative numbers
        self.assertEqual(self.calc.subtract(5, -3), 8)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        # Test subtraction involving zero
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        # Test subtraction with floating-point numbers
        self.assertAlmostEqual(self.calc.subtract(7.5, 2.5), 5.0)
        self.assertAlmostEqual(self.calc.subtract(10.0, 0.1), 9.9)

    def test_multiply(self):
        # Test multiplication with two positive numbers
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(10, 0.5), 5.0)
        # Test multiplication with two negative numbers
        self.assertEqual(self.calc.multiply(-5, -3), 15)
        # Test multiplication with a mix of positive and negative numbers
        self.assertEqual(self.calc.multiply(-5, 3), -15)
        self.assertEqual(self.calc.multiply(5, -3), -15)
        # Test multiplication involving zero
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, -10), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        # Test multiplication with floating-point numbers
        self.assertAlmostEqual(self.calc.multiply(2.5, 2.0), 5.0)
        self.assertAlmostEqual(self.calc.multiply(0.5, 0.5), 0.25)

    def test_divide(self):
        # Test division with two positive numbers
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        # Test division with two negative numbers
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        # Test division with a mix of positive and negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        # Test division by one
        self.assertEqual(self.calc.divide(10, 1), 10.0)
        self.assertEqual(self.calc.divide(-5, 1), -5.0)
        # Test dividing zero by a non-zero number
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -5), 0.0)
        # Test division by zero, which should return None
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        # Test division with floating-point numbers
        self.assertAlmostEqual(self.calc.divide(5.0, 2.0), 2.5)
        self.assertAlmostEqual(self.calc.divide(1.0, 3.0), 0.3333333333333333)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

