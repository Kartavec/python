"""1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""


input_text = 0
f_write = open('lesson_5-1.txt', 'w')
while input_text != '':
    input_text = input("введите строку для записи в файл: ")
    input_file = f_write.write((input_text + '\n'))
f_write.close()
print('------------------------------------------------------------------------------------------')



"""2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк 
и слов в каждой строке.
"""


with open('lesson_5-2.txt') as income_file:
    lines_count = 0
    for line in income_file:
        word_count = len(line.split())
        lines_count += 1
        print(f'количество слов в строке {word_count}')
    print(f'Количество строк в файле {lines_count}')
print('------------------------------------------------------------------------------------------')


"""3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов 
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих 
сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
"""


with open('lesson_5-3.txt') as employees_list:
    employee_count = 0
    average_wage = 0
    less_20000 = []
    for name in employees_list:
        employees_raw = name.split()
        average_wage = average_wage + int(employees_raw[1])
        employee_count += 1
        if int(employees_raw[1]) < 20000:
            print(employees_raw[0])
    average_wage = average_wage / employee_count
    print(f'средняя зарплата: {average_wage}')
print('------------------------------------------------------------------------------------------')


"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские 
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

numb_rus_eng = dict(One='один', Two='два', Three='три', Four='четыре')
print(numb_rus_eng)
rus_numb = ''
with open('lesson_5-4.txt') as eng_numb:
    for numb_row in eng_numb:
        split_row = numb_row.split(' — ')
        split_row[0] = numb_rus_eng[split_row[0]]
        rus_numb = rus_numb + ' - '.join(split_row)
result = open('lesson_5-4-1.txt', 'w')
result.write(rus_numb)
result.close()
print('------------------------------------------------------------------------------------------')


"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""

from random import randint

random_num = open('lesson_5-5.txt', 'a')
for i in range(10):
    random_num.write(str(randint(0, 100)) + ' ')
random_num.close()

count_sum = open('lesson_5-5.txt', 'r')
count_sum_str = count_sum.read()
count_sum.close()
result_sum = 0
for str_elem in count_sum_str.split():
    result_sum = result_sum + int(str_elem)
print(f'Сумма чисел в файле: {result_sum}')