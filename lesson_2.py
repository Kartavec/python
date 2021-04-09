#Тема “Вычисления с помощью Numpy”
#Задание 1
import numpy as np

a = np.array([[1,6],[2,8],[3,11],[3, 10],[1,7]])
print(a)
a_mean = a.mean(0)
print(a_mean)

#Задание 2
a_centered = a - a_mean
print(a_centered)

#Задание 3
a_centered_sp = np.dot(a_centered[:,0], a_centered[:,1])
print(a_centered_sp)

#Задание 4
N=a.shape[0]
my_cov=a_centered_sp/(N-1)
print(my_cov)

if np.cov(a.transpose())[0,1] == my_cov:
  print('Расчёты верны!')


#Тема “Работа с данными в Pandas”
#Задание 1
import pandas as pd

data = list(zip([1, 2, 3],['Тургенев', 'Чехов', 'Островский']))
print(data)
authors = pd.DataFrame(data,  columns =['author_id', 'author_name'])
print(authors)

data_book=list(zip([1, 1, 1, 2, 2, 3, 3],['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],[450, 300, 350, 500, 450, 370, 290]))
book = pd.DataFrame(data_book,  columns =['author_id', 'book_title', 'price'])
print(book)

#Задание 2
authors_price = pd.merge(authors, book, on = 'author_id', how = 'outer')
print(authors_price)

#Задание 3
top5=authors_price.nlargest(5, 'price')
print(top5)

#Задание 4
authors_stat=authors_price.groupby('author_name').agg({'price': ['min','max','mean']})
print(authors_stat)
