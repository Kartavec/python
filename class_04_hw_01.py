# Class 04
# Task 01
# A simple script that takes 3 numbers (hours, pay_per_hour and bonus)
# as positional args.
# The script returns a paycheck calculation
# which is done with a simple formula - (hours * pay per hour + bonus).

from sys import argv

script_name, hours, pay_per_hour, bonus = argv

paycheck = (int(hours) * int(pay_per_hour)) + int(bonus)

print(f"Your paycheck is {paycheck}")

