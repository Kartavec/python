with open('task1text.txt', 'w') as file_object:
    while True:
       the_line = input('Please, enter the data.\t')
       if the_line == '':
           break
       else:
           file_object.write(f'{the_line}\n')
