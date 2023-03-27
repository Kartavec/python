def division_func(dividend, divider):
    try:
        result = dividend / divider
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        return result    

dividend = float(input('Please, enter the dividend.\t'))
divider = float(input('Please, enter the divider.\t'))


if division_func(dividend, divider) == None:
    print('Please, start the program again.')
else:
    print(f'The result of the action is {division_func(dividend, divider)}')