# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


from task02 import split_text_by_rows


def get_members_information(rows):
    result = {}
    for row in rows:
        name, salary = row.split(' ')
        result[name] = int(salary)

    return result


def get_low_salary_members(members_info, target):
    result = [name for (name, salary) in members_info.items() if salary < target]
    return result


def get_average_salary(members_info):
    salaries = [salary for (_, salary) in members_info.items()]
    return sum(salaries)/len(salaries)


if __name__ == '__main__':
    filename = 'data/task03.txt'
    rows = split_text_by_rows(filename)
    members_info = get_members_information(rows)

    target_salary = 20000

    low_salary_members = get_low_salary_members(members_info, target_salary)
    print(f'Сотрудники, получающие меньше {target_salary} рублей: {", ".join(low_salary_members)}.')

    average_salary = get_average_salary(members_info)
    print(f'Средня зарплата равна {average_salary} рублей')
