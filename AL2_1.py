while True:
    s = input('symbol:')
    if s == '+' or s == '-' or s == '/' or s == '*':
        a = int(input('a:'))
        b = int(input('b:'))
        if s == '+':
            print(a+b)
        elif s == '-':
            print(a-b)
        elif s == '*':
            print(a*b)
        elif s == '/':
            try:
                if a != '0' or b != '0':
                    print(a / b)
            except ZeroDivisionError:
                print('error, not divided by zero')

    elif s == '0':
        break
    else:
        print('error')