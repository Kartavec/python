from helper import float_input


def diff_func(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print('Ошибка! Делить на 0 нельзя')
        return


result = diff_func(
    float_input('Введите первое число: '),
    float_input('Введите второе число: '),
)

print(f'Результат: {result}')
