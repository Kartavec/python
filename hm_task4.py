from random import choice


def encode_decode(word, coding):
    word = word.encode(coding)
    print(word)
    word = word.decode(coding)
    print(word)


if __name__ == "__main__":
    coding_array = ["utf-8", "utf-16", "utf-32"]
    words_array = ["разработка", "администрирование", "protocol", "standard"]
    my_choise = choice(coding_array)
    for i in words_array:
        encode_decode(i, my_choise)
