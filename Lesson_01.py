# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

def div(x, y):
    res: int
    error: str = 'Вы ввели не корректные числа.'
    if x > 0 and y >0:
        res = x/y
        return res
    else:
        return error
var_input_first = int(input('Введите первое число: '))
var_input_second = int(input('Введите второе число: '))

print(div(var_input_first, var_input_second))
