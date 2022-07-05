# Упражнения из главы 11 - тестирование программ на основе модуля "unittest"

import unittest


# Создадим функцию для тестирования
def get_full_name(first_name, last_name, middle_name=None):
    """Функция получает имя и фамилию и возвращает полное имя."""
    if middle_name:
        full_name = first_name.title() + " " + middle_name.title() + " " + last_name.title()
    else:
        full_name = first_name.title() + " " + last_name.title()
    return full_name


# print(get_full_name('john', 'little', 'jr'))
# Создадим класс-потомок для создания тестового сценария (серии модульных тестов):
class NameFullCheck(unittest.TestCase):
    """Тесты для функции get_full_name."""

    def test_first_last_name(self):
        """Проверка правильности работы с именами и фамилиями типа 'Дмитрий Хорьков'."""
        full_name = get_full_name('дмитрий', 'хорьков')
        self.assertEqual('Дмитрий Хорьков', full_name)

    def test_first_last_middle_name(self):
        """Проверка правильности работы с именами и фамилиями типа 'Дмитрий Сергеевич Хорьков'."""
        full_name = get_full_name('дмитрий', 'хорьков', 'сергеевич')
        self.assertEqual('Дмитрий Сергеевич Хорьков', full_name)


# Конструкция "if __name__ == '__main__':" нужна для целей предотвращения запуска теста, если модуль был импортирован.
# Более подробно см.ссылки ниже: https://egorovegor.ru/if-name-main-python/
# https://pyneng.readthedocs.io/ru/latest/book/11_modules/if_name_main.html
# https://ru.stackoverflow.com/questions/515852/%D0%A7%D1%82%D0%BE-%D0%B4%D0%B5%D0%BB%D0%B0%D0%B5%D1%82-if-name-main
if __name__ == '__main__':
    unittest.main()


# Упражнения 11.1 - 11.2 выполнены в рамках файлов 'test_cities.py' и 'city_functions.py'.

# НИЖЕ ПРОВЕДЕМ ТЕСТИРОВАНИЕ КЛАССОВ:
# Создадим класс для тестирования:
class AnonymousSurvey:
    """Сбор анонимных ответов на заданный вопрос."""

    def __init__(self, question):
        """Инициализация атрибута "вопрос" и подготовка к сохранению ответов."""
        self.question = question
        self.responses = {}

    def show_question(self):
        """Вывод вопрос для пользователя."""
        print(f'Тема опроса: {self.question}')

    def save_respond(self, name, response):
        """Сохраняет полученный ответ и имя пользователя, который дал этот ответ."""
        self.responses[name] = response

    def show_results(self):
        """Выводит результаты опроса."""
        print('Результаты опроса:')
        mark = 1
        for name, response in self.responses.items():
            print(f'{mark}) Любимая страна пользователя {name} - {response}')
            mark += 1


new_survey = AnonymousSurvey('Какая ваша любимая страна?')
new_survey.show_question()
print('Введите "выход" чтобы закончить:')
while True:
    name = input('Как вас зовут?: ')
    if name == 'выход':
        if len(new_survey.responses) == 0:
            print('Никто не принял участие в опросе')
            break
        else:
            print("Спасибо за участие в опросе!")
            new_survey.show_results()
            break
    response = input('Ваша любимая страна: ')
    if response == 'выход':
        if len(new_survey.responses) == 0:
            print('Никто не принял участие в опросе')
            break
        else:
            print("Спасибо за участие в опросе!")
            new_survey.show_results()
            break
    new_survey.save_respond(name.title(), response.title())
    print('Смена опрашиваемого пользователя...\n')


# Теперь напишем тесты для класса, созданного выше.
class SurveyCheck(unittest.TestCase):
    """Тесты для класса AnonymousSurvey."""

# Метод "setUp" очень удобен при работе с тестами.
    # Данный метод создает объекты один раз, а потом можно их использовать во всех тестах. Пример ниже:
    def setUp(self):
        """Создание экземпляра опроса и набора ответов."""
        test_question = 'Какая ваша любимая страна?'
        self.my_survey = AnonymousSurvey(test_question)
        self.test_responses = {'dima': 'russia', 'michael': 'brazil', 'lisa': 'peru', 'olga': 'japan'}

    def test_save_one_response(self):
        """Проверяет, правильно ли сохраняется один ответ."""
        test_name = 'dima'
        test_response = 'russia'
        self.my_survey.save_respond(test_name, test_response)
        self.assertIn(test_name, self.my_survey.responses)               # имя сохраняется как ключ словаря
        self.assertIn(test_response, self.my_survey.responses[test_name])  # ответ сохраняется как значение словаря

    def test_save_four_responses(self):
        """Проверяет, правильно ли сохраняются 4 ответа."""
        for k, v in self.test_responses.items():
            self.my_survey.save_respond(k, v)
        for k in self.test_responses.keys():
            self.assertIn(k, self.my_survey.responses)
        for k, v in self.test_responses.items():
            self.assertIn(v, self.my_survey.responses[k])


if __name__ == '__main__':
    unittest.main()

# Упражнение 11.3 выполнено в рамках файлов 'employee_test.py' и 'employee.py'.
