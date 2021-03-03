# Class 05
# Task 03
# A simple script that creates a text file (not programmatically)
# and writes down last names of employess and their salaries.
# The script tells what employees have salaries less than 20K
# and prints out their names.
# The script also calculates the average salary.

company = {'Connors': 110, 'Benson': 130, 'Genfast': 140, 'Johson': 150}

try:
    file_obj = open("some_file_02.txt", 'w')
    
    for last_name, salary in company.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
        
except IOError:
    
    print("Input-Output error!")
    
finally:
    file_obj.close()
    
total = 0
count = 0
employees = []

with open("some_file_02.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 200:
            employees.append(tokens[0])
        total += int(tokens[1])
        count += 1
result = total / count
print(f"employees: {employees}")
print(f"average salary: {result}")

