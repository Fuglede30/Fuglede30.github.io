import pandas as pd
import numpy as np

def load_data(file, weather_mapping):

    df = pd.read_csv(file)

    # Convert to datetime
    df["StartTime"] = pd.to_datetime(df["StartTime"])

    df["EndTime"] = df["EndTime"].str[:-10] #Remove the time offset from UTC
    df["EndTime"] = pd.to_datetime(df["EndTime"], format="%Y-%m-%dT%H:%M:%S") # Convert to datetime 

    df = df.drop(['LocalTimeZone', 'WeatherStation_AirportCode'], axis = 1)

    df['Congestion Ratio'] = np.where(
    df['DelayFromFreeFlowSpeed(mins)'] == 0,
    0,
    df['DelayFromTypicalTraffic(mins)'] / df['DelayFromFreeFlowSpeed(mins)']
    )

    df['Weather Condition Map'] = df['Weather_Conditions'].replace(weather_mapping)
    # Reverse mapping to look up new category for each raw label
    #category_lookup = {condition: category for category, conditions in weather_mapping.items() for condition in conditions}

    # Apply mapping
    #df["Weather Condition Map"] = df['Weather Conditions Map'].map(category_lookup).fillna('Other').unique()

    return df