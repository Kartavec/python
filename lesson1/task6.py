cost = int(input('Please, enter cost value in $.\n'))
revenue = int(input('Please, enter profit value in $.\n'))

if revenue > cost:
    profitability = (revenue - cost)/revenue
    empl_num = int(input('How many employees does your company have?\n'))
    prof_per_empl = (revenue - cost)/empl_num
    print (f'The profit per employee is {prof_per_empl}$.')
else:
    print ('Unfortunately, the cost is not less than the revenue.')