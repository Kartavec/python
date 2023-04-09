employee_amount = 0
full_salary = 0
with open('task3text.txt', 'r') as file_object:
    for line in file_object:
        employee_amount += 1
        line = line.split()
        salary = int(line[1])
        full_salary += salary
        if salary < 20000:
            print(line[0])
    average_salary = full_salary / employee_amount
    print(f'The average salary is {average_salary}.')
