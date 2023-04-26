class My_error(Exception):
    def __init__(self, error):
        self.error = error

my_list = []
x = ''
while x != 'stop':
    x = input('Please, enter the number or stop for quit.\t')
    try:
        x = int(x)
    except:
        err = My_error("You have entered the string. \
Please, enter the numbers.")
        print(err)
    else:
        x = int(x)
        my_list.append(x)

print(my_list)
