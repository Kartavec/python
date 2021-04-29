a = int(input("Enter the first day running distance: "))
b = int(input("Enter the distance you want to achieve: "))
c = 1
while a < b:
    a = a * 1.1
    c = c + 1
print(c)