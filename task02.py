class ZeroDivisionCustomError(Exception):
    pass


class ZeroDivisionErrorWrapper(Exception):
    pass


def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return False


def get_input_int(message):
    while True:
        user_input = input(message)
        if convert_to_int(user_input) is not False:
            return convert_to_int(user_input)
        else:
            print('Некорректный ввод! Введите число!')


def neat_division_with_wrapped_exception(x, y):
    try:
        return x / y
    except ZeroDivisionError as err:
        try:
            raise ZeroDivisionErrorWrapper(f'Message inside exception. Source error - {err}')
        except ZeroDivisionErrorWrapper as e:
            print(f'ZeroDivisionCustomError - {e}')


def neat_division(x, y):
    if y == 0:
        try:
            raise ZeroDivisionCustomError('Message inside exception')
        except ZeroDivisionCustomError as e:
            print(f'ZeroDivisionCustomError message - {e}')
            return
    return x / y


if __name__ == '__main__':
    divisible = get_input_int('Введите делимое: ')
    divider = get_input_int('Введите делитель:')

    print()
    print('Пример использования функции с кастомным исключением:')
    print(neat_division(divisible, divider))

    print()
    print('Пример использования функции с кастомным исключением - обёрткой на стандартным ZeroDivisionError: ')
    print(neat_division_with_wrapped_exception(divisible, divider))
