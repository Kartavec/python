# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет
# оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней
# величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

m_file = open('text_2.txt', 'w')
m_string = input('Введите построчно фамилию и оклад: ')
while len(m_string) > 0:
    m_file.writelines(m_string + '\n')
    m_string = input('Введите построчно фамилию и оклад: ')
m_file.close()

m_file = open('text_2.txt', 'r')
work_list = m_file.read().split('\n')
les_pay = []
employee = []
for i in work_list:
    i = i.split()
    if len(i) > 0:
        if int(i[1]) < 20:
            les_pay.append(i[0])
        employee.append(i[1])

avar = sum(map(int, employee)) / len(employee)
res = ', '.join(les_pay)
print(f'Оклад меньше 20 у {res}, средняя величена дохода {avar}')
m_file.close()
