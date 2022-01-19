"""
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
Учитывать Заглавную и прописные буквы. (вместо задания 1)
"""

def num_translate(key):
    """ Translate numbers by comparing it's askii values """
    if key.islower():
        print(numbers_dict.get(key))
    else:
        print(numbers_dict.get(key.lower()).capitalize())  # для Заглавных букв.


numbers_dict = {"один": "one", "два": "two",
                "три": "three", "четыре": "four",
                "пять": "five", "шесть": "six",
                "семь": "seven", "восемь": "eight",
                "девять": "nine", "ноль": "zero",
                "one": "один", "two": "два",
                "three": "три", "four": "четыре",
                "five": "пять", "six": "шесть",
                "seven": "семь", "eight": "восемь",
                "nine": "девять", "zero": "ноль",
                "ten": "десять", "десять": "ten"}


num_translate(input("Enter number from zero to ten in english or russian: "))
