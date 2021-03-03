# Class 05
# Task 06
# A script that uses data from a text file with some info on the subject and:
# 1.number of lecture classes
# 2.number of practical classes
# 3.number of lab classes
# Not all subject has every type of class
# The script creates a dictionary with some info on the every class
# with total hours of required classes

subjects = {}

with open('file_6.txt', 'r') as in_file:
    for line in in_file:
        subject, stats = line.split(':')
        subject_sum = sum(map(int, "".join([i for i in stats if i == ' ' or (i >= '0' and i <= '9')]).split()))
        subjects[subject] = subject_sum


print(f'Total hours on every subject - \n {subjects}')
