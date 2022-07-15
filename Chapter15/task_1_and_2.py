# Упражнения 15.1 и 15.2

import matplotlib.pyplot as plt


numbers = range(1, 5001)  # Пять тысяч кубов
numbers_cubes = [num ** 3 for num in numbers]

print(plt.style.available)
plt.style.use('classic')

fig, ax = plt.subplots()
ax.scatter(numbers, numbers_cubes, cmap=plt.cm.plasma, s=60)
ax.plot(numbers, numbers_cubes, linewidth=1)
ax.set_title('Cubes of numbers', fontsize=20)
ax.set_xlabel('Numbers', fontsize=12)
ax.set_ylabel('Cubes, mln.', fontsize=12)
ax.tick_params(axis='both', labelsize=8)


plt.show()
