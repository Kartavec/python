"""
(вместо задачи 3) Написать функцию thesaurus_adv(),
принимающую в качестве аргументов строки в формате
«Имя Фамилия» и возвращающую словарь, в котором ключи
— первые буквы фамилий, а значения — словари, реализованные
по схеме предыдущего задания и содержащие записи, в которых
фамилия начинается с соответствующей буквы.
"""

def thesaurus_adv(*args):
    """
    get name and surname. return dict() sorted by letter
    """
    tmp = []
    for i in args:
        tmp.append(i)
    tmp.sort(key=lambda letter: letter[i.index(" ")+1])

    for string in tmp:
        surname = string[string.index(" ")+1]
        res = {}
        if d1.get(surname) is None:
            d1[surname] = thesaurus(string, res)
        else:
            d1[surname] = thesaurus(string, d1[surname])


def thesaurus(io, tmp_dict):
    """
    input temporary dictionary and io string. Return finished dictionary with sorted elements
    """
    k = io[0]
    if tmp_dict.get(k) is None:
        temp_lst = [io]
    else:
        temp_lst = tmp_dict.get(k)
        temp_lst.append(io)
        temp_lst.sort(key=lambda let_n: let_n[0])
    tmp_dict[k] = temp_lst
    return tmp_dict


d1 = {}
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Василий Гальперов")
print(d1)

