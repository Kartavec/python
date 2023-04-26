class My_error(Exception):
    def __init__(self, error):
        self.error = error


dividend = int(input('Enter the dividend.\t'))
divider = int(input('Enter the divider.\t'))

try:
    result = dividend / divider
except:
    err = My_error("Can't divide by zero!")
    print(err)
else:
    print(f'{result}')
