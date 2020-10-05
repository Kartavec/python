from itertools import cycle


def cyclic_letters(letters):
    c = 0
    for letter in cycle(letters):
        c += 1
        if c > 50:
            break
        yield letter


print(list(cyclic_letters('AIDBHFIDHBF')))
