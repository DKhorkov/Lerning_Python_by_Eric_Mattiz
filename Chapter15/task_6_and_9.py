# Упражнения 15.6 и 15.9
from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline


class Dice:
    """Класс игрального кубика."""

    def __init__(self, num_sides=6):
        """Атрибуты кубика. ПО умолчанию у кубика 6 граней."""
        self.sides = num_sides

    def roll(self):
        """Симуляция броска кубика."""
        return randint(1, self.sides)


def create_results(d1, d2, d3=None):
    if d3:
        results = [d1.roll() + d2.roll() + d3.roll() for roll in range(1_000)]
    else:
        results = [d1.roll() + d2.roll() for roll in range(1_000)]  # Упражнение 15.9 - Генератор списка.
    # for roll in range(1_000):
    #     result = d1.roll() + d2.roll()
    #     results.append(result)
    return results


def create_frequencies(d1, d2, results, d3=None):
    if d3:
        frequencies = [results.count(value) for value in range(3, d1.sides + d2.sides + d3.sides + 1)]
    else:
        frequencies = [results.count(value) for value in range(2, d1.sides + d2.sides + 1)]   # Упражнение 15.9.
    # for value in range(2, d1.sides + d2.sides + 1):
    #     frequency = results.count(value)
    #     frequencies.append(frequency)
    return frequencies


def create_graph(d1, d2, frequencies, title, d3=None):
    if d3:
        x_values = list(range(3, d1.sides + d2.sides + d3.sides + 1))
    else:
        x_values = list(range(2, d1.sides + d2.sides + 1))
    data = [Bar(x=x_values, y=frequencies)]
    x_axis_config = {'title': 'Result'}
    y_axis_config = {'title': 'Frequency of Result'}
    my_layout = Layout(title=title, xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout})


dice1 = Dice(8)
dice2 = Dice(8)
results = create_results(dice1, dice2)
frequencies = create_frequencies(dice1, dice2, results)
create_graph(dice1, dice2, frequencies, 'Results of roll double D8 dices 1000 times')
