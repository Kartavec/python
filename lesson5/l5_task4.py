rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('text_4.txt', 'r', encoding="utf8") as file_obj:
    content = file_obj.read().split('\n')
    for i in content:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1] + '\n')

with open('file_4_new.txt', 'w', encoding="utf8") as file_obj2:
    file_obj2.writelines(new_file)
