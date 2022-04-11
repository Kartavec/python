with open("my_file1.txt", 'w', encoding="utf8") as my_file:
    my_file.write("1 2 3 40 10")
with open("my_file1.txt", 'r', encoding="utf8") as my_file:
    line = my_file.read()
    num = line.split(' ')
    result = sum(int(s) for s in num)
    print(result)
