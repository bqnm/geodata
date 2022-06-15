import pandas as pd
import matplotlib
import numpy as np
import pprint as p
import re
from geopy.distance import geodesic as GD

pd.set_option('display.max_columns', None)

child = pd.read_csv('./data/childcare_centers.csv', low_memory=False)
address = pd.read_csv('./data/toronto_addresses.csv', low_memory=False)

def pull_geometry(series):
    geometry = eval(series) # Read geometry value as dictionary
    coords = geometry['coordinates'] # Obtain coordinates from geometry value
    return {'longitude': coords[0], 'latitude': coords[1]} # Return longitude and latitude


def add_long_lat(df):
    geometry_dicts = df.geometry.map(pull_geometry).to_list() # Pull geometry from every value and set to list
    geometry_df = pd.DataFrame(geometry_dicts, index=df.index) # Convert list to dataframe
    df = pd.concat([df, geometry_df], axis=1) # Merge both dataframes
    return df

def get_coord(df, index, return_dict=False):
    if return_dict:
        return {'longitude': df['longitude'][index], 'latitude': df['latitude'][index]}
    else:
        return (df['longitude'][index], df['latitude'][index])

def get_distance(p1, p2):
    distance = GD(p1, p2).km
    return distance


child = add_long_lat(child)


## Sample of distance between center 1 and 1000
get_distance(get_coord(child, 1, return_dict=False), get_coord(child, 1000, return_dict=False))

