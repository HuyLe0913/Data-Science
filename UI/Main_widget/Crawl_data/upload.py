from pymongo.mongo_client import MongoClient

username = input()
password = input()

uri = f"mongodb+srv://{username}:{password}@populationcleaneddata.qxgzo.mongodb.net/?retryWrites=true&w=majority&appName=PopulationCleanedData"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Error:", e)