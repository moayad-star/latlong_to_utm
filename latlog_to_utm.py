import os
import time
import readline
import threading
import utm
import pandas as pd
from tqdm import tqdm


def read_dimensions_from_file(path):
    path = path.replace("'", "")
    path = path.strip()
    with open(path, "r") as f:
        list_dimensions = f.readlines()
    return list_dimensions

def latlon_to_utm(dimensions):
    dimensions = dimensions.split(",")
    latitude = float(dimensions[0].strip())
    longitude = float(dimensions[1].strip())
    data = utm.from_latlon(latitude, longitude)
    data = {
        "Latitude": latitude,
        "Longitude": longitude,
        "UTM Easting": "{:,.2f}".format(data[0]),
        "UTM Northing":"{:,.2f}".format(data[1]),
        "UTM Zone": data[2],
        "Zone_character": data[3]
    }
    return data
    
def main():
    path = str(input("Enter your file path: "))
    list_dimensions = read_dimensions_from_file(path)
    df = pd.DataFrame(columns = [
        "latitude", "longitude", "UTM Easting",
        "UTM Northing", "UTM Zone", "Zone_character"])
    for dimensions in tqdm(list_dimensions):
        try:
            data = latlon_to_utm(dimensions)
            df.loc[len(df)] = [
                data["Latitude"],
                data["Longitude"],
                data["UTM Easting"],
                data["UTM Northing"],
                data["UTM Zone"],
                data["Zone_character"]
            ]
        except (IndexError, ValueError) as e:
            print(f"{e}: value skiped : {dimensions}")

    df.to_excel(
        f"{time.strftime('%H_%M_%S')}.xlsx",
        index=False)
    return None


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        exit(f"\n{e}: User cancel process")
    except UnicodeDecodeError as e:
        exit(f"\n{e}: file type error")