from itertools import cycle, count

""" 1 """

for i in count(1):
    print(i)
    if i == 10:
        break

""" 2 """

a = 0
for i in cycle([1, 2, 3]):
    if a > 20:
        break
    else:
        print(i)
        a += 1
