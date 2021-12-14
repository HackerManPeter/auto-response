import json
from pymongo import MongoClient

client = MongoClient()
db = client.gdsc
collection = db.members

with open(r'data.json') as file:
    for obj in file:
        my_dict = json.loads(obj)
collection.insert_many(my_dict)

