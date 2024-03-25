import pymongo
from env_loader import get_mongo_uri

uri = get_mongo_uri()

client = pymongo.MongoClient(uri)
database_names = client.list_database_names()
print(database_names)
db = client.looky
collection = db.userss
print(list(collection.find()))
# for user in collection.find():
#     print(user)