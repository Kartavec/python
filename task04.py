# 4. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

import functools


def get_even_numbers(start, finish):
    return [a for a in range(start, finish + 1) if (a % 2 == 0)]


def get_product_of_numbers(numbers):
    return functools.reduce(lambda a, b: a * b, numbers)


if __name__ == '__main__':
    start = 100
    finish = 1000
    numbers = get_even_numbers(100, 1000)

    result = get_product_of_numbers(numbers)
    print(f'Произведение чётных чисел в инстервале от {start} до {finish} равно {result}')
