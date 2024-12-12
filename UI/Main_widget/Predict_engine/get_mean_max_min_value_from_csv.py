import pandas as pd
import json
import os
import numpy as np
def process_csv(file_path):
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
        result = {}

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
    


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    file_path = os.path.dirname(script_dir) + "\MongoDB\Data\cleaned_data.csv"  
    result = process_csv(file_path)
    
    if result:
        print("Processed Results:", result)

