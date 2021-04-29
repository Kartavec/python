earnings = int(input("Enter the company earnings: "))
expenses = int(input("Enter the company expenses: "))
if earnings < expenses:
    print("Your company is non profitable ")

else:
    profit = earnings - expenses
    print(f"Your company's profit is {profit}")
e = int(input("Write the number of employees on your company"))
e = e / profit
print(f"Pforit for 1 employee {e}")