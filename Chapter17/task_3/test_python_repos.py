# Упражнение 17.3 - тесты модуля "python_repos_.py":
import unittest

import python_repos as pr


class ReposTest(unittest.TestCase):
    """Класс для тестирования модуля python_repos."""

    def setUp(self):
        """Вызов функций для дальнейшего тестирования."""
        self.response = pr.get_response()
        self.repo_dicts = pr.get_repo_dicts(self.response)

    def test_status_code(self):
        """Проверка, что статус кода после ответа API будет 200."""
        self.assertEqual(self.response.status_code, 200)

    def test_get_repo_dicts(self):
        """Проверяет, что количетсво словай полностью передано."""
        self.assertEqual(len(self.repo_dicts), len(self.response.json()['items']))


if __name__ == '__main__':
    unittest.main()
