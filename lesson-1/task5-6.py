def float_input(prompt):
    valid_input = False
    float_value = None
    while not valid_input:
        try:
            float_value = float(input(prompt))
            if float_value < 0:
                print('Вы ввели отрицательное число! Повторите ввод')
                continue
            valid_input = True
        except ValueError:
            print('Вы ввели не число! Повторите ввод')
    return float_value


revenue = float_input('Введите выручку: ')
costs = float_input('Введите издержки: ')

if revenue > costs:
    profit = revenue - costs
    print('Выручка больше издержек. Всё ок')
    print('Прибыль: %.2f%%' % (profit / revenue * 100))
    employees = int(float_input('Введите количество сотрудников: '))
    print('Прибыль на одного сотрудника: %.2f' % (profit/employees))
elif revenue == costs:
    print('Выручка равна издержкам')
else:
    print('Издержки привышают прибыль')