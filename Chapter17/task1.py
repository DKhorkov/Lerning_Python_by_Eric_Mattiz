# Упражнение 17.1 - Визуализация самый популярных проектов на языке "go".

import requests
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:go&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

response_dict = r.json()
print(response_dict.keys())

# Обработка словарей с данными о проектах:
repo_dicts = response_dict['items']
links, stars, descriptions = [], [], []
for d in repo_dicts:
    # for key in sorted(d.keys()):
    #     print(key)
    links.append(f'<a href="{d["html_url"]}">{d["name"]}</a>')
    stars.append(d['stargazers_count'])
    descriptions.append(f'{d["owner"]["login"]}<br />{d["description"]}')

# Визуализация обработанных данных:
data = {'type': 'bar',
        'x': links,
        'y': stars,
        'hovertext': descriptions
        }
my_layout = {'title': 'Top-Starred projects on GOlang GitHub',
             'titlefont': {'size': 30,
                           'color': 'black'},
             'xaxis': {'title': 'Repo names',
                       'titlefont':{'size': 16,
                                    'color': 'red'}
                       },
             'yaxis': {'title': 'Stars',
                       'titlefont':{'size': 16,
                                    'color': 'red'}
                       }
             }
offline.plot({'data': data, 'layout': my_layout})
