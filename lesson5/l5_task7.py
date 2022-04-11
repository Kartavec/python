import json

with open("text_77.json", 'w', encoding="utf8") as j_file:
    with open("text_7.txt", encoding="utf8") as t_file:
        profit = {e.split()[0]: int(e.split()[2]) - int(e.split()[3]) for e in t_file}
        aw_profit = round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                          len([int(i) for i in profit.values() if int(i) > 0]))
        print(aw_profit)
        res = [profit, {"awerage_profit": aw_profit}]
        json.dump(res, j_file, ensure_ascii=False, indent=4)
