with open("my_file.txt", 'w+', encoding="utf8") as my_file:
    while True:
        message = str(input('Enter your text: '))
        if 0 == len(message):
            break
        else:
            my_file.write(message + '\n')
