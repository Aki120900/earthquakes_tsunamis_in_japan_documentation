import matplotlib.pyplot as plt
import pandas as pd

earthquake_data = {
    1927: 40,
    1948: 1000,
    1964: 80,
    1968: 131,
    1973: 5,
    1978: 865,
    1980: 1,
    1982: 1,
    1983: 800,
    1984: 43,
    1987: 5,
    1993: 1565,
    1994: 170.4,
    1995: 100000,
    2000: 150,
    2001: 500,
    2003: 734,
    2004: 28000,
    2007: 12500,
    2011: 220136.6,
    2014: 2,
    2016: 20100,
    2018: 9000,
    2021: 8250,
    2022: 8800,
    2024: 17600
}

tsunami_data = {
    1964: 80,
    1968: 131,
    1973: 5,
    1978: 865,
    1982: 1,
    1983: 800,
    1993: 1207,
    1994: 170.4,
    1995: 100000,
    2003: 90,
    2011: 220136.6,
    2019: 7700,
    2021: 8800,
    2024: 17600
}

earthquake_df = pd.DataFrame(list(earthquake_data.items()), columns=['Year', 'Total Damage ($Mil)'])
tsunami_df = pd.DataFrame(list(tsunami_data.items()), columns=['Year', 'Total Damage ($Mil)'])

damage_comparison_new = pd.merge(earthquake_df, tsunami_df, on='Year', how='outer', suffixes=('_Earthquake', '_Tsunami')).fillna(0)

plt.figure(figsize=(15, 10))
width = 0.4

plt.bar(damage_comparison_new['Year'] - width/2, damage_comparison_new['Total Damage ($Mil)_Earthquake'], width=width, label='Earthquakes', color='#D9534F')
plt.bar(damage_comparison_new['Year'] + width/2, damage_comparison_new['Total Damage ($Mil)_Tsunami'], width=width, label='Tsunamis', color='#5BC0DE')

plt.xlabel('Year')
plt.ylabel('Total Damage ($Mil)')
plt.title('Comparison of Total Damage by Earthquakes and Tsunamis')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.xticks(damage_comparison_new['Year'], rotation=90)

plt.yscale('log')  # Applying logarithmic scale
plt.yticks([1, 10, 100, 1000, 10000, 100000, 230000], [f'{int(i)}' for i in [1, 10, 100, 1000, 10000, 100000, 230000]])

plt.savefig('Total_Damage_Earthquakes_vs_Tsunamis_Custom_Ticks_Fixed.svg', format='svg')
plt.show()
