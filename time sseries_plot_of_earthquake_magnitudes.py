import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset
file_path = 'earthquakes1925-2024.csv'
earthquakes_data = pd.read_csv(file_path)

# Prepare the data for the time series plot
time_series_data = earthquakes_data[['Year', 'Mag']].dropna()

# Plot the time series of earthquake magnitudes
plt.figure(figsize=(14, 7))
plt.plot(time_series_data['Year'], time_series_data['Mag'], linestyle='-', marker='o', color='b')

# Set major ticks for x-axis for every year in the range
plt.xticks(range(int(time_series_data['Year'].min()), int(time_series_data['Year'].max()) + 1, 1), rotation=90)

plt.title('Time Series of Earthquake Magnitudes (1925-2024)')
plt.xlabel('Year')
plt.ylabel('Magnitude')
plt.grid(True)
plt.tight_layout()
plt.show()
