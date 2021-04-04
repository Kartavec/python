store = [
    (1, {
        'название': 'компьютер',
        'цена': 20000,
        'количество': 5,
        'ед': 'шт'
    }),
    (2, {
        'название': 'принтер',
        'цена': 6000,
        'количество': 2,
        'eд': 'шт.'
    }),
    (3, {
        'название': 'сканер',
        'цена': 2000,
        'количество': 7,
        'eд': 'шт.'
    }),
]

display={
        'название':list(set([v for elem in store for k,v in elem[1].items() if k=='название'])),
        'цена':list(set([v for elem in store for k,v in elem[1].items() if k=='цена'])),
        'количество':list(set([v for elem in store for k,v in elem[1].items() if k=='количество'])),
        'ед':list(set([v for elem in store for k,v in elem[1].items() if k=='ед']))}
print(display)
