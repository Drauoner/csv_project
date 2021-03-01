#For your 5th python script file - 

#Automatic Indexes: We hard coded the indexes corresponding to the TMIN and TMAX
#columns. Use the header row to determine the indexes for these values, so your program can work
#for Sitka or Death Valley. Use the station name to automatically generate an appropriate title
#for your graph as well.

#create 2 subplot graphs in one visualization so you can see both graphs to compare side by side.

#Matplotlib's pyplot API has a convenience function called subplots() which acts as a
#utility wrapper and helps in creating common layouts of subplots, including the
#enclosing figure object, in a single call.

# fig, ax = plt.subplots(2,2)  -  this will create a visualization with 2 charts on it

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
