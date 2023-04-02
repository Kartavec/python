"""
Задание 1.
Создать программный файл в текстовом формате, записать
в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""


result = []
while True:
    line = input("Введите строку, или Enter для выхода: ")
    if line == '':
        exit()
    else:
        newline = line + '\n'
        result.append(newline)
    with open("test.txt", "w") as my_fail:
        my_fail.writelines(result)
