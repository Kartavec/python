def my_f(a_1, a_2):
    if a_2 == 0:
        print('На 0 делить нельзя!')
    else:
        return a_1 / a_2


print(
    my_f(
        a_1=int(input('Введите аргумент 1: ')),
        a_2=int(input('Введите аргумент 2: '))
    )
)
