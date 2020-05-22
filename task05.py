import sys


def exit_cli():
    sys.exit()


def convert_to_int(input_string):
    try:
        return int(input_string)
    except ValueError:
        return None


def add_number(dictionary, number):
    dictionary.append(number)
    dictionary.sort(reverse=True)
    return dictionary


def print_dict(dictionary):
    print(dictionary)


if __name__ == '__main__':
    my_dict = [7, 5, 3, 3, 2]
    while True:
        user_input = input('Введите число. Для выхода напечатайте "exit" >>')
        if user_input.lower() == 'exit':
            exit_cli()
        number_to_add = convert_to_int(user_input)
        if number_to_add is None or number_to_add <= 0:
            continue
        my_dict = add_number(my_dict, number_to_add)
        print_dict(my_dict)
