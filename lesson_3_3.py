# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.

def my_func(a, b, c):
    ls = [a, b, c]
    max1 = max(ls)
    ls.remove(max(ls))
    return max1 + max(ls)


print(my_func(4, 2, 8))
