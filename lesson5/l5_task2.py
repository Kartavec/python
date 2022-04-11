with open("text_2.txt", 'r', encoding="utf8") as file:
    file_array = list(file)
    print(f"В документе {len(file_array)} строк(и)")
    for index, line in enumerate(file_array):
        index += 1
        print(f"В {index} строке {len(line.strip().split())} слов(а)")
