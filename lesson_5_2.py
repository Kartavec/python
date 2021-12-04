# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
import re


with open('lesson_5_2.txt', encoding='utf-8') as f:
    str_cnt = 0
    wrd_cnt = []
    for line in f.readlines():
        str_cnt += 1
        wrd_cnt.append(len(re.findall(r'\w+', line)))

print(f'Количество строк в файле: {str_cnt}')
[print(f'Строка {i+1}: слов в строке - {wrd_cnt[i]}') for i in range(len(wrd_cnt))]
