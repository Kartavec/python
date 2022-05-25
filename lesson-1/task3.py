valid_input = False
n = None
while not valid_input:
    try:
        n = int(input('Введите целое число: '))
        valid_input = True
    except ValueError:
        print('Вы ввели не число! Повторите ввод')

print('Результат: ', (n + int(str(n)*2) + int(str(n)*3)))
