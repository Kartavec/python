# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
import os


def check_directory(filename):
    path = filename.rsplit('/', 1)[0]
    if not os.path.exists(path):
        os.makedirs(path)


def write_to_file(filename, data, mode):
    check_directory(filename)
    with open(filename, mode) as file:
        file.write(data + '\n')


if __name__ == '__main__':
    output_filename = 'output/task01.txt'
    while True:
        input_data = f'{input("Добавить строку: ")}'
        if input_data == '':
            break
        else:
            write_to_file(output_filename, input_data, 'a')
