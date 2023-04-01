from sys import argv
script_name, work_time, money_per_hour, bonus = argv
work_time = int(work_time)
money_per_hour = int(money_per_hour)
bonus = int(bonus)
salary = work_time * money_per_hour + bonus
print(f'The salary of employee is {salary}$.')