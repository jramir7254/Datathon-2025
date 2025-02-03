from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


full_data = './Raw Data/Data for Hackathon.xlsx'
weather = './Raw Data/El Paso Daily Weather.csv'
weather2 = './Raw Data/Weather_Data.xlsx'

lake_data = pd.read_excel(full_data)

weather_data = pd.read_csv(weather)

weather_data2 = pd.read_excel(weather2)
#weather_data2['date'] = pd.to_datetime(weather_data2['date'])
weather_data2['date'] = pd.to_datetime(weather_data2['date'], format="%Y-%m-%d")

# print(lake_data[0:5])

# print(lake_data['TimeStamp'].dtype)

# print(weather_data[0:5])

print(weather_data2['date'].dtype)

weather_data2.to_excel('./Raw Data/Weather_Data.xlsx', index=False)