summary = 0
with open('task5text.txt', 'w') as file_object:
    numbers_list = input("Please, enter numbers separated by space.\t")
    file_object.write(numbers_list)
with open('task5text.txt', 'r') as file_object:
    line1 = file_object.readline()
line_split = line1.split()
for i in line_split:
    i = int(i)
    summary += i
print(summary)
