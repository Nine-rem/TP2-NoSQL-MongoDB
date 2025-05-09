from pymongo import MongoClient
MONGO_URI = "mongodb://user1:<password>@localhost"
client = MongoClient(MONGO_URI)
print(client.list_database_names())
