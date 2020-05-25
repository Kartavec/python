def division(divisible, divider):
    try:
        return divisible / divider
    except ZeroDivisionError:
        return None


def convert_to_int(number):
    try:
        return int(number)
    except ValueError:
        return None


def main():
    a = convert_to_int(input('Введите делимое: '))
    b = convert_to_int(input('Введите делитель: '))

    if a is None or b is None:
        print('Введены некорректные данные, делимое и делитель должны быть числами!')
        return

    result = division(a, b)
    if result is None:
        print('На ноль делить нельзя!')
    else:
        print(f'Результат операции: {result}')


if __name__ == '__main__':
    main()
