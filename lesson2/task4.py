string = list(input('Введите слова через пробел: ').split(' '))
for index, elem in enumerate(string, start=1):
    print(index, elem[:10])