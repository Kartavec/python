# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

m_file = open('text.txt', 'r')
data = m_file.read()
print(data)
m_file = open('text.txt', 'r')
lines = len(m_file.readlines())
print(f'Количество строк {lines}')
m_file = open('text.txt', 'r')
word_data = m_file.readlines()
for i, j in enumerate(word_data):
    a = j.split()
    print(f'Количество слов в {i + 1} строке равно {len(a)}')

m_file.close()
