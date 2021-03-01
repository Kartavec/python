# Class 05
# Task 05
# A script that creates a text file, writes down a few numbers separated by spaces.
# The script reads the numbers, sums them up and prints the sum out on the screen.

def cal_total():
    
    try:
        with open('s_file.txt', 'w+') as file_obj:
            line = input('Enter a few intergers divided by spaces: \n')
            file_obj.writelines(line)
            some_nums = line.split()

            print(sum(map(int, some_nums)))
            
    except IOError:
        print('File error')
        
    except ValueError:
        print('Wrong number. It must an integer. Input-Output error!')

cal_total()
