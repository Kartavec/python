num = int(input('введите число '))
max_num = 0

if num < 0:
    print('Только положительные числа!')
else:
    while num:
        digit = num % 10
        num //= 10
        if digit > max_num:
            max_num = digit

    print(f'Самая большая цифра в числе {max_num}')
