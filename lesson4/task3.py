# решение
generator = (numb for numb in range(20, 241) if (numb % 20 == 0) or (numb % 21 == 0))

# вывод решения
for i in generator:
    print(i)


"""
второй вариант полностью в 1 строку

print([x for x in range(20,240) if x % 20 == 0 or x % 21 == 0])"""