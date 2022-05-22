from chardet import detect
import re
import csv


def coding_detect(file):
    with open(file, "rb") as f_i:
        return detect(f_i.read())['encoding']


def read_correct_file(file, correct_coding):
    with open(file, "r", encoding=correct_coding) as f_i:
        data = f_i.readlines()
    return data


def get_data(array_files):
    for array_f in array_files:
        file_data = read_correct_file(array_f, coding_detect(array_f))
        for i in file_data:
            temp1 = re.search(r"Изготовитель системы", i)
            temp2 = re.search(r"Название ОС", i)
            temp3 = re.search(r"Код продукта", i)
            temp4 = re.search(r"Тип системы", i)
            if temp1:
                i = i.split(":")
                i[1] = i[1].strip("\n").strip()
                os_prod_list.append(i[1])
            elif temp2:
                i = i.split(":")
                i[1] = i[1].strip("\n").strip()
                os_name_list.append(i[1])
            elif temp3:
                i = i.split(":")
                i[1] = i[1].strip("\n").strip()
                os_code_list.append(i[1])
            elif temp4:
                i = i.split(":")
                i[1] = i[1].strip("\n").strip()
                os_type_list.append(i[1])


def fill_data():
    for i in range(3):
        main_data[i+1].append(os_prod_list[i])
        main_data[i+1].append(os_name_list[i])
        main_data[i+1].append(os_code_list[i])
        main_data[i+1].append(os_type_list[i])


def write_to_csv(out_file, data_write):
    with open(out_file, "w", encoding="UTF-8", newline='') as fff:
        f_n_writer = csv.writer(fff, quoting=csv.QUOTE_NONNUMERIC)
        f_n_writer.writerows(data_write)


csv_file = "answer_csv.csv"
file_list = ["info_1.txt", "info_2.txt", "info_3.txt"]
os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []
main_data = [["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"], [], [], []]

if __name__ == "__main__":
    get_data(file_list)
    fill_data()
    write_to_csv(csv_file, main_data)
