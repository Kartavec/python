earnings = int(input("Enter the company earnings: "))
expenses = int(input("Enter the company expenses: "))
if earnings < expenses:
    print("Your company is non profitable ")

else:
    profit = earnings - expenses
    print(f"Your company's profit is {profit}")