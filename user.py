"""Представление классов обычного пользователя, супер-пользователя (админа) и привилегий админа."""


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


class Admin(User):
    """Класс-наследник с особыми правами на основе класса-родителя 'User'."""

    def __init__(self, first_name, last_name, age, country):
        """Инициализация атрибутов класса-родителя, а потом атрибута класса-наследника."""
        super().__init__(first_name, last_name, age, country)
        self.privileges = Privileges()


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