# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

from task01 import write_to_file


def generate_numbers(count, start, finish):
    return [random.randint(start, finish) for _ in range(count)]


def convert_to_int(values):
    result = []
    for value in values:
        result.append(int(value))
    return result


def convert_to_str(numbers):
    result = []
    for number in numbers:
        result.append(str(number))
    return result


def get_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = file.read().split(' ')
    return convert_to_int(numbers)


if __name__ == '__main__':
    numbers = generate_numbers(30, 1, 150)
    output_filename = 'task05_output.txt'

    data = ' '.join(convert_to_str(numbers))
    write_to_file(output_filename, data, 'w')

    numbers_from_file = get_numbers_from_file(output_filename)
    print(f'Последовательность чисел: {numbers}')
    print(f'Сумма чисел: {sum(numbers_from_file)}')
