import pandas as pd
import matplotlib.pyplot as plt

# Load the files
data = pd.read_excel('Data for Hackathon.xlsx', engine='openpyxl')
weather = pd.read_csv('El Paso Daily Weather.csv')

# Convert to datetime
weather['date'] = pd.to_datetime(weather['date'])
data['TimeStamp'] = pd.to_datetime(data['TimeStamp'])

# Filter only the first 50 rows of data
data = data[(data['Source'] == 'LAKE-1') & (data['Parameter'] == 'NOXTONS') & (data['TimeStamp'].dt.year == 2023)]
print(data)

# Correct filtering of weather data (for January-April 2022)
# weather = weather[(weather['date'].dt.month.isin([1, 2, 3, 4])) & 
#                   (weather['date'].dt.year == 2022)]

# Ensure timestamps are within the same range
weather = weather[weather['date'].isin(data['TimeStamp'])]

print(weather)

# Plot Emissions and Rainfall on the Same Graph
fig, ax1 = plt.subplots(figsize=(10, 5))

# First y-axis (Emissions)
ax1.set_xlabel('Timestamp')
ax1.set_ylabel('Emission Levels', color='blue')
ax1.plot(data['TimeStamp'], data['Value'], label="Emission", marker='o', linestyle='-', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Second y-axis (Rain)
ax2 = ax1.twinx()
ax2.set_ylabel('Precipitation (Rain)', color='red')
ax2.plot(weather['date'], weather['tavg'], label="Rain", marker='s', linestyle='--', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Titles and Labels
plt.title("Emissions vs. Rainfall Over Time")
fig.tight_layout()  # Adjust layout to prevent overlap

# Show Plot
plt.show()
