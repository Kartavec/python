# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

from task02 import get_random_numbers


def get_unique_numbers(numbers):
    my_set = set()
    return [a for a in numbers if not (a in my_set or my_set.add(a))]


if __name__ == '__main__':
    numbers = get_random_numbers(1, 5, 20)

    result = get_unique_numbers(numbers)
    message = f'Исходный список: {numbers}\n' \
              f'Результат: {result}\n'
    print(message)
