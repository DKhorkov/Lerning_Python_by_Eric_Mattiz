# Упражнения из главы 9 - классы
import car
from restaurant import Restaurant
from user import User, Admin, Privileges
from random import randint, choices


class Cat:
    """Создает класс обычной кошки со стандартными атрибутами."""

    def __init__(self, name, age, breed):
        """Супер-метод инициализации основных атрибутов будущих экземпляров: имя, возраст и порода кошки."""
        self.name = name
        self.age = age
        self.breed = breed

    def meow(self):
        """Кошка мяукает."""
        print(f'Кошка по кличке {self.name},чья порода - {self.breed}, - и которой {self.age} лет мяукнула.')


cat1 = Cat('Sasha', 18, 'Basic')
# После создания экземпляра можно вызывать методы объекта(экземпляра), которые были прописаны внутри класс. Пример ниже:
cat1.meow()
# Ниже приведен пример обращения к атрибутам экземпляра (атрибуты переданы при создании экземпляра):
print(f'My cat\'s name was {cat1.name} and it was {cat1.age} years old.')

# Упражнения 9.1 - 9.15
# 9.1
# Класс ресторана был импортирован в начале файла из отдельного модуля с целью сокращения объема кода.
restaurant = Restaurant('У Миши', "Японская", False)
print(f'Существует ресторан "{restaurant.restaurant_name}".')
print(f'В этом ресторане функционирует {restaurant.cuisine_type.lower()} кухня.'
      f'\nА если все это объединить, то получится:')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9.2
restaurant2 = Restaurant('Конкуренты Миши', 'Куда более вкусная, чем у Миши', True)
restaurant2.describe_restaurant()
restaurant3 = Restaurant('Конкуренты конкурентов Миши', 'еще более вкусная, чем у конкурентов Миши', True)
restaurant3.describe_restaurant()

# 9.3
# Класс юзера был импортирован из отельного файла для оптимизации кода.
user1 = User('Михаил', 'Венедиктов', 24, 'Россия')
user2 = User('Дмитрий', 'Хорьков', 24, 'Россия')
user1.greet_user()
user1.describe_user()
user2.greet_user()
user2.describe_user()

# 9.4
print(restaurant.number_served)
restaurant.set_number_served(100)
print(restaurant.number_served)
restaurant.increment_number_served(20)
print(restaurant.number_served)

# 9.5
print(user1.login_attempts)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)


# 9.6
class IceCreamStand(Restaurant):
    """Создает класс-потомок на основе класса ресторан."""

    def __init__(self, restaurant_name, cuisine_type, open_close):
        """Инициализация атрибутов класса-родителя, а также инициализация атрибутов класса потомка."""
        super().__init__(restaurant_name, cuisine_type, open_close)
        self.flavours = ["Шоколадное", "Крем-брюле", "Пломбир"]

    def describe_flavours(self):
        """Описывает существующие виды мороженного в ресторане."""
        print(f"В данном ресторане существуют следующие виды мороженного: {self.flavours}")
        mark = 1
        for flavour in self.flavours:
            print(f'{mark}) {flavour}')
            mark += 1


ice_cream_restaurant = IceCreamStand('Мир мороженного', 'ice cream', True)
# После создания экземпляра на основе класса-потомка, можно обращаться также и к методам класса-родителя. Пример ниже:
ice_cream_restaurant.describe_restaurant()
ice_cream_restaurant.open_restaurant()
ice_cream_restaurant.describe_flavours()

# 9.7
# Класс супер-пользователя (админа) также был импортирован из модуля "user.py"
admin1 = Admin('Супер', "Пользователь", 999, 'Planet Earth')
admin1.describe_user()
admin1.privileges.show_privileges()

# 9.8
# Класс привилегий был импортирован из модуля "user.py" с целью оптимизации кода.
admin2 = Admin('Мега', "Пользователь", 111, 'Planet Earth')
# Немного поигрался с изменением привилегий внутри класса "Privileges", чтобы попрактиковаться с изменением атрибутов.
admin2.describe_user()
admin2.privileges = Privileges(['Бан'])
admin2.privileges.show_privileges()

# 9.9
# Используем импортированный модуль, куда перенесли сам класс автомобиля, батарее и электромобиля.
tesla = car.ElectricCar('Tesla', 'Model-s', 2022)
print(tesla.get_descriptive_name())
tesla.read_odometer()
tesla.battery.describe_battery()
tesla.battery.get_range()
tesla.battery.upgrade_battery()
tesla.battery.describe_battery()
tesla.battery.get_range()


# 9.10 Выполнено в рамках упражнения 9.1

# 9.11 Выполнено в рамках упражнения 9.3

# 9.12 Является разбиением модуля "user.py" на два отдельных модуля.


# 9.13
class Dice:
    """Класс простого кубика с заданным количеством граней."""

    def __init__(self, sides=6):
        """Инициализация атрибутов кубика."""
        self.sides = sides

    def roll_dice(self):
        """Метод по симуляции броска кубика."""
        print(f'Кубик имеет {self.sides} граней. \nВыпавшее число на кубике: {randint(1, self.sides)}')


six_sides_dice = Dice()
for num in range(10):
    six_sides_dice.roll_dice()

ten_sides_dice = Dice(10)
for num in range(10):
    ten_sides_dice.roll_dice()

twenty_sides_dice = Dice(20)
for num in range(10):
    twenty_sides_dice.roll_dice()

# 9.14
# Используемая в данной программе комбинация: f1g2n3m4k567890
lottery = str(input('Введите последовательность, содержащую 10 чисел и 5 букв: '))
count_numbers = 0
for sym in lottery:
    try:
        int(sym)
        count_numbers += 1
    except ValueError:
        count_numbers += 0
while not (len(lottery) == 15 and count_numbers == 10):
    lottery = str(input('Ошибка! Нужно ввести последовательность, содержащую 10 чисел и 5 букв: '))

win_ticket = choices(lottery, k=4)
win_ticket = ''.join(win_ticket)
print(f'Победный билет должен содержать следующую комбинацию: {win_ticket}')

# 9.15
my_ticket = []
x = choices(lottery, k=4)
my_ticket.append(x)
print("Идет процесс подсчета...")
while not x == win_ticket:
    x = choices(lottery, k=4)
    x = ''.join(x)
    if x not in my_ticket:
        my_ticket.append(x)

print(f'Для получения выигрышной комбинации понадобилось {len(my_ticket)} попыток.')
