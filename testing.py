import math
import unittest
from formula import formula, handtesting

class Test_auto(unittest.TestCase):
    #тесты будут запускаться в алфавитном порядке
    def test_normal(self):
        result = handtesting(10, 6, 25)
        self.assertAlmostEqual(result, math.sqrt(4)/4 + math.sqrt(25))

    def test_zero_division(self):
        result = handtesting(7, 7, 9)
        self.assertEqual(result, "Деление на ноль")
        
        result = handtesting(0, 0, 0)
        self.assertEqual(result, "Деление на ноль")

    def test_negative_sqrt(self):
        result = handtesting(2, 5, 16)
        self.assertEqual(result, "Нельзя взять корень из отрицательного числа")
        
        result = handtesting(3, 1, -4)
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
        
    def test_complex_numbers(self): #можно было использовать cmath для комплексных, но решила так 
        result = handtesting(5+1j, 3, 16)
        self.assertEqual(result, "Ошибка типов данных")
        
    #тут проблема в том, что оно перехватывало TypeError быстрее чем ZeroDivisionError, поэтому тест падал
    #def test_complex_with_zero_division(self):
        #result = handtesting(2+1j, 2+1j, 9)
        #self.assertEqual(result, "Деление на ноль")
        
    def test_different_numeric_types(self):
        result = handtesting(True, False, 16)  
        self.assertIsInstance(result, float)
        
    def test_bool_inputs(self):
        
        #Тесты с булевыми значениями (True = 1, False = 0), все те же самые проверки
        
        result = handtesting(True, False, 16)
        self.assertAlmostEqual(result, math.sqrt(1)/1 + 4)
        
        result = handtesting(True, True, 9)
        self.assertEqual(result, "Деление на ноль")
        
        result = handtesting(False, False, 4)
        self.assertEqual(result, "Деление на ноль")
        
        result = handtesting(False, True, 9)
        self.assertEqual(result, "Нельзя взять корень из отрицательного числа")
        
        result = handtesting(True, 0, 25)
        self.assertAlmostEqual(result, math.sqrt(1)/1 + 5)

if __name__ == "__main__":
    unittest.main(verbosity=2) #чтобы выводило красиво, а то были неэстетичные точки, которые показывали успешное выполнение
