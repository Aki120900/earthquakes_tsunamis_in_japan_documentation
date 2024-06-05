import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import contextily as ctx

def add_manual_coordinates(df):
    coordinates = {
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

    df['Coordinates'] = df['Location Name'].map(coordinates)
    df = df.dropna(subset=['Coordinates'])
    df.loc[:, 'Latitude'] = df['Coordinates'].apply(lambda x: x[0])
    df.loc[:, 'Longitude'] = df['Coordinates'].apply(lambda x: x[1])
    return df

def plot_geospatial_bubble(file_path):
    earthquakes_data = pd.read_csv(file_path)
    earthquakes_data = add_manual_coordinates(earthquakes_data)
    
    geometry = [Point(xy) for xy in zip(earthquakes_data['Longitude'], earthquakes_data['Latitude'])]
    geo_df = gpd.GeoDataFrame(earthquakes_data, geometry=geometry)
    
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
    
    geo_df.plot(ax=ax, markersize=geo_df['Mag']*30, color='red', alpha=0.5, edgecolor='k')
    ctx.add_basemap(ax, crs=geo_df.crs.to_string(), zoom=5)
    
    ax.set_title("Geospatial Bubble Plot of Earthquakes in Japan (1925-2024)")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    
    plt.show()

# Run the function with the correct path
file_path = '/Users/alexandrapastouchova/Desktop/UAL/Year 2/Visualisation and Sensing - computational practices/Assignment website/earthquakes1925-2024.csv'
plot_geospatial_bubble(file_path)
