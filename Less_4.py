# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
m_file = open('text_3.txt', 'r')

for i in m_file:
    i = i.split(' ', 1)
    new_file.append(rus[i[0]] + '  ' + i[1])
print(new_file)
m_file.close()
m_file_2 = open('text_3_new.txt', 'w')
m_file_2.writelines(new_file)
m_file_2.close()
