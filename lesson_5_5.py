# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('lesson_5_5.txt', "r+", encoding='utf-8') as f:
    print(*[i for i in range(1, 100, 2)], file=f)
    f.seek(0)
    print(f'Сумма чисел в файле: {sum([int(line) for line in str(f.readline()).split()])}')

