
import numpy as np
import torch
import torch.nn as nn
import os
import json
import pandas as pd
import math

class NeuralNet(nn.Module):
    def __init__(self):
        super(NeuralNet, self).__init__()

        self.MLP = nn.Sequential(
            nn.Linear(18, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            #nn.Dropout(0.5),

            nn.Linear(512, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            #nn.Dropout(0.5),

            nn.Linear(512, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            #nn.Dropout(0.5),

            nn.Linear(512, 1)
        )


    def forward(self, x):
                    
        return self.MLP(x)

class NeuralNet_for_population_with_year(nn.Module):
    def __init__(self):
        super(NeuralNet_for_population_with_year, self).__init__()
        
        self.MLP = nn.Sequential(
            nn.Linear(19, 256),         
            #nn.BatchNorm1d(128),         
            nn.ReLU(),           
            #nn.Dropout(0.5),            
            
            nn.Linear(256, 256),        
            #nn.BatchNorm1d(256),
            nn.ReLU(),
            #nn.Dropout(0.5),
            
            nn.Linear(256, 256),         
            #nn.BatchNorm1d(128),
            nn.ReLU(),
            #nn.Dropout(0.5),
            
            nn.Linear(256, 1)            
        )


    def forward(self, x):
                    
        return self.MLP(x)
class Predict():
    def __init__(self, life_predict = True):

        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.life_predict = life_predict
        
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        

        if life_predict:
                self.model = NeuralNet()
                self.model.load_state_dict(torch.load(self.script_dir + "\Life_Expectancy_Predictor_1.563MSE_with_Year.pth", map_location=torch.device(self.device), weights_only=True))
                
        else:
                self.model = NeuralNet_for_population_with_year()
                self.model.load_state_dict(torch.load(self.script_dir + "\population_growth%_0.504MSE_with_Year_14_12.pth", map_location=torch.device(self.device), weights_only=True))
                
        self.model.eval()
        self.model = self.model.to(self.device)
        
        
        


    def predict(self, input_dict : dict):
        with open(self.script_dir + "\mean_max_min_dictionary.json", "r") as json_file:
            mean_max_min_dict = json.load(json_file)
        sgd_region_map = {
            'Central and Southern Asia': 1,
            'Europe and Northern America': 2,
            'Australia and New Zealand': 3,
            'Latin America and the Caribbean': 4,
            'Sub-Saharan Africa': 5,
            'Northern Africa and Western Asia': 6,
            'Oceania': 7,
            'Eastern and South-Eastern Asia': 8
        }
        num_regions = len(sgd_region_map)
        feature_columns = [
            'Year', 'Young Age Dependency Ratio', 'Retirement Age Dependency Ratio', 'Population',
            'Male Population Ratio', 'Urban Population Ratio', 'Total Area (sq km)',
            'GDP_per_Capita', 'Infant mortality per 1000 live births', 'BMI']
        log10_cloumns = ['Population', 'Total Area (sq km)', 'GDP_per_Capita', 'Infant mortality per 1000 live births']
        if not self.life_predict:
            feature_columns.append("Life Expectancy")
            

        def one_hot_encode_region(region):
            if not region: #region is none
                return np.zeros(num_regions)
            index = sgd_region_map[region] - 1 
            one_hot_vector = np.zeros(num_regions)
            one_hot_vector[index] = 1
            return one_hot_vector
        value_array = []
        for feature_column in feature_columns:
            
            if input_dict[feature_column] is None:
                input_dict[feature_column] = 0
                value_array.append(input_dict[feature_column])
            else:
                if feature_column not in log10_cloumns:
                    mean_value,max_value,min_value = mean_max_min_dict[feature_column]
                    old_value = input_dict[feature_column]
                    input_dict[feature_column] = (old_value - mean_value) / (max_value - min_value)
                    value_array.append(input_dict[feature_column])
                else:
                    mean_value,max_value,min_value = mean_max_min_dict[feature_column]
                    old_value = np.log10(input_dict[feature_column])
                    input_dict[feature_column] = (old_value - mean_value) / (max_value - min_value)
                    value_array.append(input_dict[feature_column])

        region = input_dict["SDG Region"]
        value_array.extend(one_hot_encode_region(region))
        
        input_for_model = torch.tensor(value_array, dtype=torch.float32).to(self.device).unsqueeze(0)
        return self.model(input_for_model) #có thể lỗi ở chỗ này do array ko đủ features input
    def create_new_json(self, file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\MongoDB\Data\cleaned_data.csv"):
        """
        Reads a CSV file and returns mean, max, and min values of numerical columns.
        Skips columns with NaN values.
        
        Args:
            file_path (str): Path to the CSV file.
            
        Returns:
            result: A dictionary with column names as keys and tuples (mean, max, min) as values.
        """
        try:
            data = pd.read_csv(file_path)
            data = data.sort_values(by=['Country', 'Year'])
            data['Population Growth (%)'] = data.groupby('Country')['Population'].pct_change() * 100
            data['Population Growth (%)'] = data.groupby('Country')['Population Growth (%)'].shift(-1)
            data = data.dropna(subset=['Population Growth (%)'])  
            data = data.drop(columns=['Population Growth (%)'], errors='ignore')  
            result = {}
            log10_cloumns = ['Population', 'Total Area (sq km)', 'GDP_per_Capita', 'Infant mortality per 1000 live births']
            for column in data.columns:
                if pd.api.types.is_numeric_dtype(data[column]):
                    if data[column].isnull().any():
                        print(f"Column '{column}' contains NaN values, all the nan value will be skipped.")
                        values = data[column].values
                        sum,min,max = 0,float("inf"),-float("inf")
                        n = 0
                        for value in values:
                            if not np.isnan(value):
                                sum += value
                                n += 1
                                if value < min:
                                    min = value
                                if value > max: 
                                    max = value
                        result[column] = (round(sum/n,2),max,min)
                        continue
                    if column in log10_cloumns:
                        data[column] = np.log10(data[column])
                    mean_value = data[column].mean()
                    max_value = data[column].max()
                    min_value = data[column].min()
                    result[column] = (mean_value, max_value, min_value)
            
            script_dir = os.path.dirname(os.path.abspath(__file__))
            output_file = "\mean_max_min_dictionary.json"
            with open(script_dir + output_file, "w") as json_file:
                json.dump(result, json_file, indent=4)

            print(f"Dictionary is saved to '{script_dir + output_file}' in the working directory.")
            return result

        except FileNotFoundError:
            print("Check again the path to the csv file.")
            return None
        except Exception as e:
            print(f"{e}")
            return None








