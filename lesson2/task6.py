items_list = [] #конечный список товаров
item_info = {'name' : '', 'price' : '', 'amount' : '', 'measure' : ''}
count = 1 #переменная для записи номера товара по порядку в кортеже
question = ''

#списки для сбора аналитики 
name = []
price = []
amount = []
measure = []

while question != 'quit':
#заполняем информацию о товаре в словарь. 1 товар - 1 словарь
    for keys in item_info.keys ():
        characteristic = input (f'Please, enter the {keys} of item.\n')
        item_info [keys] = characteristic
#сразу добавляем информацию о товаре в списки для сбора аналитики
        if keys == 'name':
            name.append (characteristic)
        elif keys == 'price':
            price.append (characteristic)
        elif keys == 'amount':
            amount.append (characteristic)
        elif keys == 'measure':
            measure.append (characteristic)
#реализуем требуемый вид структуры данных "Товары"
    all_info = (count, item_info)
    items_list.append (all_info)
    count += 1 
    question = input ('Do you want to add one more item? Press enter, '
                       'if you do or enter quit, if you do not.\t')
#выводим построчно структуру данных "Товары"
for k in items_list:
    print (k)    
#реализууем заполнение и вывод стпуктуры данных "Аналитика товаров"
item_info ['name'] = name
item_info ['price'] = price
item_info ['amount'] = amount
item_info ['measure'] = measure

for key, value in item_info.items (): 
    print (f' {key} : {value}')


