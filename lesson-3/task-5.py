def sum_from_chars(chars):
    tmp_sum = 0
    for simb in chars:
        if simb.lower() == 'n':
            return tmp_sum, True
        try:
            tmp_sum += int(simb)
        except TypeError:
            continue
    return tmp_sum, False


stop = False
res = 0
while not stop:
    tmp, stop = sum_from_chars(
        str(input('Введите строку чисел, разделённых пробелом или N для выхода: ')).split()
    )
    res += tmp
    print(f'Промежуточный результат: {res}')

print(f'Результат: {res}')
