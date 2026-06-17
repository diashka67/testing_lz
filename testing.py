import math
import unittest
from formula import formula, handtesting

class Test_hand(unittest.TestCase):

    def test_normal_case(self):
        result = handtesting(5, 3, 16)
        self.assertEqual(result, math.sqrt(2)/2 + 4)

    def test_zero_division(self):
        result = handtesting(2, 2, 4)
        self.assertEqual(result, "Деление на ноль")
        
        result = handtesting(0, 0, 0)
        self.assertEqual(result, "Деление на ноль")

    def test_negative_sqrt(self):
        result = handtesting(1, 3, 9)
        self.assertEqual(result, "Нельзя взять корень из отрицательного числа")
        
        result = handtesting(1, 0, -5)
        self.assertEqual(result, "Нельзя взять корень из отрицательного числа")

    def test_type_error(self):
        result = handtesting("a", 1, 4)
        self.assertEqual(result, "Ошибка типов данных")
        
        result = handtesting(2, 1, "textik")
        self.assertEqual(result, "Ошибка типов данных")

    def test_empty_input(self):
        result = handtesting("", 0, 4)
        self.assertEqual(result, "Ошибка типов данных")

    def test_none_input(self):
        result = handtesting(None, 0, 4)
        self.assertEqual(result, "Ошибка типов данных")

if __name__ == "__main__":
    unittest.main(verbosity=0)
