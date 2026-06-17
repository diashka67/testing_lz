import unittest
from heand import hand

class Test_hand(unittest.TestCase):

    def test_by_zero(self):
        self.assertEqual((2, 2, 4), 'Деление на ноль')
        self.assertEqual((-2, -2, 4), 'Деление на ноль')

    def test_all_zero(self):
        self.assertEqual((0, 0, 0), 'Деление на ноль')

    def test_normal(self):
        self.assertEqual((2, -2, 4), 2.5)

    def test_negativet(self):
        self.assertEqual((1, 3, 9), 'Извлечение корня из отрицательного числа')
        self.assertEqual((1, 0, -5), 'Извлечение корня из отрицательного числа')

    def test_text(self):
        self.assertEqual(("a", 1, 4), 'Ошибка типов данных')
        self.assertEqual((1, "b", 4), 'Ошибка типов данных')
        self.assertEqual((2, 1, "text"), 'Ошибка типов данных')

    def test_empty(self):
        self.assertEqual(("", 0, 4), 'Ошибка типов данных')
        self.assertEqual((1, "", 4), 'Ошибка типов данных')

if __name__ == "__main__":
    unittest.main()
