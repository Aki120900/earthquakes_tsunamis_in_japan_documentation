import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np




# Coordinates for earthquake and tsunami locations
earthquake_location_to_coords = {
    'HONSHU': (35.6895, 139.6917),
    'RYUKYU ISLANDS': (26.2124, 127.6792),
    'SANRIKU': (39.3315, 141.8828),
    'KASHIMA': (35.9678, 140.6440),
    'HIUGANADA': (31.9000, 131.4167),
    'KYUSHU': (32.7500, 129.8670),
    'HOKKAIDO ISLAND': (43.0642, 141.3468),
    'SEIKAIDO': (34.8020, 135.5153),
    'SHIKOKU': (33.6500, 133.6667),
    'KII PENINSULA': (33.8295, 135.6028),
    'FUKUI': (36.0652, 136.2216),
    'MIYAGI PREFECTURE': (38.2682, 140.8694),
    'IZU PENINSULA': (34.9000, 138.9333),
    'MIYAZAKI': (31.9111, 131.4239),
    'SENDAI': (38.2682, 140.8694),
    'SHIZOUKA PREFECTURES': (34.9756, 138.3828),
    'BONIN ISLANDS': (27.0932, 142.1947),
    'JAPAN TRENCH': (39.2030, 143.9290),
    'HACHIJOJIMA': (33.1111, 139.8000),
    'NAKAGI': (34.8000, 138.2333),
    'MITO': (36.3700, 140.4700),
    'AROSAN': (32.8833, 131.0833),
    'OITA': (33.2381, 131.6126),
    'TOKKAIDO': (35.6895, 139.6917),
    'TOHOKU': (39.7036, 141.1527),
    'HIROSHIMA': (34.3853, 132.4553),
    'IWATE': (39.7036, 141.1527),
    'YOKOHAMA': (35.4437, 139.6380),
    'IBARAKI': (36.3414, 140.4468),
    'NOSHIRO': (40.2039, 140.0247),
    'MIYAKEJIMA': (34.0800, 139.5300),
    'TOTTORI': (35.5011, 134.2351),
    'OKINAWA': (26.2124, 127.6792),
    'CHIBA PERFECTURE': (35.6073, 140.1063),
    'AOMORI PREFECTURE': (40.8246, 140.7406),
    'HOKKADIO, KUSHIRO, HACHINOHE, HONSHU': (41.7688, 140.7288),
    'HONSHU, ISHIKAWA, TOYAMA, NIIGATA': (37.9022, 139.0236),
    'KOBE': (34.6901, 135.1955),
    'HONSHU, KOBE, AWAJI-SHIMA, NISHINOMIYA': (34.7264, 135.3132),
    'NIIGATA PREFECTURE': (37.9022, 139.0236),
    'VOLCANO ISLANDS': (24.2833, 141.3000),
    'KOZU-SHIMA': (34.2167, 139.1333),
    'NII-JIMA': (34.3731, 139.2661),
    'OKAYAMA': (34.6550, 133.9194),
    'HIROSHIMA, OKAYAMA, HONSHU, KAGAMA': (34.3963, 132.4594),
    'IWATE, MIYAGI, YAMAGATA, AKITA': (39.7036, 141.1527),
    'MIYAGI, IWATE': (38.2682, 140.8694),
    'ATSUGI': (35.4389, 139.3597),
    'KYOTO': (35.0116, 135.7681),
    'KYOTO, WAKAYAMA, SAKAI': (34.2260, 135.1675),
    'FUKUOKA': (33.5904, 130.4017),
    'IZU ISLANDS': (34.2025, 139.4297),
    'NAGANO': (36.6513, 138.1810),
    'CHICHIJIMA ISLAND': (27.1000, 142.2000),
    'KYUSYU ISLAND': (32.7500, 129.8670),
    'KUMAMOTO': (32.8031, 130.7079),
    'KURAYOSHI': (35.4302, 133.8222),
    'SHIMANE PREFECTURE': (35.4723, 133.0505),
    'OSAKA': (34.6937, 135.5023),
    'FUKUSHIMA': (37.7500, 140.4670),
    'ISHIKAWA PREFECTURE': (36.5940, 136.6256),
}

tsunami_location_to_coords = {
    'HONSHU ISLAND': (35.6895, 139.6917),
    'SANRIKU': (39.3315, 141.8828),
    'KASHIMA': (35.9678, 140.6440),
    'HIUGANADA': (31.9000, 131.4167),
    'SEIKAIDO': (34.8020, 135.5153),
    'HONSHU': (36.2048, 138.2529),
    'HOKKAIDO ISLAND': (43.0642, 141.3468),
    'RYUKYU ISLANDS': (26.2124, 127.6792),
    'FUKUSHIMA PREFECTURE': (37.7500, 140.4670),
    'KII PENINSULA': (33.8295, 135.6028),
    'TOKAIDO': (34.7303, 137.3833),
    'MIYAGI': (38.2682, 140.8694),
    'IZU PENINSULA': (34.9000, 138.9333),
    'AICHI PREFECTURE': (35.1803, 136.9066),
    'SEIKAIDO-NANKAIDO': (33.9500, 134.0333),
    'JAPAN TRENCH': (39.2030, 143.9290),
    'HACHIJO ISLAND': (33.1150, 139.7875),
    'HACHIJOJIMA': (33.1111, 139.8000),
    'CHICHI JIMA': (27.0932, 142.1947),
    'IWATE': (39.7036, 141.1527),
    'IBARAKI': (36.3414, 140.4468),
    'NOSHIRO': (40.2039, 140.0247),
    'OKINAWA': (26.2124, 127.6792),
    'KYUSHU': (32.7500, 129.8670),
    'KYUSHU ISLAND': (32.7500, 129.8670),
    'AOMORI PREFECTURE': (40.8246, 140.7406),
    'BONIN ISLANDS': (27.0932, 142.1947),
    'TOHUKU': (39.7036, 141.1527),
    'KOBE': (34.6901, 135.1955),
    'KOZU-SHIMA ISLAND': (34.2167, 139.1333),
    'NIIGATA': (37.9022, 139.0236),
    'NOTO PENINSULA': (37.4500, 137.3000),
    'IZU ISLANDS': (34.2025, 139.4297),
    'ARATOZAWA': (38.7239, 140.8433),
}


# Load your datasets
earthquakes_df = pd.read_csv('earthquakes1925-2024.csv')
tsunamis_df = pd.read_csv('tsunamis1927-2024.csv')

# Map coordinates
earthquakes_df['Coordinates'] = earthquakes_df['Location Name'].map(earthquake_location_to_coords)
tsunamis_df['Coordinates'] = tsunamis_df['Location Name'].map(tsunami_location_to_coords)

# Safely split 'Coordinates' into 'Lat' and 'Long'
earthquakes_df[['Lat', 'Long']] = pd.DataFrame(earthquakes_df['Coordinates'].tolist(), index=earthquakes_df.index)
tsunamis_df[['Lat', 'Long']] = pd.DataFrame(tsunamis_df['Coordinates'].tolist(), index=tsunamis_df.index)

# Create a plot with Cartopy
fig, ax = plt.subplots(figsize=(15, 10), subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_extent([122, 153, 24, 46])  # Japan area

# Add geographic features
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.OCEAN, facecolor='#a6bddb')
ax.add_feature(cfeature.LAND, facecolor='#dddddd')

# Plotting using Matplotlib directly to avoid compatibility issues
ax.scatter(
    earthquakes_df['Long'], earthquakes_df['Lat'],
    color='red', label='Earthquakes', alpha=0.7, s=200,  # Adjust the size with the `s` parameter
    transform=ccrs.PlateCarree(), edgecolor='black'
)
ax.scatter(
    tsunamis_df['Long'], tsunamis_df['Lat'],
    color='blue', label='Tsunamis', alpha=0.5, s=200,  # Adjust the size with the `s` parameter
    transform=ccrs.PlateCarree(), edgecolor='black'
)

plt.title('Geospatial Plot of Earthquake and Tsunami Occurrences (1925-2024)', fontsize=15)
plt.legend(loc='upper left')
plt.show()
