# Class 03
# Task 06
# A program with a simple function that takes a word with letters in lowercase
# and returns a capitalized word.
# The program can take a string of words with letters in the lowercase separated by spaces.
# The program should print out capitalized words.

def int_func(words):
    result = ""
    for word in words:
        word = word[0].upper() + word[1:]
        result += word + " "
    return result


some_string = input("Enter a string of words with letters in the lowercase separated by spaces: ")

print(int_func(some_string.split()))
            
  
