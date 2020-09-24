import random

print('Привет, начинаем учить python')
print('Попробуем сумировать a + b')
a = int(input('Введите a '))
b = int(input('Введите b '))
print(f'a + b = {a + b}')

print('Возведем a в степень b')
a = int(input('Введите a '))
b = int(input('Введите b '))
print(f'a в степени b = {a**b}')

print('На последок случайное число от 0 до 100')
random_num = random.randint(0, 100)
print(random_num)