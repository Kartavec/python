# 3. Реализовать функцию my_func(), которая принимает три позиционных
# аргумента и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    sum: int
    if a > b > c:
        return a + b
    elif a > c > b:
        return a + c
    elif b > c > a:
        return b + c
    elif c > b > a:
        return c + b


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

print(my_func(a, b, c))
