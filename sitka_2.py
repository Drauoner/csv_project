import csv
from datetime import datetime


open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)

highs = []

for row in csv_file:
    highs.append(int(row[5]))

#print(highs)

import matplotlib.pyplot as plt

plt.plot(highs, c="red")
plt.title("Daily High Temperatures, July 2018", fontsize=16)
plt.xlabel("", fontsize=16)
plt.ylabel("Temperatue (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

#plt.show()




#The call to fig.autofmt_xdate() draws the date labels diagnoally to prevent overlapping

fig.autofmt_xdate()

plt.show()