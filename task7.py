a = int(input('How many kilometers did athlete run on the first day?\n'))
b = int(input('how many kilometers should he run per day?\n'))
i = 0
while a < b:
    a = 1.1 * a
    i = i + 1
print (f'He achieved the goal - not less than {b} kilometeres - on the {i} day.' )