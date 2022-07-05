import unittest

from city_functions import city_info


class CityInfoCheck(unittest.TestCase):
    """Тесты для функции city_info."""

    def test_city_country(self):
        """Проверяет, правильно ли работает функция с данными типа 'Moscow, Russia'."""
        city = city_info('moscow', 'russia')
        self.assertEqual(city, 'Moscow, Russia')

    def test_city_country_population(self):
        """Проверяет, правильно ли работает функция с данными типа 'Moscow, Russia, 3_000_000'."""
        city = city_info('moscow', 'russia', 3_000_000)
        self.assertEqual(city, 'Moscow, Russia - population 3 000 000.')


if __name__ == '__main__':
    unittest.main()
