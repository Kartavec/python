import yaml

file_name = "file.yaml"
yaml_list = ['msg_1', 'msg_2', 'msg_3']
yaml_number = 999
yaml_dict = {1 : 1, 2 : 2, 3 : 3, 4 : 4}
DATA_TO_YAML = {'100€': yaml_list, '200€': yaml_number, '300€': yaml_dict}

with open(file_name, "w", encoding="UTF-8") as f_n:
    yaml.dump(DATA_TO_YAML, f_n, default_flow_style=True, allow_unicode=True, indent=4)

with open(file_name, "r", encoding="UTF-8") as f_n:
    data = yaml.load(f_n, Loader=yaml.FullLoader)

if DATA_TO_YAML == data:
    print("OK")

print(data)
print(DATA_TO_YAML)