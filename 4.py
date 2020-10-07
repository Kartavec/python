
with open('4.1.txt', 'r') as f:
    lines = f.readlines()

print(lines)
lines[0] = lines[0].replace('One', 'Один')
lines[1] = lines[1].replace('Two', 'Два')
lines[2] = lines[2].replace('Three', 'Три')
lines[3] = lines[3].replace('Four', 'Четыре')


with open('4.2.txt', 'w') as f:
    f.writelines(lines)
