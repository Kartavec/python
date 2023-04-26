with open('task4text.txt', 'r') as file_object:
    lines = file_object.readlines()
with open('task4_1text.txt', 'w') as file_object1:
    for line in lines:
        line = line.split()
        if line[0] == 'One':
            line[0] = 'Один'
        elif line[0] == 'Two':
            line[0] = 'Два'
        elif line[0] == 'Three':
            line[0] = 'Три'
        elif line[0] == 'Four':
            line[0] = 'Четыре'
        line = " ".join(line)
        file_object1.writelines(f'{line}\n')