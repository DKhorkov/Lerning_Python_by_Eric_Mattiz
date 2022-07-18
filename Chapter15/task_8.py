# Упражнение 15.8
from plotly.graph_objs import Bar, Layout
from plotly import offline

from task_6_and_9 import Dice

dice1 = Dice()
dice2 = Dice()

results = [dice1.roll() * dice2.roll() for roll in range(1000)]
frequencies = [results.count(value) for value in range(1, dice1.sides * dice2.sides + 1)]

x_values = list(range(1, dice1.sides * dice2.sides + 1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Multiplying results of rolling two D6 dices', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout})
