import math

def formula(a,b,c,d,f):
    return math.sqrt(a - b) / (a - b) + math.sqrt(f)


def handtesting():
    try:
        result = formula(a,b,c,d,f)
        print(result)

    except (ZeroDivisionError):
        result = 'Деление на ноль'
        print('Деление на ноль')


    except(TypeError):
        result = 'Ошибка типов данных'
        print('Ошибка типов данных')

    except(ValueError):
        result = 'Нельзя взять корень отрицательного числа'
        print('Нельзя взять корень отрицательного числа')

"""
1. Деление на ноль при (a - b) == 0
2. Все нули
3. Отрицательное значение под корнем
4. Нормальный случай
5. Текст в аргументах
6. Пустой ввод
"""
