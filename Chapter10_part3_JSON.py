# Упражнения из главы 10, часть 3 - сохранение данных пользователя с помощью модуля JSON
import json

# Создадим информацию, которую сохраним в файле с помощью JSON:
info = 'Some information to save and load by JSON'
save = 'saving_data.json'
with open(save, 'w') as f:
    json.dump(info, f)

# Теперь вернем эту информацию из файла в рабочую программу:
file_name = 'saving_data.json'
with open(file_name) as f:
    loaded_info = json.load(f)
print(loaded_info)

# Объединим два метода в одну программу, чтобы сохранять уже данные, введенные пользователем.
# Программа нацелена на предотвращения доступа несовершеннолетних к фильмам с рейтингом "R".
file_name = "user_age.json"
try:
    with open(file_name) as f:
        user_age = json.load(f)
except FileNotFoundError:
    user_age = input('Please enter u\'r age: ')
    while True:
        try:
            user_age = int(user_age)
        except ValueError:
            user_age = input('Error! U should enter a number: ')
        else:
            with open(file_name, 'w') as f:
                json.dump(user_age, f)
            if user_age >= 18:
                print('Enjoy watching the film!\nWe will remember u\'r age for further times!')

            else:
                print('This video is intended for persons over 18 years old!'
                      '\nWe will remember u\'r age for further times!')
            break
else:
    if user_age >= 18:
        print('Enjoy watching the film!')
    else:
        print('This video is intended for persons over 18 years old!')


# Произведем рефакторинг программы, написанной выше, а также добавим в нее улучшения, приблизив к реальности:
def rights_check(name, user_name, age):
    """Проверяет, можно ли человеку смотреть фильмы с рейтингом R."""
    if name == user_name and age >= 18:
        print(f'Enjoy watching the film, {name.title()}!')
    else:
        print(f'Sorry, {name.title()}, but this film is intended for persons over 18 years old!')


def get_restored_info():
    """Получает хранимую в файле информацию о пользователях."""
    file_name = "user_info.json"
    try:
        with open(file_name) as f:
            info = json.load(f)
    except FileNotFoundError:
        print('Error. File with users info was removed from current folder.')
        q = input('Press "Enter" key to quit: ')
        exit()
    else:
        return info


def age_input():
    """Получение возраста от пользователя."""
    age = input('Please, enter u\'r age: ')
    while True:
        try:
            age = int(age)
        except ValueError:
            age = input('Error! U should enter a number: ')
        else:
            break
    return age


def adding_info(name, age):
    """Добавление информации о новом пользователе в файл, с информацией о пользователях."""
    file_name = "user_info.json"
    new_user = dict(name=name, age=age)
    try:
        with open(file_name) as f:
            info = json.load(f)
    except FileNotFoundError:
        print('Error. File with users info was removed from current folder.')
        q = input('Press "Enter" key to quit: ')
        exit()
    else:
        info.append(new_user)
        with open(file_name, "w") as f:
            json.dump(info, f)


def list_of_users_check(user_name):
    """Выводит список имен всех пользователей и, если имя пользователя не в списке, обновляет файл с информацией
    о всех пользователях."""
    info = get_restored_info()
    list_of_users = []
    for element in info:
        list_of_users.append(element['name'])
    if user_name not in list_of_users:
        age = age_input()
        adding_info(user_name, age)


def watch_the_film():
    """Функция анализирует, может ли пользователь быть допущен к просмотру фильма с рейтингом R."""
    user_name = input('Enter ur name: ').lower()
    list_of_users_check(user_name)
    info = get_restored_info()
    for element in info:
        if user_name in element['name']:
            rights_check(element['name'], user_name, element['age'])
        else:
            continue


watch_the_film()


# Упражнения 10.11 - 10.13
# 10.11 и 10.12
def num_input():
    """Checks if input value is numeric"""
    num = input('Enter u\'r favourite number: ')
    while not num.isdigit() == True:
        num = input('Error. U should enter anumber: ')
    return num


file = "user_favourite_number.json"
try:
    with open(file) as f:
        fav_num = json.load(f)
except FileNotFoundError:
    fav_num = num_input()
    with open(file, "w") as f:
        json.dump(fav_num, f)
else:
    print(f'I know u\'r favourite number! It\'s {fav_num}.')

# 10.13 было выполнено и модернизировано в рамках программы по по анализу доступности фильма для пользователя.
# Более подробно см. строки кода 46-123.
