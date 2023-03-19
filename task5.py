cost = int(input('Please, enter cost value.\n'))
revenue = int(input('Please, enter profit value.\n'))
if revenue > cost:
    print('The company makes a profit. You are doing great! ')
elif revenue < cost:
    print('The company makes a lesion. You have to work harder!')
else:
    print('The profit and cost value are equal.')