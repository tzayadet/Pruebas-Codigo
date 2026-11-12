import unittest

from calculadora_basica import dividir, multiplicar, restar, sumar
from codificador import (
    decode_system_1,
    decode_system_2,
    encode_system_1,
    encode_system_2,
)


class CalculatorTests(unittest.TestCase):
    def test_arithmetic_operations(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(restar(8, 3), 5)
        self.assertEqual(multiplicar(4, 3), 12)
        self.assertEqual(dividir(12, 3), 4)

    def test_division_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(1, 0)


class CipherTests(unittest.TestCase):
    def test_caesar_round_trip_preserves_case_and_punctuation(self):
        message = "Hello, María! 123"
        self.assertEqual(decode_system_1(encode_system_1(message)), message)

    def test_affine_round_trip(self):
        message = "Tactical Recruiting: Python & SQL."
        self.assertEqual(decode_system_2(encode_system_2(message)), message)

    def test_caesar_known_value(self):
        self.assertEqual(encode_system_1("ABC xyz"), "DEF abc")


if __name__ == "__main__":
    unittest.main()
