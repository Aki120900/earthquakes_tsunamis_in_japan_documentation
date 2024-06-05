import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'tsunamis1927-2024.csv'
tsunami_data = pd.read_csv(file_path)

# Prepare the data for the time series plot
time_series_data = tsunami_data[['Year', 'Tsunami Magnitude (Iida)']].dropna()
time_series_data.columns = ['Year', 'Magnitude']

# Plot the time series of tsunami magnitudes
plt.figure(figsize=(14, 7))
plt.plot(time_series_data['Year'], time_series_data['Magnitude'], linestyle='-', marker='o', color='b')

# Set major ticks for x-axis for every 5 years in the range
plt.xticks(range(int(time_series_data['Year'].min()), int(time_series_data['Year'].max()) + 1, 1), rotation=90)

plt.title('Time Series of Tsunami Magnitudes (1927-2024)')
plt.xlabel('Year')
plt.ylabel('Magnitude')
plt.grid(True)
plt.tight_layout()
plt.show()
