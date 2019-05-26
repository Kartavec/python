n = int(input('How many numbers will there be? '))
d = int(input('What figure to count? '))
c = 0
for i in range(1, n + 1):
    m = int(input("Number " + str(i) + ": "))
    while m > 0:
        if m % 10 == d:
            c += 1
        m = m // 10

print(f'Was entered {c}, digit {d}')