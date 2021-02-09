my_string = str(input("Введите любое предложение: "))
my_string = my_string.split(" ")
my_string = list(my_string)
my_string[:] = (el[:10] for el in my_string)
for ind, el in enumerate(my_string):
    print(ind, el)