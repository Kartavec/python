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


a = float_input('Результат первого дня (км.): ')
b = float_input('Желаемый результат (км.): ')
result_days = 1
while a < b:
    a += a * 0.1
    result_days += 1
    # print('День %d. Результат: %.2f' % (result_days, a))

print('на %d день спортсмен достиг результата — не менее %.2f км.' % (result_days, b))
