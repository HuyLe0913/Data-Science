import pandas as pd
from pymongo import MongoClient
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(dir_path,r"Data\cleaned_data.csv")

db_username = input()
db_password = input()

client = MongoClient(f'mongodb+srv://{db_username}:{db_password}@populationcleaneddata.qxgzo.mongodb.net/?retryWrites=true&w=majority&appName=PopulationCleanedData')

db = client["cleaned_data"]
collection = db["cleaned_data"]

collection.delete_many({})

data = pd.read_csv(data_path)

documents = data.to_dict(orient='records')
collection.insert_many(documents)

print("Existing data replaced with new data successfully!")