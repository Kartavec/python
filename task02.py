# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

import random


def get_list(numbers):
    return [a for a, b in zip(numbers[1:], numbers[:-1]) if a > b]


def get_random_numbers(start=1, finish=450, count=10):
    return [random.randint(start, finish) for _ in range(count)]


if __name__ == '__main__':
    numbers = get_random_numbers()
    result = get_list(numbers)
    message = f'Исходный список: {numbers}\n' \
              f'Результат: {result}\n'
    print(message)
