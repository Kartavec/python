from itertools import count
for el in count(3):
    if el > 10:
        break
    else:
        print(el)

print('*' * 50)

from itertools import cycle
c = 0
for el in cycle('Go'):
    if c > 20:
        break
    print(el)
    c += 1