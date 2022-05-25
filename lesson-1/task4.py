valid_input = False
n = None
while not valid_input:
    try:
        n = int(input('Введите целое положительное число: '))
        if n < 0:
            print('Вы ввели отрицательное число! Повторите ввод')
            continue
        valid_input = True
    except ValueError:
        print('Вы ввели не число! Повторите ввод')

# Вариант 1
print('Максимальная цифра в числе: ', max(list(str(n))))
# Вариант 2
max_num = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max_num:
        max_num = n % 10

print('Максимальная цифра в числе: ', max_num)
