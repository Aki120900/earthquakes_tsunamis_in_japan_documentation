import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Load the dataset
file_path = '/Users/alexandrapastouchova/Desktop/UAL/Year 2/Visualisation and Sensing - computational practices/Assignment website/earthquakes1925-2024.csv'
earthquake_data = pd.read_csv(file_path)

# Filter relevant columns and handle missing values by replacing them with zeros
filtered_data = earthquake_data[['Deaths', 'Missing', 'Injuries', 'Damage ($Mil)', 'Houses Destroyed', 'Houses Damaged']].fillna(0)

# Calculate the total values for each of the selected columns
total_values = filtered_data.sum()

# Prepare data for the radar chart
totals = total_values.tolist()
totals += totals[:1]  # Complete the loop

# Categories for the radar chart
categories = list(total_values.index)
num_vars = len(categories)

# Compute angle of each axis
angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
angles += angles[:1]

# Re-plotting the radar chart with further adjustments for better clarity of specific annotations
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one axe per variable + add labels
plt.xticks(angles[:-1], categories, color='blue', size=8)

# Draw y-labels
ax.set_rlabel_position(0)
plt.yticks([1000, 10000, 100000, 1000000, 10000000], ["1K", "10K", "100K", "1M", "10M"], color="grey", size=7)
plt.ylim(0, max(totals))

# Plot data
ax.plot(angles, totals, linewidth=2, linestyle='solid')

# Fill area
ax.fill(angles, totals, 'b', alpha=0.1)

# Add dots at the vertices
ax.scatter(angles[:-1], totals[:-1], color='black', s=50, zorder=10)

# Annotate the total values with positions following the user's directions
for i in range(num_vars):
    angle_rad = angles[i]
    value = totals[i]
    # Adjust the position of the text according to the user's directions
    offset = max(totals) * 0.1
    if i == 3:  # Specific adjustment for 'Damage ($Mil)'
        ax.text(angle_rad, value + offset * 2.5, f"{value:.2f}", horizontalalignment='center', size=8, color='red')
    elif i == 4:  # Specific adjustment for 'Houses Destroyed'
        ax.text(angle_rad - pi / 24, value + offset, f"{value:.2f}", horizontalalignment='center', size=8, color='red')
    elif i == 5:  # Specific adjustment for 'Houses Damaged'
        ax.text(angle_rad + pi / 24, value - offset, f"{value:.2f}", horizontalalignment='center', size=8, color='red')
    elif i == 1:  # Adjustment for 'Missing'
        ax.text(angle_rad, value + max(totals) * 0.15, f"{value:.2f}", horizontalalignment='center', size=8, color='red')
    elif i == 2:  # Adjustment for 'Deaths'
        ax.text(angle_rad, value - max(totals) * 0.3, f"{value:.2f}", horizontalalignment='center', size=8, color='red')
    else:
        ax.text(angle_rad, value + offset, f"{value:.2f}", horizontalalignment='center', size=8, color='red')

# Highlight the section with the highest total value
max_value_index = totals.index(max(totals[:-1]))  # Exclude the duplicated first/last value
ax.fill([angles[max_value_index], angles[max_value_index + 1]], [0, max(totals)], 'red', alpha=0.1)

# Title
plt.title('Total Earthquake Impacts (1925-2024)', size=15, color='black', y=1.1)

# Show the plot with adjusted annotations
plt.show()
