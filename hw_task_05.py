# task 05
# The user enters the amount of revenue and costs of conpany's operations.
# This simple program calculates if the company works with profit
# It also the ratio of profit to revenue and revenue per employee

revenue = int(input('Enter the amount of revenue: '))

costs = int(input('Enter the amount of costs: '))

profit = revenue - costs

if profit > 0:
    print('The company is profitable!')
else:
    print('The company is NOT profitable!')

staff = int(input('Enter the number of staff: '))

profit_per_employee = profit / staff

print("The company's profit per employee is ", profit_per_employee)




            



