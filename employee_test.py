"""Тестовый сценарий для класса 'employee'."""
import unittest

from employee import Employee


class EmployeeTest(unittest.TestCase):
    """Тест методов класса 'employee'."""

    def setUp(self):
        """Создание экземпляра работника."""
        self.base_employee = Employee('michael', 'venedictov', 90_000)

    def test_default_raise(self):
        """Проверка стандартного повышения зарплаты."""
        self.base_employee.give_raise()
        self.assertEqual(95_000, self.base_employee.salary)

    def test_custom_raise(self):
        """Проверка выборочного повышения зарплаты."""
        self.base_employee.give_raise(10_000)
        self.assertEqual(100_000, self.base_employee.salary)


if __name__ == '__main__':
    unittest.main()
