# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input('Введите число n: ')
n_sec = str(n)+str(n)
n_thry = str(n) + str(n) + str(n)
res = int(n)  + int(n_sec) + int(n_thry)
print(f'{n} + {n}{n} + {n}{n}{n} = {res}')