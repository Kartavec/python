import csv
import json
import yaml

with open('1.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open('1.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        print(row.get('articul'))

table = [
    ['articul', 'name', 'price', 'vendor', 'country', 'images'],
    ['UX31E', 'ASUS ZENBOOK', '44400', 'Asus', 'China', 'http://shopexpress.difocus.ru/alboms/3/3/zenbook.jpg'],
    ['MBA-123', '13-inch MacBook Air', '45000', 'Apple', 'China', 'http://shopexpress.difocus.ru/alboms/3/3/apple-air-13.jpg'],
    ['HD-8838', 'Philips Saeco HD 8838', '27462', 'Philips', 'Russia', 'http://shopexpress.difocus.ru/alboms/3/3/saeco-hd-8838.jpg'],
    ['HD-8838', 'Delonghi ECAM 23.210', '27462', 'Delonghi', 'Italy', 'http://shopexpress.difocus.ru/alboms/3/3/delonghi.jpg'],
    ]

with open('1-write.csv', 'w') as file:
    writer = csv.writer(file)
    for row in table:
        writer.writerow(row)

#csv to json
with open('1.csv') as file:
    reader = csv.DictReader(file)
    rows = list(reader)
with open('csv_to_json.json', 'w') as file:
    json.dump(rows, file)

#csv to yaml
with open('1.csv') as file:
    reader = csv.DictReader(file)
    rows = list(reader)
with open('csv_to_yaml.yaml', 'w') as file:
    yaml.dump(rows, file)