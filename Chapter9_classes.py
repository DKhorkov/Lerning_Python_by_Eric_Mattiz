# Упражнения из главы 9 - классы

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


# Упражнения 9.1 - 9.9
# 9.1
class Restaurant:
    """Создает класс обычного ресторана."""

    def __init__(self, restaurant_name, cuisine_type, open_close):
        """Инициализирует имя ресторана и тип кухни в данном ресторане."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open_close = open_close
        # Создаем атрибут  "number_served" для задания 9.4
        self.number_served = 0

    def describe_restaurant(self):
        """Метод описывает экземпляр ресторана."""
        print(f'"{self.restaurant_name}" - это популярный ресторан, где работает {self.cuisine_type.lower()} кухня.')

    def open_restaurant(self):
        """Выводит информацию о том, что ресторан открыт."""
        if self.open_close is True:
            print('Ресторан открыт, добро пожаловать!')
        else:
            print('К сожалению, на данный момент ресторан не работает!')

    # Создаем метод по установлению количества обслуженных гостей для задания 9.4:
    def set_number_served(self, number):
        """Устанавливает количество обслуженных гостей."""
        self.number_served = number

    # Создаем метод по увеличению количества обслуженных гостей для задания 9.4:
    def increment_number_served(self, amount):
        """Увеличивает количество обслуженных гостей на заданное число."""
        self.number_served += amount


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
class User:
    """Стандартный пользователь."""

    def __init__(self, first_name, last_name, age, country):
        """Инициализация стандартных для пользователя атрибутов."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        # Для упражнения 9.5 добавим атрибут "login_attempts"
        self.login_attempts = 0

    # Создаем метод по увеличению количества попыток ввода логина пользователя для задания 9.5:
    def increment_login_attempts(self):
        """Увеличивает количество попыток ввести логин."""
        self.login_attempts += 1

    # Создаем метод по обнулению количества попыток ввода логина пользователя для задания 9.5:
    def reset_login_attempts(self):
        """Обнуляет количество попыток ввести логин."""
        self.login_attempts = 0

    def describe_user(self):
        """Выводит свод информации по пользователю."""
        print(f'Пользователя зовут {self.first_name.title()} {self.last_name.title()}.'
              f'\nПолное количество лет пользователя - {self.age}.'
              f'\nМесто жительства - {self.country.title()}')

    def greet_user(self):
        """Индивидуальное приветствие пользователя."""
        print(f'Доброго времени суток, {self.first_name.title()} {self.last_name.title()}!')


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
class Admin(User):
    """Класс-наследник с особыми правами на основе класса-родителя 'User'."""

    def __init__(self, first_name, last_name, age, country):
        """Инициализация атрибутов класса-родителя, а потом атрибута класса-наследника."""
        super().__init__(first_name, last_name, age, country)
        self.privileges = ['Разрешено удалять пользователей',
                           'разрешено банить пользователей',
                           'Разрешено добавлять сообщения']

    def show_privileges(self):
        """Метод по выводу информации о привилегиях."""
        print(f'У данного пользователя имеются следующие привилегии:')
        mark = 1
        for privilege in self.privileges:
            print(f'{mark}) {privilege}')
            mark += 1


admin1 = Admin('Супер', "Пользователь", 999, 'Planet Earth')
admin1.describe_user()
admin1.show_privileges()


# 9.8
class Privileges:
    """Класс привилегий пользователя."""

    def __init__(self, privileges=None):
        """Инициализация привилегий."""
        if privileges is None:
            privileges = ['Разрешено удалять пользователей',
                          'разрешено банить пользователей',
                          'Разрешено добавлять сообщения']
        self.privileges = privileges

    def show_privileges(self):
        """Метод по выводу информации о привилегиях."""
        print(f'У данного пользователя имеются следующие привилегии:')
        mark = 1
        for privilege in self.privileges:
            print(f'{mark}) {privilege}')
            mark += 1


class Admin(User):
    """Класс-наследник с особыми правами на основе класса-родителя 'User'."""

    def __init__(self, first_name, last_name, age, country):
        """Инициализация атрибутов класса-родителя, а потом атрибута класса-наследника."""
        super().__init__(first_name, last_name, age, country)
        self.privileges = Privileges()


admin2 = Admin('Мега', "Пользователь", 111, 'Planet Earth')
# Немного поигрался с изменением привилегий внутри класса "Privileges", чтобы попрактиковаться с изменением атрибутов.
admin2.describe_user()
admin2.privileges = Privileges(['Бан'])
admin2.privileges.show_privileges()


# 9.9
class Car:
    """Класс обычного автомобиля."""

    def __init__(self, manufacturer, model, year):
        """Инициализация атрибутов обычного автомобиля."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Вывод полного названия автомобиля."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Вывод информации о пробеге автомобиля."""
        print("Пробег данного автомобиля равен " + str(self.odometer_reading) + " милям.")

    def update_odometer(self, mileage):
        """Обновляет показатель пробега. Препятствует скручиванию пробега."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Нельзя уменьшить пробег!")

    def increment_odometer(self, miles):
        """Увеличение показателя пробега."""
        self.odometer_reading += miles


class Battery:
    """Модель простой батареи для электромобиля."""

    def __init__(self, battery_size=75):
        """Инициализация атрибутов батареи."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Вывод информации об энергоемкости батареи."""
        print("У данного автомобиля батарея на " + str(self.battery_size) + "-kWh.")

    def get_range(self):
        """Вывод информации о том, какое расстояние сможет проехать автомобиль на полном заряде батареи."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        message = "Данный автомобиль может проехать приблизительно " + str(range) + " миль на полной зарядке."
        print(message)

    def upgrade_battery(self):
        """Изменение объема батарее, если он не равен 100 kWh."""
        if self.battery_size != 100:
            self.battery_size = 100
            print("Изменение объема батареи до 100 kWh.")
        else:
            print("Размер батареи уже равен 100 kWh.")


class ElectricCar(Car):
    """Класс обычного электромобиля."""

    def __init__(self, manufacturer, model, year):
        """Инициализация атрибутов класса обычной машины. Затем инициализация атрибутов электромобиля."""
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


tesla = ElectricCar('Tesla', 'Model-s', 2022)
print(tesla.get_descriptive_name())
tesla.read_odometer()
tesla.battery.describe_battery()
tesla.battery.get_range()
tesla.battery.upgrade_battery()
tesla.battery.describe_battery()
tesla.battery.get_range()