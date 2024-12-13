import pandas as pd
import json
import os
from Predict_engine.infer_life_expectancy import Predict
# Read the created CSV file
processed_data = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + "\MongoDB\\Data\\distinct_countries_highest_year.csv")

# Initialize a list to hold dictionaries for each country's data
ouput_dict_list = []

# Define the range of years to generate versions for
base_year = 2016
num_versions = 10

# Iterate through each row in the processed dataset
for _, row in processed_data.iterrows():
    for i in range(num_versions):
        country = row["Country"]
        year = base_year + i
        input_dict = {
            "Year": year,
            "Young Age Dependency Ratio": row["Young Age Dependency Ratio"],
            "Retirement Age Dependency Ratio": row["Retirement Age Dependency Ratio"],
            "Population": row["Population"],
            "Male Population Ratio": row["Male Population Ratio"],
            "Urban Population Ratio": row["Urban Population Ratio"],
            "Total Area (sq km)": row["Total Area (sq km)"],
            "GDP_per_Capita": row["GDP_per_Capita"],
            "Infant mortality per 1000 live births": row["Infant mortality per 1000 live births"],
            "BMI": row["BMI"],
            "SDG Region": row["SDG Region"],
            "Life Expectancy": row["Life Expectancy"],

        }
        pre = Predict(life_predict = False, year = True)
        ans = pre.predict(input_dict)
        ouput_dict = {"Country" : country, "Year": year, "Predict" : round(ans.item(), 2)}

        ouput_dict_list.append(ouput_dict)
df = pd.DataFrame(ouput_dict_list)
# Save the DataFrame to a CSV file
df.to_csv(os.path.dirname(os.path.abspath(__file__)) + "\Predict_engine\\population_growth_predict.csv", index=False)
# Display a sample of the generated input dictionaries

