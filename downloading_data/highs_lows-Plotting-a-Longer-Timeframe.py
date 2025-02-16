# Plotting Dates

import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get dates and high temperatures from file.
filename = "csv_files/sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Two lists to store the dates and the highs of those days from the csv file
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

# Plot Data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c="red")

# Format plot.
plt.title("Daily high temperatures - 2014", fontsize=24)
plt.xlabel("", fontsize=16)

# formats dates to appear diagonally
fig.autofmt_xdate()

plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
print("\nData : Plotted in new window\n")
plt.show()
