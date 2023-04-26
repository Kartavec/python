from sys import argv
script_name, work_time, money_per_hour, bonus = argv

def salary(work_time, money_per_hour, bonus):
   work_time = int(work_time)
   money_per_hour = int(money_per_hour)
   bonus = int(bonus)
   salary_result = work_time * money_per_hour + bonus
   return salary_result

result = salary(work_time, money_per_hour, bonus)
print(f'The salary of employee is {result}$.')
