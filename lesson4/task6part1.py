from itertools import count

for el in count(3, 1):
    if el <= 10:
       print(el, end=" ")
    else: 
        break