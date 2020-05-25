def division(divisible, divider):
    try:
        return divisible / divider
    except ZeroDivisionError:
        return None


def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None


def main():
    a = convert_to_int(input('Введите делимое: '))
    if a is None:
        print('Введены некорректные данные, делимое должно быть числом!')
        return

    b = convert_to_int(input('Введите делитель: '))
    if b is None:
        print('Введены некорректные данные, делитель должен быть числом!')
        return

    result = division(a, b)
    if result is None:
        print('На ноль делить нельзя!')
    else:
        print(f'Результат операции: {result}')


if __name__ == '__main__':
    main()
