# Упражнения 15.3 - 15.5
# https://matplotlib.org/stable/gallery/color/colormap_reference.html#sphx-glr-gallery-color-colormap-reference-py

import matplotlib.pyplot as plt
from random import choice


class RandomWalk:
    """Класс для случайного блуждания."""

    def __init__(self, num_of_points=5_000):
        """Инициализация атрибутов случайного блуждания."""
        self.num_of_points = num_of_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Заполнения графика случайным блужданием."""
        while len(self.x_values) < self.num_of_points:
            self.x_step = self.get_step()
            self.y_step = self.get_step()
            self.x_values.append(self.x_values[-1] + self.x_step)
            self.y_values.append(self.y_values[-1] + self.y_step)

    def get_step(self):
        """Рассчитывает размер шага."""
        direction = choice([-1, 1])
        distance = choice(range(1, 9))
        return distance * direction


rw = RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(16, 9))
ax.plot(rw.x_values, rw.y_values, c='blue', linewidth=1)
ax.set_title('Random-walking line')
ax.set_xlabel('OX', fontsize=12)
ax.set_ylabel('OY', fontsize=12)

# Отметим начало и конец пути:
ax.scatter(0, 0, c='yellow', s=100, zorder=2)  # "zorder" - указывает порядок наложения (точка поверх линии в тек.случ.)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100, zorder=2)

plt.show()
