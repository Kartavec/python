# Class 05
# Task 02
# A simple script that creates a text file (not programmatically)
# and writes down a few lines entered by the user.
# The script counts the number of lines and words in every line.

some_file = open('file_01.txt', 'r')

lines = some_file.read()

print(f'Content: \n{lines}')

some_file = open('file_01.txt', 'r')

lines = some_file.readlines()

print(f'Number of lines in the file - {len(lines)}')

some_file = open('file_01.txt', 'r')

lines = some_file.read()

lines = lines.split()

print(f'Total number of words - {len(lines)}')

some_file.close()


