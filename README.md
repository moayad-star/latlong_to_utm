# Latitude and Longitude to UTM Converter

## Overview
This Python script converts geographic coordinates (Latitude and Longitude) into UTM (Universal Transverse Mercator) coordinates. It reads a list of coordinates from a specified file, processes them, and outputs the results into an Excel file.

## Features
- Converts Latitude and Longitude to UTM Easting and Northing.
- Outputs results in an Excel file.
- Handles multiple coordinate conversions in a single run.
- Provides error handling for invalid input values.

## Requirements
- Python 3.x
- Required libraries:
  - `utm`
  - `pandas`
  - `tqdm`

You can install the required libraries using pip:

```
pip install utm pandas tqdm
```
## Usage

 1. Prepare a text file containing Latitude and Longitude coordinates. Each coordinate should be on a new line and formatted as latitude,longitude (e.g.` 00.00000, 00.00000`).
 2. Run the script:

`bash`
```
python latlon_to_utm_converter.py
```
3. When prompted, enter the path to your text file containing the coordinates.

## Example

Given a file `coordinates.txt` with the following content:
````
34.0522,-118.2437
40.7128,-74.0060
51.5074,-0.1278
````
Running the script will produce an Excel file with the UTM conversions for the provided coordinates.