"""
Задание 3.
Создать текстовый файл (не программно). Построчно записать
фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих
сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""


file_name = 'task_5_3.txt'
workers = dict()
try:
    with open(file_name) as f:
        while True:
            line = f.readline().split()
            if not line:
                break
            try:
                workers[line[0]] = float(line[1])
                if workers[line[0]] <= 0:
                    raise ValueError
            except ValueError:
                pass
            except IndexError:
                pass
except IOError:
    print('Ошибка ввод-вывода')

print('Сотрудники у котрых зарплата меньше 20000:')
print(
    ', '.join([worker for worker, salary in workers.items() if salary < 20000])
)
print(
    f'Средний доход сотрудников: {sum(workers.values()) / len(workers): .2f}'
)
