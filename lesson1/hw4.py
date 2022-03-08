i = input('Введите целое положительное число: ')
n = 0
length = len(i) - 1
m = i[0]
if i[n] >= i[n + 1]:
    m = i[n]
else:
    m = i[n + 1]
    n = n + 1
while n <= length - 1:
    if i[n + 1] <= m:
        m = m
    else:
        m = i[n + 1]
    n = n + 1
print(m)



