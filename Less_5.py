# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и
# выводить её на экран.

m_file = open('text_4.txt', 'w+')
m_string = input('Набор чисел разделенных пробелом: ')
print(m_string)
m_file.writelines(m_string)
res_sum = list(map(int, m_string.split(' ')))
print(sum(res_sum))
