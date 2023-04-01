#решение
generator = (numb for numb in range(20, 241) if (numb % 20 == 0) or (numb %  21 == 0))

#вывод решения
for i in generator:
    print(i)