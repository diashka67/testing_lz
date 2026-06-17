import math

def formula(a,b,f):
    return math.sqrt(a - b) / (a - b) + math.sqrt(f)


def handtesting():
    try:
        result = formula(a,b,f)
        print(result)
        return result
        
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль (a - b == 0)")
        return "Деление на ноль"

    except ValueError:
        print("Ошибка: Нельзя взять корень из отрицательного числа")
        return "Нельзя взять корень из отрицательного числа"

    except TypeError:
        print("Ошибка: Неверный тип данных")
        return "Ошибка типов данных"

    except Exception as e:      
        print(f"Неизвестная ошибка: {e}")
        return "Неизвестная ошибка"
"""
1. Деление на ноль при (a - b) == 0
2. Все нули
3. Отрицательное значение под корнем
4. Нормальный случай
5. Текст в аргументах
6. Пустой ввод
"""
