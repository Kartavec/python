# coding=utf-8
def int_input(prompt):
    return typed_input(prompt, int)


def str_input(prompt):
    return typed_input(prompt, str)


def float_input(prompt):
    return typed_input(prompt, float)


def typed_input(prompt, input_type):
    value = None
    while True:
        try:
            value = input_type(input(prompt))
        except ValueError:
            print('Ошибка ввода')
            continue
        break
    return value