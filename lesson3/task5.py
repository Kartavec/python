sum = 0
indicator = True
while indicator == True:
    number_str = input('Please, enter the "SPACE" after every number or symbol.'
                        'For quit enter "@".\t')
    number_list = number_str.split()
    for i in number_list:
        if i != '@':
            i = int(i)
            sum += i
        elif i == '@':
            indicator = False
            break
    print(sum)