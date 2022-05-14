def check_typeandcontent(word):
    return print("For element type is ", type(word), " and content is ", word)


print("1st step of check(pure)")
task_words = ["разработка", "сокет", "декоратор"]
for i in task_words:
    check_typeandcontent(i)
print("\n2st step of check(converted)")
task_words_converted = ["\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430",
                        "\u0441\u043e\u043a\u0435\u0442",
                        "\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440"]
for i in task_words_converted:
    check_typeandcontent(i)
