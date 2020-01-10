from pymongo import MongoClient
from pprint import pprint
import pandas as pd

client = MongoClient('localhost',27017)
db = client['game_database']

data = pd.read_csv('gog_games.csv', index_col=0)

def fill_database(database, record_iter):
    games = database.games
    for record in record_iter:
        res = games.insert_one(record)
        print('Inserted id: ', res.inserted_id)

def make_db_request(database, min_price, limit=-1):
    games = database.games
    request = {'final_price': {'$gt': min_price}}
    objects = games.find(request).limit(limit)
    for game in objects:
        pprint(game)


if __name__ == '__main__':
    print('Menu:\n')
    var = input('1 to fill database from gog_games.csv\n2 to make request to db\n')
    if var == 1:
        fill_database(db, iter(data.to_dict('records')))
    elif var == 2:
        price = input('enter minimum dollar price: ')
        make_db_request(db, price, 10)
    else:
        print('unrecognized')

