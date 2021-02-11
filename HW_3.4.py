def pow():
    global x, y
    x = float(input('give real positive number X '))
    y = int(input('give integer negative number Y '))
    c = x ** y
    return c
print(f'X raised to the N-th power is {pow():.02f}')

e = '*' * 30
print(e)

def pow2():
    d = 1 / x
    if y == 0:
        d = 1
    else:
        count = 1
    while count <= abs(y):
        d = d * 1 / count
        count += 1
    return d
print(f'X raised to the N-th power is {pow2():.02f}')