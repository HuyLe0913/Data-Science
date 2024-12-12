# %%
import matplotlib.pyplot as plt
import random
import warnings
import pandas as pd
import seaborn as sns
import plotly.express as px
import os
from io import BytesIO
# %%
script_dir = os.path.dirname(os.path.abspath(__file__))
dic = {}
data = pd.read_csv(script_dir + "\MongoDB\Data\cleaned_data.csv")
data

# %%
data = data.sort_values(by=['Country', 'Year'])
data['Population Growth (%)'] = data.groupby('Country')['Population'].pct_change() * 100
data['Population Growth (%)'] = data.groupby('Country')['Population Growth (%)'].shift(-1)

# %%
data["Population Density"] = data['Population'] / data["Total Area (sq km)"]


class Visualization():
    def __init__(self):
        self.graph = {}

        

        
    def random_countries(self,x,y='Year'):
        random_countries = random.sample(list(data['Country'].unique()), 4)

        fig, axes = plt.subplots(2, 2, figsize=(8, 6))

        for i, country in enumerate(random_countries):
            ax = axes[i // 2, i % 2] 
            country_data = data[data['Country'] == country]
            ax.scatter(country_data[y], country_data[x], color='blue', marker='o')
            ax.set_title(f'{x} vs {y}\n({country})')
            ax.set_xlabel(y)
            ax.set_ylabel(x)
        plt.tight_layout()
        plt.show() 

    def find_extreme_row(self, column_name, extreme='max'):
        if extreme == 'max':
            extreme_value = data[column_name].max()
        elif extreme == 'min':
            extreme_value = data[column_name].min()
        extreme_rows = data[data[column_name] == extreme_value]
        print(f"Row(s) with the {extreme} {column_name}:")
        print(extreme_rows)
        return extreme_rows

    def plot_scatter(self, col_x, col_y = "Life Expectancy",reduce_factor = None,country = None,lower_percentile = 0, upper_percentile = 1,regression = False, save_location = "", plot_only = False):
        warnings.filterwarnings("ignore", message=".*The figure layout has changed to tight.*")
        if lower_percentile>1:
            lower_percentile/=100
        if upper_percentile>1:
            upper_percentile/=100
        data_frame = data
        if reduce_factor:
            if reduce_factor > 1000:
                data_frame = data_frame[data_frame['Year'] == reduce_factor]
            else:
                data_frame = data_frame[data_frame['Year'] % reduce_factor == 0]
        if country:
            data_frame = data_frame[data_frame['Country'] == country]
            data_frame
        if lower_percentile == 0:
            lower_bound = data_frame[col_x].min()
        else:
            lower_bound = data_frame[col_x].quantile(lower_percentile)
        if upper_percentile == 1:
            upper_bound = data_frame[col_x].max()
        else:
            upper_bound = data_frame[col_x].quantile(upper_percentile)
        data_frame = data_frame[(data_frame[col_x] >= lower_bound) & (data_frame[col_x] <= upper_bound)]
        if regression:
            sns.set_style('whitegrid')
            sns.lmplot(x = col_x, y = col_y, data=data_frame,line_kws={'color': 'orange'})
        else:
            plt.scatter(data_frame[col_x], data_frame[col_y], color='blue', marker='o')
        plt.xlabel(col_x)
        plt.ylabel(col_y)
        title = f'{col_y} vs {col_x}\n {round(lower_percentile *100)} - {round(upper_percentile*100)} percentile'
        if country:
            title += f"\n{country}"
        plt.title(title)
        #plt.show()
        #Save fig
        directory = "\Graph\\" + save_location
        filename = f"{col_y} vs {col_x}_{reduce_factor}_{country}_{str(round(lower_percentile *100)).replace('.', r',')}%_{str(round(upper_percentile*100)).replace('.', r',')}%" 
        if save_location not in self.graph.keys():
            self.graph[save_location] = [filename]
        else:
            self.graph[save_location].append(filename)
        filepath = os.path.join(directory, filename)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Make sure the directory exists
        #os.makedirs(directory, exist_ok=True)
        plt.tight_layout()
        if not plot_only:
            plt.savefig(script_dir + filepath + ".png", dpi= 500, bbox_inches='tight')
            
        else:
            buf = BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            plt.close('all')
            return filename, buf
        plt.close('all')
        return filename



    def detect_outliers_by_mean(self, data, column, threshold=3):
        mean = data[column].mean()
        std_dev = data[column].std()
        upper_bound = mean + threshold * std_dev
        lower_bound = mean - threshold * std_dev
        outliers = data[(data[column] > upper_bound) | (data[column] < lower_bound)]
        return outliers, upper_bound, lower_bound
    def get_graph(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        folders = os.listdir(script_dir + "\Graph")
        for save_folder in folders:
            files = os.listdir(script_dir + "\Graph\\" + save_folder)
            for file in files:
                filename = file.split(".")[0] 
                if save_folder not in self.graph.keys():
                    self.graph[save_folder] = [filename]
                else:
                    self.graph[save_folder].append(filename)

        return self.graph
    def get_columns(self):
        return list(data.columns)
    def get_rows(self, column):
        return list(data[column].unique())
Visualization()
    

