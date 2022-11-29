# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
# элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.
from typing import Dict

list_1 = [1, 45, 2.35, None, 'some_word', 0, 0x1d5e, 0b1011101010111101110001]
print(list_1)
for element in list_1: print(type(element))

# 2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3
# и т. д. При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно
# использовать функцию input().
element_input = 0
list_2 = []
for element_input in range(0, 9):
    element_input = input(f"Введите значения в массиве: ")
    list_2.append(element_input)
print(list_2)
i = 1
while i < 8:
    print(list_2)
    list_2.insert((i - 1), list_2.pop(i))
    print(list_2)
    i = i + 2
    print(i)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и dict.
# Вариант со списками
month_number = int(input(f"Введите номер месяца от 1 до 12: "))
month_name = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
              'декабрь']
sezon = ['зима', 'весна', 'лето', 'осень']
if 6 > month_number > 2:
    j = 1
elif 9 > month_number > 5:
    j = 2
elif 12 > month_number > 8:
    j = 3
else:
    j = 0
print(f"Вы выбрали {month_name[(month_number - 1)]}. Месяц {month_name[(month_number - 1)]} относится к времени года"
      f" {sezon[j]}")

# Вариант со словарями
month_number = int(input(f"Введите номер месяца от 1 до 12: "))
dict_month = {"1": 'январь', "2": 'февраль', "3": 'март', "4": 'апрель', "5": 'май', "6": 'июнь',
              "7": 'июль', '8': 'август', "9": 'сентябрь', "10": 'октябрь', "11": 'ноябрь',
              "12": 'декабрь'}
dict_sezon = {"key_1": 'зима', "key_2": 'весна', "key_3": 'лето', "key_4": 'осень'}
if month_number < 6 > 2:
    k = "key_2"
elif month_number < 9 > 5:
    k = 'key_3'
elif month_number < 12 > 8:
    k = "key_4"
else:
    k = "key_1"
print(f"Вы выбрали {dict_month[str(month_number)]}. Месяц {dict_month[str(month_number)]} "
      f"относится к времени года {dict_sezon[str(k)]}")

#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.
phrase = input("Введите фразу из нескольких слов: ")
for i, s in enumerate(phrase.split()): print(i + 1, s[0:10])

#5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает. У пользователя
# нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый
# элемент с тем же значением должен разместиться после них.
num_input = int(input("Введите целое число от 0 до 9: "))
my_range = [7, 5, 3, 3, 2]
print(my_range)
o = 0
while my_range[o] >= num_input:
   o += 1
my_range.insert(o, num_input)
print(my_range)

