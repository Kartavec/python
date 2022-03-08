list = list(input("Введите список: "))
m = 0
for i in range(int(len(list) / 2)):
    list[m], list[m + 1] = list[m + 1], list[m]
    m += 2
print(list)






