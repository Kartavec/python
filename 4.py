inp_str = input('Enter string ')

words = inp_str.split()
i = 1
for word in words:
    print(f'{i}) {word[:10]}')
    i += 1