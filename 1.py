
with open('1.txt', 'w', encoding='utf-8') as f:
    while True:
        a = input()
        f.write(a)
        if a == '':
            break

