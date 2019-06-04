import json
import yaml

table = [
    {"first_name" : "John","last_name" : "Smith","location" : "London","online" : "true","followers" : 987},
    {"first_name" : "Jane","last_name" : "South","location" : "New Yor","online" : "true","followers" : 123},
    {"first_name" : "Jill","last_name" : "Silky","location" : "Moscow","online" : "true","followers" : 456}
]

print((json.dumps(table)))
print(json.dumps(table[1]["first_name"]))

with open('write.json', 'w') as file:
    writer = json.dump(table, file, indent=4)

with open('write.json', 'r') as file:
    print(json.load(file))

#json to yaml
with open('write.json') as file:
    reader = json.load(file)

with open('json_to_yaml.yaml', 'w') as file:
    yaml.dump(reader, file)