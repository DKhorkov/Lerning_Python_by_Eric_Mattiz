# Упражнениe 16.2.

import csv
from matplotlib import pyplot as plt
from datetime import datetime


def create_highs_and_lows_temperatures(filename, dates, highs, lows):
    """На основе входных данных создает заготовку для визуализации максимальной и минимальной ежедневной температуры."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        name_index = header_row.index('NAME')
        date_index = header_row.index('DATE')
        high_temp_index = header_row.index('TMAX')
        low_temp_index = header_row.index('TMIN')

        for row in reader:
            title = row[name_index]
            date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_temp_index])
                low = int(row[low_temp_index])
            except ValueError:
                print(f'Missing data for {date}.')
            else:
                highs.append(high)
                dates.append(date)
                lows.append(low)
        return title.title()


plt.style.use('seaborn')
fig, ax = plt.subplots()

dates, highs, lows = [], [], []
filename1 = 'data/sitka_2018.csv'
title1 = create_highs_and_lows_temperatures(filename1, dates, highs, lows)
ax.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, alpha=0.3, facecolor='green')

filename2 = 'data/death_valley_2018.csv'
dates, highs, lows = [], [], []
title2 = create_highs_and_lows_temperatures(filename2, dates, highs, lows)
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, alpha=0.3, facecolor='yellow')

# Форматируем диаграмму:
plt.ylabel('Temperature (F)', fontsize=14)
plt.ylim(20, 140)
plt.title(f'Highest and lowest daily temperatures in {title1} (green fill) \nand {title2} (yellow fill) for 2018Y',
          fontsize=16)
fig.autofmt_xdate()
plt.show()
