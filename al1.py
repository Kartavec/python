#
#1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
#

# num = input('Введите 3х значное число:')
#
# if len(num) == 3:
#     n1 = int(num) // 100
#     n2 = int(num) % 100 // 10
#     n3 = int(num) % 10
#     print('Сумма цифр: ' ,n1+n2+n3,'\nПроизведение цифр: ' ,n1*n2*n3)
# else:
#     print('Ошибка, введите 3х значное чисто')


#
#2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
#

# _5, _6 = 5, 6
#
# print(f'5&6 = {bin(_5&_6)} '
#       f'\n5|6 =  {bin(_5|_6)} '
#       f'\n5^6 = {bin(_5^_6)} '
#       f'\n5>>2 =  {bin(_5 >> 2)} '
#       f'\n5<<2 = {bin(_5 << 2)}')
#

#
#3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.
#

# print('Решаем уравнение y = kx + b через координатам двух точек!')
#
# print('Введите координаты точки А(x1;y1): ')
# x1 = float(input('x1 = '))
# y1 = float(input('y1 = '))
#
# print('Введите координаты точки B(x2;y2): ')
# x2 = float(input('x2 = '))
# y2 = float(input('y2 = '))
#
# print('Вычисляем значение k,b по формуле: \nk = (y1 - y2) / (x1 - x2) \nb = y2 - k * x2')
# k = (y1 - y2) / (x1 - x2)
# b = y2 - k * x2
# print(f'y = {k} * x + {b}')

#
#4. Написать программу, которая генерирует в указанных пользователем границах:
# ? случайное целое число, ? случайное вещественное число,
# ? случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
#

# import random
#
# print('Выберите что хотите получить случайно и в каком диапазоне: \n1-случайное целое число'
#       '\n2-случайное вещественное число \n3-символ')
#
# ch = input()
#
# if ch == '1':
#     print('Введите диапазон целых чисел: ')
#     i_ch1 = int(input('От: '))
#     i_ch2 = int(input('До:'))
#     ran_i = int(random.random() * (i_ch2 - i_ch1 + 1)) + i_ch1
#     print(ran_i)
# elif ch == '2':
#     print('Введите диапазон целых чисел: ')
#     f_ch1 = float(input('От: '))
#     f_ch2 = float(input('До:'))
#     ran_f = random.random() * (f_ch2 - f_ch1) + f_ch1
#     print(round(ran_f,3))
# elif ch == '3':
#     print('Введите диапазон целых чисел: ')
#     s_ch1 = ord(input('От: '))
#     s_ch2 = ord(input('До:'))
#     ran_s = int(random.random() * (s_ch2 - s_ch1 + 1)) + s_ch1
#     print(chr(ran_s))
# else:
#     print('Ошибка, введите число от 1 до 3')


#
#5. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

# ЗАДАТЬ ВОПРОС ПРЕПОДАВАТЕЛЮ

# s1 = ord(input('1я буква: '))
# s2 = ord(input('2я буква: '))
# _s1 = s1 - ord('a') + 1
# _s2 = s2 - ord('a') + 1
# res = abs(_s1-_s2)-1
# print(f'Место {chr(s1)} в алфавите под номером {_s1}'
#       f'\nМесто {chr(s2)} в алфавите под номером {_s2}'
#       f'\nМежду буквами символов: {res}')

#
#6.Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
#

# s = int(input('Введите цифру в диапазоне от 1 до 26 что бы получить букву: '))
# if s >=1 and s <= 26:
#     s = ord('a') + s - 1
#     print(f'Это буква: {chr(s)}')
# else:
#     print('Ошибка, введите цифру в диапазоне от 1 до 26')


#
#9. Вводятся три разных числа. Найти, какое из них является средним
# (больше одного, но меньше другого).
#

# print('Введите 3 числа: ')
# a = int(input('1: '))
# b = int(input('2: '))
# c = int(input('3: '))
#
# if b < a < c or c < a < b:
#     print('Среднее: ', a)
# elif a < b < c or c < b < a:
#     print('Среднее: ',b)
# elif a < c < b or b < c < a:
#     print('Среднее: ',c)
# else:
#     print('Одно число равно другому.')