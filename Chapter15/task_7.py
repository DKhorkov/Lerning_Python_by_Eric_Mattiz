# Упражнение 15.7
from task_6_and_9 import Dice, create_graph, create_frequencies, create_results


dice1 = Dice()
dice2 = Dice()
dice3 = Dice()

results = create_results(dice1, dice2, dice3)
frequencies = create_frequencies(dice1, dice2, results, dice3)
create_graph(dice1, dice2, frequencies, 'Results of rolling 3 D6 dices 1000 times', dice3)
