import os
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.io as pio

data = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + "\Predict_engine\population_growth_predict.csv")
# Unique years in the dataset
unique_years = data['Year'].unique()

# Create and save a choropleth map for each year
output_base_path = os.path.dirname(os.path.abspath(__file__)) + "/World_map"
os.makedirs(output_base_path, exist_ok=True)

for year in unique_years:
    # Filter data for the specific year
    year_data = data[data['Year'] == year]
    
    # Create the choropleth map
    fig = px.choropleth(
        year_data,
        locations="Country",
        locationmode="country names",
        color="Predict",
        title=f"Population Growth ({year})",
        color_continuous_scale="Plasma",
        labels={"Predict": "Population growth(%)"}
    )
    fig.update_layout(
        coloraxis_colorbar=dict(
            orientation='h', # Set horizontal orientation
            x=0.5,           # Position it at the center
            xanchor='center',
            y=-0.2,      # Move it below the plot
            thickness=20,    # Adjust the thickness (height in horizontal orientation)
            len=1
        )
    )
    # Define output folder for the year
    year_folder = os.path.join(output_base_path, str(year))
    os.makedirs(year_folder, exist_ok=True)
    
    # Save the figure
    output_path = os.path.join(year_folder, f"PopulationGrowth_{year}.png")
    pio.write_image(fig, output_path, format='png', width=700, height=550)


output_base_path
