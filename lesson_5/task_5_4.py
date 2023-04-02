"""
Задание 4.
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


file_in = 'task_5_4_in.txt'
file_out = 'task_5_4_out.txt'
lines = []
figures = {
    'one': 'один', 'two': 'два', 'three': 'три',
    'four': 'четыре', 'five': 'пять', 'six': 'шесть',
    'seven': 'семь', 'eight': 'восемь',
    'nine': 'девять', 'zero': 'ноль'
}
try:
    with open(file_in) as f:
        lines = f.readlines()
except IOError as e:
    print(e)
    print('Ошибка ввод-вывода')

try:
    with open(file_out, 'w') as f:
        for line in lines:
            word, delimetr, digit = line.split()
            f.write(f"{figures[word.lower()]} {delimetr} {digit}\n")
except IOError as e:
    print(e)
    print('Ошибка ввод-вывода')
