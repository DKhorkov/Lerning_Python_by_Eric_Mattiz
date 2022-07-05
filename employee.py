"""Представление классов обычного работника."""


class Employee:
    """Обычный работник."""

    def __init__(self, name, surname, salary):
        """Инициализация атрибутов класса работника."""
        self.name = name
        self. surname = surname
        self.salary = salary

    def give_raise(self, amount=5000):
        """Метод повышения годовой зарплаты работника."""
        self.salary += amount
        return self.salary
