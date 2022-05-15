from random import choice
from chardet import detect


def make_file():
    with open(file_name, "w", encoding=my_choice) as f:
        f.writelines(words_array)


def what_is_encoding():
    with open(file_name, "rb") as f:
        data = f.read()
    return detect(data)['encoding']


def open_correct(correct_code):
    print("Correct encoding is", correct_code)
    with open(file_name, "r", encoding=correct_code) as f:
        data = f.read()
    print(data)


if __name__ == "__main__":
    file_name = "test_file.txt"
    coding_array = ["utf-8", "utf-16", "utf-32"]
    words_array = ["сетевое программирование\n", "сокет\n", "декоратор"]
    my_choice = choice(coding_array)
    make_file()
    open_correct(what_is_encoding())
