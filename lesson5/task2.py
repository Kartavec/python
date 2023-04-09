lines_amount = 0
with open('task2text.txt', 'r') as file_object:
    for line in file_object:
        lines_amount += 1
        line = line.split()
        words_in_line = len(line)
        print(f'{lines_amount} line contains {words_in_line} words.')
print(f'There is(are) {lines_amount} line(s) in this file.')
