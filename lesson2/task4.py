the_string = input ('Please, enter words, separated by spaces.\t')
words_list = list (the_string.split())

for i in words_list:
    if len (i) <= 10:
        print (f'{words_list.index (i) +1}. {i}')
    else: 
        long_word = list (i)
        print (f'{words_list.index (i) + 1}.', end = ' ')
        for j in long_word:
            while long_word.index (j) < 10:
                print (f'{j}', end = '')
                break
        print ('')