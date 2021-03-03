# Class 02
# Task 06

products = []

while input("Would you like add product? Enter yes or no: ") == 'yes':
    number = int(input("Enter product number: "))
    characs = {}
    
    while input("Would you like add product parameters? Enter yes or no: ") == 'yes':
        characs_key = input("Enter characs product: ")
        characs_value = input("Enter characs value product: ")
        characs[characs_key] = characs_value
        
    products.append(tuple([number, characs]))
    
print(products)

# products = [(1, {'name': 'comp', 'price': '11'}), (2, {'name': 'pri', 'price': '22'})]

analitics = {}

for prod in products:
    for characs_key, characs_value in prod[1].items():
        if characs_key in analitics:
            analitics[characs_key].append(characs_value)
        else:
            analitics[characs_key] = [characs_value]
         
print(analitics)
