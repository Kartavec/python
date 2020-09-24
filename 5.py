proceeds = int(input('Введите выручку '))
costs = int(input('Введите издержки '))

results = proceeds - costs
if results <= 0:
    print(f'Работаем в убыль! {results}')
else:
    print(f'Имеется прибыль {results}')

    print(f'Рентабельность {results/proceeds:01.2f}')

    emp_num = int(input('Введите количество сотрудников '))
    print(f'Прибыль на сотрудника {results/emp_num:1.2f}')