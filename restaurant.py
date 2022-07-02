"""Класс для представления обычного ресторана."""


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
