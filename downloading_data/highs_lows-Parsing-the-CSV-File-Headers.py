import csv

filename = "csv_files/sitka_weather_07-2014.csv"
with open(filename) as f:
    # reads the csv and stores the read info in
    # the reader object \/
    reader = csv.reader(f)
    # shows the first line of the csv file
    header_row = next(reader)
    print(header_row)
