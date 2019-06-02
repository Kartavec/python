SIZE_M = 5
SIZE_N = 4
array = []
for i in range(SIZE_N):
    b = []
    s = 0
    print(f'{i}nd line')
    for j in range(SIZE_M - 1):
        n = int(input())
        s += n
        b.append(n)
    b.append(s)
    array.append(b)

for i in array:
    print(i)