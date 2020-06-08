# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

from task02 import split_text_by_rows
from task05 import convert_to_int

import re


def add_item_to_dict(dictionary, row):
    subject, _ = row.split(':')
    pattern = '\d+'
    hours = convert_to_int(re.findall(pattern, row))
    dictionary[subject] = sum(hours)


def make_dictionary(rows):
    result = {}
    for row in rows:
        add_item_to_dict(result, row)
    return result


if __name__ == '__main__':
    filename = 'data/task06.txt'
    rows = split_text_by_rows(filename)
    print(make_dictionary(rows))
