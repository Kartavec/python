"""
Задание 2.
Создать текстовый файл (не программно), сохранить
в нём несколько строк, выполнить подсчёт строк и словв каждой строке.
"""


def count_words(string):
    return len(string.split())


def count_lines(file):
    file.seek(0, 0)
    return len(file.readlines())


with open('task_5_2.txt', 'r') as f:
    for i, line in enumerate(f.readlines(), 1):
        print(f'Слов в {i} строке: {count_words(line)}')
    print(f'Количество строк: {count_lines(f)}')
