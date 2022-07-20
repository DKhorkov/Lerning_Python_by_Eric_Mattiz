# Упражнения 16.6 - 16.8.
# Ссылка https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
import json
from plotly.graph_objs import Layout
from plotly import offline

with open('data/last_week_eq.json') as f:
    readable = json.load(f)

with open('data/readable_lw_eq.json', 'w') as f:
    json.dump(readable, f, indent=4)

with open('data/readable_lw_eq.json') as f:
    all_data = json.load(f)

all_dicts = all_data['features']
title = all_data['metadata']['title']

mags, lons, lats, places = [], [], [], []
for d in all_dicts:
    mags.append(d['properties']['mag'])
    lons.append(d['geometry']['coordinates'][0])
    lats.append(d['geometry']['coordinates'][1])
    places.append(d['properties']['place'])

data = [{'type': 'scattergeo',
         'text': places,
         'lon': lons,
         'lat': lats,
         'marker': {'size': [5 * mag if mag > 0 else 0.1 for mag in mags],  # 0.1 для отрицательных магнитуд.
                    'color': mags,
                    'colorscale': 'Electric',
                    'reversescale': True,
                    'opacity': 1,
                    'colorbar': {'title': 'Earthquake magnitude ratio'}}
         }]
my_layout = Layout(title=title)

offline.plot({'data': data, 'layout': my_layout})
