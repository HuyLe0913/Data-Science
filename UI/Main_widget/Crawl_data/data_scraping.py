import requests
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def getData(url,name):
    response = requests.get(url)
    data = response.json()
    data_list = []
    for entry in data[1]:
        if entry["value"] is not None:
            data_list.append({
                "Country": entry["country"]["value"],
                "Year": entry["date"],
                name: entry["value"]
            })
    data_df = pd.DataFrame(data_list)
    print(data_df)
    data_df.to_csv(os.path.dirname(os.path.abspath(__file__)) + f"\Data\\{name}.csv", index=False)
def getUrl(code,num_page = 20000):
    return f"http://api.worldbank.org/v2/country/all/indicator/{code}?format=json&per_page={num_page}"

population_url = getUrl("SP.POP.TOTL")
male_ratio_url = getUrl("SP.POP.TOTL.MA.ZS")
urban_population = getUrl("SP.URB.TOTL.IN.ZS")
gdp_url = getUrl("NY.GDP.PCAP.CD")
area_url = getUrl("AG.SRF.TOTL.K2")
old_url = getUrl("SP.POP.DPND.OL")
young_url = getUrl("SP.POP.DPND.YG")
life_url = getUrl("SP.DYN.LE00.IN")

getData(population_url,"Population")
getData(male_ratio_url,"Male Population Ratio")
getData(urban_population,"Urban Population Ratio")
getData(gdp_url,"GDP_per_Capita")
getData(area_url,"Total Area (sq km)")
getData(old_url,"Retirement Age Dependency Ratio")
getData(young_url,"Young Age Dependency Ratio")
getData(life_url,"Life Expectancy")
#WHO
who_url = "https://ghoapi.azureedge.net/api/Indicator"
response = requests.get(who_url)

indicators_df = pd.DataFrame(response.json()['value'])
bmi_indicators_df = indicators_df[indicators_df['IndicatorName'].str.contains('bmi', case=False)]
print(bmi_indicators_df)

bmi_indicator_code = 'NCD_BMI_MEAN'
bmi_url = f"https://ghoapi.azureedge.net/api/{bmi_indicator_code}"
response = requests.get(bmi_url)
data = response.json()
bmi_data_df = pd.DataFrame(data['value'])
print("Data for NCD_BMI_MEAN:")
print(bmi_data_df)
bmi_data_df.to_csv(os.path.dirname(os.path.abspath(__file__)) + "\Data\\bmi_data.csv")
#Selenium
webdriver_path = os.path.dirname(os.path.abspath(__file__)) + "\edgedriver_win64\\msedgedriver.exe"  # replace with actual path
service = Service(webdriver_path)
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)

country_code_url = "https://wits.worldbank.org/wits/wits/witshelp/content/codes/country_codes.htm"
driver.get(country_code_url)
time.sleep(5)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table.wt1')))

table = driver.find_element(By.CSS_SELECTOR, 'table.wt1')

rows = table.find_elements(By.TAG_NAME, 'tr')
data = []
for row in rows[2:]:
    cols = [col.text for col in row.find_elements(By.TAG_NAME, 'td')]
    if cols:  # Check if cols is not empty
        data.append(cols)
df = pd.DataFrame(data, columns=["Country","ISO3","Code"])
print(df)
df.to_csv(os.path.dirname(os.path.abspath(__file__)) + "\Data\\country_codes.csv", index=False)

sdg_url = "https://ourworldindata.org/grapher/world-regions-sdg-united-nations?tab=table"
driver.get(sdg_url)
time.sleep(5)
table = driver.find_element(By.CLASS_NAME, 'table-wrapper')
headers = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]

rows = table.find_elements(By.TAG_NAME, 'tr')
data = []
for row in rows[1:]:
    cols = [col.text for col in row.find_elements(By.TAG_NAME, 'td')]
    data.append(cols)

df = pd.DataFrame(data, columns=headers)
print(df)
df.to_csv(os.path.dirname(os.path.abspath(__file__)) + "\Data\\world_regions_sdg.csv", index=False)

infant_url = r"https://data.un.org/Data.aspx?q=infant&d=PopDiv&f=variableID%3a77"
driver.get(infant_url)

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.DataContainer')))
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox'][value]")

for checkbox in checkboxes:
    try:
        year = int(checkbox.get_attribute('name'))
    except ValueError as e:
        continue
    if year <= 2024:
        if not checkbox.is_selected():
            driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
            time.sleep(1)
            checkbox.click()


apply_filters_link = driver.find_element(By.ID, "ctl00_main_filters_anchorApplyBottom")
apply_filters_link.click()

time.sleep(5) 
all_data = []
def scrape_table():
    data_container = driver.find_element(By.CSS_SELECTOR, 'div.DataContainer')
    headers = [header.text for header in data_container.find_elements(By.TAG_NAME, 'th')]
    rows = data_container.find_elements(By.TAG_NAME, 'tr')
    page_data = []
    for row in rows[1:]:
        cols = [col.text for col in row.find_elements(By.TAG_NAME, 'td')]
        page_data.append(cols)
    
    return headers, page_data

while True:
    headers, page_data = scrape_table()
    all_data.extend(page_data)
    try:
        next_button = driver.find_element(By.ID, "linkNextB")
        if 'disabled' in next_button.get_attribute('class'):
            break
        next_button.click()
        time.sleep(5)
    except Exception as e:
        print(f"Reached the last page or encountered an error: {e}")
        break

df = pd.DataFrame(all_data, columns=headers)
print(df)
df.to_csv(os.path.dirname(os.path.abspath(__file__)) + "\Data\\Infant Mortality.csv", index=False)
driver.quit()
