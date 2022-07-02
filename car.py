"""Класс для представления обычного автомобиля, перенесенный в отдельный модуль дял удобства использования в будущем.
Также добавлены класс батареи для электромобиля и класс обычного электромобиля, так как связаны с классом обычного
автомобиля."""


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
