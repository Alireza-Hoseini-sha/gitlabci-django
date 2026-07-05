from django.test import TestCase

# Create your tests here.

class SimpleTest(TestCase):
    def test_simple_test(self):
        self.assertEqual(1 + 2, 3)

    def test_simple_test_2(self):
        self.assertEqual(8 - 6, 2)

    def test_basic_multiplication(self):
        self.assertEqual(2 * 3, 6)

    def test_basic_division(self):
        self.assertEqual(6 / 3, 2)

    def test_basic_modulo(self):
        self.assertEqual(7 % 3, 1)

    def test_basic_power(self):
        self.assertEqual(2 ** 3, 8)
        