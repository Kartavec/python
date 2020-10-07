
with open('3.txt', 'r', encoding='utf-8') as f:
    accum = 0
    count = 0
    for lines in f:
        salary = float(lines.split()[1])
        accum += salary
        count += 1
        if salary > 20000:
            print(salary)
    average = accum / count

    print(f'Average salary: {average}')