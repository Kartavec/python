"""
Задание 2.
Представлен список чисел.
Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию,
оформить в виде списка.
Для его формирования используйте генератор.
Пример исходного списка:
    [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат:
    [12, 44, 4, 10, 78, 123].
"""

from random import randint


def list_generator(range_begin, range_end, cnt_of_elements):
    return [randint(range_begin, range_end) for _ in range(cnt_of_elements)]


def my_list(lst):
    return [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i - 1]]


if __name__ == '__main__':
    source_list = list_generator(1, 100, 15)
    print(f'Исходный список: {source_list}')
    print(f'Итоговоый список: {my_list(source_list)}')
