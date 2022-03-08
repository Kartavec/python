words = str(input('Введите несколько слов: ')).split(' ')
index = 0
for word in words:
    index +=1
    if len(word) <= 10:
        print(index, word)
    else:
        print(index, word[0:10])