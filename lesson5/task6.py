with open('task6text.txt', 'r') as file_object:
    lesson_inf = file_object.readlines()
all_inf = {}
summ = 0
for i in lesson_inf:
    j = i.split()
    summ = 0
    for k in j:
        try:
            k = int(k)
        except ValueError:
            continue
        else:
            summ += k
        all_inf[j[0]] = summ
print(all_inf)
