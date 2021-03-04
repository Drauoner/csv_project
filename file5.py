# For your 5th python script file -

# Automatic Indexes: We hard coded the indexes corresponding to the TMIN and TMAX
# columns. Use the header row to determine the indexes for these values, so your program can work
# for Sitka or Death Valley. Use the station name to automatically generate an appropriate title
# for your graph as well.

# create 2 subplot graphs in one visualization so you can see both graphs to compare side by side.

# Matplotlib's pyplot API has a convenience function called subplots() which acts as a
# utility wrapper and helps in creating common layouts of subplots, including the
# enclosing figure object, in a single call.

# fig, ax = plt.subplots(2,2)  -  this will create a visualization with 2 charts on it

import csv
from datetime import datetime
import matplotlib.pyplot as plt


open_file = open("death_valley_2018_simple.csv", "r")
open_file2 = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")
csv_file2 = csv.reader(open_file2, delimiter=",")

header_row = next(csv_file)
header_row2 = next(csv_file2)

print(type(header_row))
print(header_row)

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)

highs = []
lows = []
dates = []

for row in csv_file:
    if row[1] == "DEATH VALLEY, CA US":
        try:
            name = row[1]
            high = int(row[4])
            low = int(row[5])
            converted_date = datetime.strptime(row[2], "%Y-%m-%d")
        except ValueError:
            print(f"Missing data for {converted_date}")
        else:
            highs.append(int(row[4]))
            lows.append(int(row[5]))
            dates.append(converted_date)
    else:
        try:
            name = row[1]
            high = int(row[5])
            low = int(row[6])
            converted_date = datetime.strptime(row[2], "%Y-%m-%d")
        except ValueError:
            print(f"Missing data for {converted_date}")
        else:
            highs.append(int(row[5]))
            lows.append(int(row[6]))
            dates.append(converted_date)

highs2, lows2, dates2 = [], [], []

for row in csv_file2:
    if row[1] == "SITKA AIRPORT, AK US":
        try:
            name2 = row[1]
            high = int(row[5])
            low = int(row[6])
            converted_date = datetime.strptime(row[2], "%Y-%m-%d")
        except ValueError:
            print(f"Missing data for {converted_date}")
        else:
            highs2.append(int(row[5]))
            lows2.append(int(row[6]))
            dates2.append(converted_date)
    else:
        try:
            name2 = row[1]
            high = int(row[4])
            low = int(row[5])
            converted_date = datetime.strptime(row[2], "%Y-%m-%d")
        except ValueError:
            print(f"Missing data for {converted_date}")
        else:
            highs2.append(int(row[4]))
            lows2.append(int(row[5]))
            dates2.append(converted_date)

# print(highs)

# fig = plt.figure()
fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle("Temperature comparison between " + name + " and " + name2)
ax1.plot(dates, highs, c="red")
ax1.plot(dates, lows, c="blue")
ax2.plot(dates2, highs2, c="red")
ax2.plot(dates2, lows2, c="blue")

ax1.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
ax2.fill_between(dates2, highs2, lows2, facecolor="blue", alpha=0.1)

ax1.set_title(name, fontsize=16)
ax1.set_xlabel("", fontsize=12)
ax1.set_ylabel("Temperatue (F)", fontsize=12)
ax1.tick_params(axis="both", which="major", labelsize=12)
ax2.set_title(name2, fontsize=16)
ax2.set_xlabel("", fontsize=12)
ax2.set_ylabel("Temperatue (F)", fontsize=12)
ax2.tick_params(axis="both", which="major", labelsize=12)

"""
plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

plt.title(name, fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperatue (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)


plt.plot(dates2, highs2, c="red")
plt.plot(dates2, lows2, c="blue")

plt.fill_between(dates2, highs2, lows2, facecolor="blue", alpha=0.1)

plt.title(name2, fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperatue (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

# plt.show()
"""

# The call to fig.autofmt_xdate() draws the date labels diagnoally to prevent overlapping

fig.autofmt_xdate()

plt.show()
