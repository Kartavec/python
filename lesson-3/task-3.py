from helper import int_input


def my_func(p1, p2, p3):
    li = [p1, p2, p3]
    li.remove(min(li))
    return sum(li)


a = int_input('Введите число a: ')
b = int_input('Введите число b: ')
c = int_input('Введите число c: ')
print(my_func(a, b, c))
