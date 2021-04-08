import pprint

storage =[]

while 1:
    item = input('Введите название товара, цену товара, количество и единицу измерения через запятую или EOF для окончания ввода данных:')
    if not item.upper() == 'EOF':
        item_name, item_price, item_qty, item_unit = tuple(item.split(','))
        if item_price.isalnum() and item_qty.isalnum():
            idx = len(storage)+1
            item_for_arr = (idx, {
                'название': item_name,
                'цена': int(item_price),
                'количество': int(item_qty),
                'ед': 'шт'
                }) 
            storage.append(item_for_arr)
        else:
            print('Введены неверные данные')
    else:      
        display={
                'название':list(set([v for elem in storage for k,v in elem[1].items() if k=='название'])),
                'цена':list(set([v for elem in storage for k,v in elem[1].items() if k=='цена'])),
                'количество':list(set([v for elem in storage for k,v in elem[1].items() if k=='количество'])),
                'ед':list(set([v for elem in storage for k,v in elem[1].items() if k=='ед']))}
        pprint.pprint(display, sort_dicts=False)
