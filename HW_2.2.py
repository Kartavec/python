ml = list(input("Введите любые символы "))
k = 0
for i in range(int(len(ml) / 2)):
    ml[k], ml[k + 1] = ml[k + 1], ml[k]
    k += 2
for el in ml:
    print(el,end="")

