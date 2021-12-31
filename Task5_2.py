"""
Создать список, содержащий цены на товары (10–20 товаров), например: [57.8, 46.51, 97, ...]
Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5
руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек
или 0 копеек (должно быть 07 коп или 00 коп).
Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после
сортировки остался тот же).
Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
"""


def prising(listing):
    new_prices = list()
    for i, price in enumerate(listing):
        rubles = int(price)
        cents = int(round((price - rubles)*100))
        new_prices.append (f'{rubles} руб {cents:02} коп')
    print(str(new_prices))


prise_list = [57.8, 46.51, 9.7, 34, 11.23, 86.45, 38, 2, 43, 90.2, 30, 455, 36, 22.45, 451.54, 123, 43.2, 1.6]
print('ID of price list:', id(prise_list))
prising(prise_list)
prise_list.sort()
print('ID of sorted price list:', id(prise_list))
prising(prise_list)
print("Reverse sorted list:")
prise_list.sort(reverse=True)
prising(prise_list)
print("Max 5 values:")
prising(prise_list[:5])  # 5 максимальных значений
