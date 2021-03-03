# Class 05
# Task 01
# A simple script that creates a text file programmatically
# and writes down data entered line by line by the user.
# A blank line signifies the end of the script.

some_file = open('some_file.txt', 'w')
some_line = input("Enter some text: \n")

while some_line:
    some_file.writelines(some_line)
    some_line = input("Enter some text: \n")
    if not some_line:
        break

some_file.close()

some_file = open('some_file.txt', 'r')
text = some_file.readlines()
print(text)

some_file.close()



    
    

