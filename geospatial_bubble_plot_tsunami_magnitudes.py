import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import contextily as ctx

# Extend the coordinates dictionary to include all provided locations
extended_coordinates = {
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
    'ARATOZAWA': (38.7239, 140.8433)
}

# Function to add manual coordinates to the dataframe using the extended coordinates
def add_manual_coordinates(df):
    df['Coordinates'] = df['Location Name'].map(extended_coordinates)
    df = df.dropna(subset=['Coordinates'])
    df.loc[:, 'Latitude'] = df['Coordinates'].apply(lambda x: x[0])
    df.loc[:, 'Longitude'] = df['Coordinates'].apply(lambda x: x[1])
    return df

# Function to plot the geospatial bubble plot with basemap
def plot_geospatial_bubble_blue(file_path):
    tsunamis_data = pd.read_csv(file_path)
    tsunamis_data = add_manual_coordinates(tsunamis_data)
    
    geometry = [Point(xy) for xy in zip(tsunamis_data['Longitude'], tsunamis_data['Latitude'])]
    geo_df = gpd.GeoDataFrame(tsunamis_data, geometry=geometry)
    
    # Set CRS to EPSG:4326
    geo_df.set_crs(epsg=4326, inplace=True)
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    
    # Set the bounding box to cover Japan and surrounding areas
    bounds = gpd.GeoSeries([
        Point(122.93457, 24.396308),  # South-West corner
        Point(153.986672, 45.551483)  # North-East corner
    ]).total_bounds
    
    ax.set_xlim(bounds[0], bounds[2])
    ax.set_ylim(bounds[1], bounds[3])
    
    geo_df.plot(ax=ax, markersize=geo_df['Tsunami Magnitude (Iida)'].abs()*30, color='blue', alpha=0.5, edgecolor='k')
    
    # Add the basemap
    ctx.add_basemap(ax, crs=geo_df.crs.to_string(), zoom=5)
    
    ax.set_title("Geospatial Bubble Plot of Tsunamis in Japan (1927-2024)")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    
    plt.show()

# Provide the correct path to your CSV file
file_path = '/Users/alexandrapastouchova/Desktop/UAL/Year 2/Visualisation and Sensing - computational practices/Assignment website/tsunamis1927-2024.csv'
plot_geospatial_bubble_blue(file_path)
