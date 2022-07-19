# Упражнения 16.1 и 16.4.
import csv
from matplotlib import pyplot as plt
from datetime import datetime


def prcp_ratio(filename, dates_list, prcp_list):
    """Создает из данных заготовку для визуализации рейтинга PRCP."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        print(header_row)

        # Для целей упражнения 16.4:
        date_index = header_row.index('DATE')
        prcp_es_index = header_row.index('PRCP')
        name_index = header_row.index('NAME')

        for row in reader:
            date = datetime.strptime(row[date_index], '%Y-%m-%d')
            title_name = row[name_index]
            try:
                prcp = float(row[prcp_es_index])
            except ValueError:
                print(f'Missing data for {date}.')
            else:
                dates_list.append(date)
                prcp_list.append(prcp)
        return title_name.title()


filename1 = 'data/sitka_2018.csv'
dates, prcp_es = [], []
title1 = prcp_ratio(filename1, dates, prcp_es)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, prcp_es, c='green', linewidth=2, alpha=0.5)


filename2 = 'data/death_valley_2018.csv'
dates, prcp_es = [], []
title2 = prcp_ratio(filename2, dates, prcp_es)
plt.plot(dates, prcp_es, c='red', linewidth=2)
plt.title(f'PRCP ratio per day in {title1} (green) and {title2} (red) for 2018Y')  # Упражнение 16.4.
fig.autofmt_xdate()
plt.show()
