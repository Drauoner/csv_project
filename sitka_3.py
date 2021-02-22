#Change file to include all data for 2018
#Change title to daily high
#Add in the lows
#Shade in area between high and low

import csv
from datetime import datetime
import matplotlib.pyplot as plt


open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)



for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)

highs = []
lows = []
dates = []

for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
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

#subplots are a matplotlib feature

fig2, a = plt.subplots(2)

a[0].plot(dates,highs, c='red')
a[1].plot(dates,lows, c='blue')

plt.show()