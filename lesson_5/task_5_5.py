"""
Задание 5.
Создать (программно) текстовый файл, записать в него программно
набор чисел, разделённых пробелами. Программа должна подсчитывать
сумму чисел в файле и выводить её на экран.
"""


with open("task_5_5.txt", "w+") as f:
    try:
        user_enter = input('Введите числа через пробел: ')
        f.writelines(user_enter)
        answer = user_enter.split()
    except ValueError:
        print('Ошибка ввода данных')
    print(sum(map(int, answer)))
