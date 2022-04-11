with open("text_3.txt", 'r', encoding="utf8") as new_file:
    array = list(new_file)
    for a in array:
        element = a.strip().split()
        if float(element[-1]) < 20000:
            print(element[0])
        else:
            continue
    salary = [line.strip().split(' ')[-1] for line in array]
    average_salary = sum(float(i) for i in salary)
    print(f"Средняя величина доходов всех сотрудников: {average_salary}")
