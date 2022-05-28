# coding=utf-8
def int_input(prompt):
    return typed_input(prompt, int)


def str_input(prompt):
    return typed_input(prompt, str)


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


stop = False
products = []
i = 1
while not stop:
    products.append((i, {
        "название": str_input('Введите название товара: '),
        "цена": int_input('Введите цену товара: '),
        "количество": int_input("Введите количество товара: "),
        "eд": str_input('Введите еденицу измерения товара: ')
    }))
    if str(input('Продолжить? [Y/N] ')).lower() == 'n':
        stop = True

print(products)
res = {}
for prod in products:
    for k, v in prod[1].items():
        if k not in res:
            res[k] = []
        if v not in res[k]:
            res[k].append(v)

print(res)
