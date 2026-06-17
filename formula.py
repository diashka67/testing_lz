import math

def formula(a,b,f):
    return math.sqrt(a - b) / (a - b) + math.sqrt(f)


def handtesting(a,b,f):
    try:
        result = formula(a,b,f)
        print(f"Результат: {result}") 
        return result
        
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль (a - b == 0)")
        return "Деление на ноль"

    except ValueError:
        print("Ошибка: Нельзя взять корень из отрицательного числа")
        return "Нельзя взять корень из отрицательного числа"

    except TypeError:
        print("Ошибка типов данных")
        return "Ошибка типов данных"

    except Exception as e:      
        print(f"Неизвестная ошибка: {e}")
        return "Неизвестная ошибка"

if __name__ == "__main__":
    testiki = [
        (10, 6, 25),         # нормальный случай
        (7, 7, 9),           # деление на ноль
        (0, 0, 0),           # деление на ноль
        (2, 5, 16),          # отрицательное под первым корнем
        (3, 1, -4),          # отрицательное под вторым корнем
        ("a", 1, 4),         # текст
        (None, 0, 4),        # None
        (5+1j, 3, 16),       # комплексное
        (True, False, 16),   # bool
        (True, True, 9),     # деление на ноль
        (False, True, 9),    # отрицательное
    ]
    
    for a, b, f in testiki:
        print(f"Вход: a={a}, b={b}, f={f}")
        handtesting(a, b, f)
"""
1. Деление на ноль при (a - b) == 0
2. Все нули
3. Отрицательное значение под корнем
4. Все норм
5. Текст в аргументах
6. Пустой ввод, None
7. Комплексные числа без cmath
8. Буллевые значения
"""
