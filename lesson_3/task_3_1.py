"""
Задание 1.
Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


my_a = float(input('Введите число a: '))
my_b = float(input('Введите число b: '))


def my_func(a, b):
    try:
        c = a / b
        return f'{c:.02f}'
    except ZeroDivisionError:
        return f'{a}/{b}=infinite'
    except ValueError:
        return 'Неверные значения'


print(my_func(my_a, my_b))
