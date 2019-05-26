import random
n = random.randint(0,100)
i = 1
print('The computer made a number. Guess it. You have 10 attempts')
while i <= 10:
    u = int(input(str(i) + 'nd attempt: '))
    if u > n:
        print('Lot')
    elif u < n:
        print('Few')
    else:
        print(f'You guessed it with {i}nd attempt')
        break
    i += 1
else:
    print('You have exhausted 10 attempts. It was made', n)