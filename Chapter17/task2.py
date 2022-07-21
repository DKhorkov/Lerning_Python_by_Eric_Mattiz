# Упражнение 17.2 - Визуализация самых обсуждаемых статей.
import requests
from plotly import offline
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    # Вызов API для каждой статьи:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Создание словаря для каждой статьи:
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

titles, comments = [], []
for sd in submission_dicts:
    titles.append(sd['title'])
    comments.append(sd['comments'])

data = {'type': 'bar',
        'x': titles,
        'y': comments,
        }
my_layout = {'title': 'Most-discussed articles on Hacker News',
             'titlefont': {'size': 30,
                           'color': 'blue'},
             'xaxis': {'title': 'Article title',
                       'titlefont': {'size':20,
                                     'color': 'red'},
                       },
             'yaxis': {'title': 'Comments number',
                       'titlefont': {'size':20,
                                     'color': 'red'},
                       }
             }
offline.plot({'data': data, 'layout': my_layout})
