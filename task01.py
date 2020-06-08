# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


def write_to_file(filename, data, mode):
    with open(filename, mode) as file:
        file.write(data + '\n')


if __name__ == '__main__':
    while True:
        input_data = f'{input("Добавить строку: ")}'
        if input_data == '':
            break
        else:
            write_to_file('task01_output.txt', input_data, 'a')
