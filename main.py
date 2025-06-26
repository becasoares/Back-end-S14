from pymongo import MongoClient
from dotenv import dotenv_values

mongo_uri = "mongodb+srv://souzaannarebeca:AR146810@cluster0.oaqqlwf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
mongo_client = MongoClient(mongo_uri)

database = mongo_client['database_test']
test_colletion = database['test_colletion']

person = {" name": "Lucca de Enzo", "age": 12}
test_colletion. insert_one(person)

config = dotenv_values('.env')
mongo_uri = config['URI_MONGO_ATLAS']

mongo_clien = MongoClient(mongo_uri)
