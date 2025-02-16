# Plotting Dates

import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get dates and high temperatures from file.
filename = "csv_files/death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Three lists to store the dates, highs and lows of the months of the year from the csv file
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(f"{row[0]} missing data")  # Print missing data
        else:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# Plot Data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)  # type: ignore

# Format plot.
plt.title("Daily high temperatures - 2014", fontsize=24)
plt.xlabel("", fontsize=16)

# formats dates to appear diagonally
fig.autofmt_xdate()
diagram_title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(diagram_title, fontsize=20)
plt.tick_params(axis="both", which="major", labelsize=16)
print("\nData : Plotted in new window\n")
plt.show()
