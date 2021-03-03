# Class 05
# Task 04
# A simple script that reads a text file line by line.
# The script substitutes English numbers with the numbers in Russian.
# New block with the numbers in Russian is written to a separate file.
# file_04.txt has the following info:
# """One - 1
# Two - 2
# Three - 3
# Four - 4"""


russian = {'One' : 'Odin', 'Two' : 'Dva', 'Three' : 'Tri', 'Four' : 'Chetire'}
new_f = []

with open('file_4.txt', 'r') as f_obj01:
    
    for i in f_obj01:
        i = i.split(' ', 1)
        new_f.append(russian[i[0]] + '  ' + i[1])
    for i in new_f:
        print(i)

with open('file_4_new.txt', 'w') as f_obj02:
    f_obj02.writelines(new_f)
