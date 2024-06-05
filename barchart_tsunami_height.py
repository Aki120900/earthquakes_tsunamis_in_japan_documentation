import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Given the manual data for maximum water heights
manual_data = {
    'Year': [1927, 1933, 1940, 1944, 1946, 1952, 1964, 1968, 1973, 1983, 1993, 2011, 2024],
    'Maximum Water Height (m)': [11.3, 29, 5, 10, 6.54, 6.54, 5.8, 6, 5.96, 14.93, 32, 39.26, 6.2]
}

manual_df = pd.DataFrame(manual_data)

# Create a bar chart to visualize the manual data
plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")

# Plotting the bar chart without error bars
sns.barplot(x='Year', y='Maximum Water Height (m)', data=manual_df, palette='viridis', ci=None)

plt.title('Maximum Water Height of Tsunamis (1927-2024)')
plt.xlabel('Year')
plt.ylabel('Maximum Water Height (m)')
plt.xticks(rotation=45)
plt.yticks(range(0, 41, 5))

# Show plot
plt.show()
