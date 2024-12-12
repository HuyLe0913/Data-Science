
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd
import os 

class DB():
    def __init__(self, username, password, database_name = "cleaned_data"):
        self.data = []
        self.username = username
        self.password = password
        self.database_name = database_name 
        self.status = self.try_to_connect()
    def get_status(self):
        return self.status

    def try_to_connect(self):
        self.uri = f"mongodb+srv://{self.username}:{self.password}@populationcleaneddata.qxgzo.mongodb.net/?retryWrites=true&w=majority&appName=PopulationCleanedData"
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        try:
            self.client.admin.command('ping')
            
            return "Connected"
        except Exception as e:
            
            return str(e)
        
    def change(self, new_username, new_password):
        self.username = new_username
        self.password = new_password
    def read_collection(self, collection_name):
        
        self.database = self.client[self.database_name]
        self.collection = self.database[collection_name]
        data = self.collection.find({})
        first_line = list(data[0].keys())
        first_line.pop(0)
        self.data = first_line
        for doc in data:
            line = list(doc.values())
            line.pop(0)
            self.data.append(line)
        return self.data
    def disconnect(self):
        self.client.close()
    def download_collection(self, collection_name = "cleaned_data"):
        self.database = self.client[self.database_name]
        self.collection = self.database[collection_name]
        documents = self.collection.find({})
        data = pd.DataFrame(list(documents))
        data.drop(columns='_id',inplace=True)
        dir_path = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(dir_path, r"Data\cleaned_data.csv")
        data.to_csv(data_path, index=False)

        print(f"Data downloaded and saved to {data_path} successfully!")
    def upload_collection(self, collection_name = "cleaned_data"):
        self.database = self.client[self.database_name]
        self.collection = self.database[collection_name]
        self.collection.delete_many({})
        dir_path = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(dir_path, r"Data\cleaned_data.csv")
        data = pd.read_csv(data_path)

        documents = data.to_dict(orient='records')
        self.collection.insert_many(documents)

        print("Existing data replaced with new data successfully!")
    def get_role(self, collection_name = "cleaned_data"):
        # Extract role
        user_info = self.client[collection_name].command("usersInfo", {"user": self.username, "db": collection_name})

        # Extract roles
        if "users" in user_info and user_info["users"]:
                user_roles = user_info["users"][0].get("roles", [])
                
        else:
                print(f"User '{self.username}' not found in database.")
        return user_roles

    




    