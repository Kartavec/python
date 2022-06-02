from helper import float_input, int_input


def my_func_v1(x, y):
    return x ** y


def my_func_v2(x, y):
    res = 1
    for i in range(0, abs(y)):
        res /= x
    return res


valid_x = False
valid_y = False
x = None
y = None
while not valid_x or not valid_y:
    if x and y:
        print('Ошибка ввода')
    if not valid_x:
        x = float_input('Введите действительное положительное число: ')
    if not valid_y:
        y = int_input('Введите целое отрицательное число: ')
    valid_x = x > 0
    valid_y = y < 0

print(f'Результат (вариант 1): {my_func_v1(x, y)}')
print(f'Результат (вариант 2): {my_func_v2(x, y)}')
