# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.

staff = []
min_salary = 20000
with open('lesson_5_3.txt', 'r', encoding='utf-8') as f:
    [print(f"Фамилия: {empl.split()[0]}, оклад: {empl.split()[1]}") for empl in f.readlines()
     if int(empl.split()[1]) < min_salary]
