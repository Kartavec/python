with open('5.txt', 'w') as f:
    f.write('1 2 3 4 5')

with open('5.txt', 'r') as f:
    print(sum(map(int, f.readline().split())))
