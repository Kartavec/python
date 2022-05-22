import json


def write_order_to_json(item, quantity, price, buyer, date):
    my_data = [item, quantity, price, buyer, date]
    keys = list(dict_to_json.keys())
    for i in range(len(my_data)):
        dict_to_json[keys[i]] = my_data[i]
    with open(file_output, "r+", encoding="UTF-8") as f_n:
        data = json.load(f_n)
        data["orders"].append(dict_to_json)
        f_n.seek(0)
        json.dump(data, f_n, indent=4)


if __name__ == "__main__":
    file_output = "orders.json"
    dict_to_json = {"item": "",
                    "quantity": "",
                    "price": "",
                    "buyer": "",
                    "date": ""}
    write_order_to_json("PC", 2, 140000, "Ivanov Ivan Ivanovich", "2022-05-23")
