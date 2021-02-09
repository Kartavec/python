k = str(input("для ввода данных о товаре нажмите ENTER или введите СТОП для прекращения: "))
i = 1

while k != "СТОП":
    list(mm_tuple)
    name = str(input("введите наименование товара: "))
    price = float(input("введите цену товара: "))
    quant = float(input("введите количество товара: "))
    unit = str(input("введите единицу измерения: "))
    m_dict = dict(name = name, price = price, quantaty = quant, unit = unit)
    mm_tuple = list()
    mm_tuple.append(i)
    mm_tuple.append(m_dict)
    mm_tuple = tuple(mm_tuple)
    i +=1
    k = str(input("продолжить ввод данных? ENTER или СТОП "))
print(mm_tuple)
print(mm_tuple.items())