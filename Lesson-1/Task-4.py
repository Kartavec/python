your_number = input('Введите целое положительное число: ')
i = len(your_number) - 1
a = your_number[i - 1]
while i >= 0:
    b = your_number[i]
    if a < b:
        a = b
    i = i - 1
print(f'Наибольшее число:{a}')