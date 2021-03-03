# Class 08
# Task 03
# A  script that creates Error class
# (that checks if there are strings and boole operators in lists).


class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        # self.my_list = [int(i) for i in input('Enter symbols with spaces ').split()]
        # val = int(input('Enter symbols and press Enter - '))
        # self.my_list.append(val)
        while True:
            try:
                val = int(input('Enter symbols and press Enter - '))
                self.my_list.append(val)
                print(f'Current list - {self.my_list} \n ')
            except:
                print(f"Forbidden symbols - string and boole operators")
                y_or_n = input(f'Want to try again? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'You quit!'
                else:
                    return f'You quit!'

try_except = Error(1)
print(try_except.my_input())


