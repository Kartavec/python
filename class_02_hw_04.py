# Class 02
# Task 04

some_string = input('Enter a few words separated by spaces: ')

list_of_words = list(some_string.split())

num = 1

for word in list_of_words:
    if len(word) > 10:
        print(num, word[:10])
        num += 1
    else:
        print(num, word)
        num += 1




      

