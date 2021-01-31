# task 06
# The user enters the number of kilometers (a) a runner covers on the 1st day.
# Every day the runner increases his result by 10%
# The user should define the number of day when the runner should cover
# the desired number of kilometers (b)

a = int(input('Enter the number of kilometers a runner covers on the 1st day: '))
b = int(input('Enter the number of kilometers a runner wants to run on the last day: '))

if a >= b:
    print('The number of kilometers a runner wants to run on the last day should more than on the 1st day!')
    a = int(input('Enter the number of kilometers a runner covers on the 1st day: '))
    b = int(input('Enter the number of kilometers a runner wants to run on the last day: '))

diary = []

while a < b:
    a *= 1.1
    diary.append(a)

for i in diary:
    print(i)

    

    
    





    





