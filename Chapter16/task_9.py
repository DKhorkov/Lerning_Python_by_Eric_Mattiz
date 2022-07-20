# Упражнение 16.9.

import csv

from plotly.graph_objs import Layout
from plotly import offline
from plotly import colors

for k, v in colors.PLOTLY_SCALES.items():
    print(k, v)

lons, lats, brightness = [], [], []
with open('data/world_fires_1_day.csv') as f:
    reader = csv.reader(f)
    header = next(reader)

    for index, value in enumerate(header):
        print(index, value)

    for row in reader:
        lats.append(float(row[0]))
        lons.append(float(row[1]))
        brightness.append(float(row[2]))


date = [{'type': 'scattergeo',
         'lon': lons,
         'lat': lats,
         'marker': {'size': [bright / 30 for bright in brightness],
                    'color': brightness,
                    'colorscale': 'Hot',
                    'reversescale': True,
                    'opacity': 1,
                    'colorbar': {'title': 'Fire brightness scale'}}
         }]
my_layout = Layout(title='World fires for 1 day')
offline.plot({'data': date, 'layout': my_layout})
