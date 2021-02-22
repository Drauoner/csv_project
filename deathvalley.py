# handle error checking using try and except
# change file to use death valley data

import csv
from datetime import datetime
import matplotlib.pyplot as plt


open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)

highs = []
lows = []
dates = []

for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for {converted_date}")
    else:
        highs.append(int(row[4]))
        lows.append(int(row[5]))
        dates.append(converted_date)

#print(highs)

fig = plt.figure()



plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

plt.fill_between(dates, highs, lows, facecolor='blue',alpha=.1)

plt.title("Daily High And Low Temperatures For 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperatue (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

#plt.show()




#The call to fig.autofmt_xdate() draws the date labels diagnoally to prevent overlapping

fig.autofmt_xdate()

plt.show()
