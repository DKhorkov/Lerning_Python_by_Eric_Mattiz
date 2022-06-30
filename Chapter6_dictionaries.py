# Упражнения из главы 6 - Словари


# Создать словарь можно несколькими способами
# https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html
dictionary = {'Map': 'Germany', 'Num': 3}
print(dictionary['num'.title()])
dictionary2 = dict(Color='blue', name='Drue')
print(dictionary2)
# Можно также создавать пустые словари, как и списки/кортежи
dictionary3 = {}
print(dictionary3)

# Чтобы использовать словарь в f-строке, нужно использовать один тип кавычек для f-строки и другой для ключа словаря.
print(f'The country u live in is {dictionary["Num"]}')
# Либо создать новую переменную, присвоить ей нужное значение словаря, а потом вставить в "f-строку". См. ниже
ur_country = dictionary['Map']
print(f'The country u live in is {ur_country}')


# Добавления значений в словарь делается путем названия "название словаря"["Ключ"] = "значение"
dictionary['Population'] = 150
print(dictionary)

# Изменение значений в словаре аналогично присваиванию нового значения переменной
dictionary3['Name'] = 'Peter'
print(dictionary3)
dictionary3['Name'] = 'Stan'
print(dictionary3)

# обновление словаря через метод "update"
# https://programbox.ru/2021/12/20/python-метод-обновления-словаря-update/#:~:text=Метод%20обновления%20словаря%20Python%20update(),(обычно%20кортежи)%20в%20качестве%20параметров

# Удаление пар "ключ-значение"
del dictionary3['Name']
print(dictionary3)

# Метод "get" для предотвращения ошибки "KeyError", когда в словаре нет нужного нам ключа.
dictionary3['Color'] = "blue"
dictionary3['Points'] = 5
print(dictionary3)
# print(dictionary3['Points'])
# Traceback (most recent call last):
#   File "C:\Users\alexq\Desktop\Python\PyCharm Projects\LearningPythonBook\Chapter6_tasks.py", line 38, in <module>
#     print(dictionary3['Points'])
# KeyError: 'Points'
# Если нет такого ключа, то получает ошибку
# Ситуация решается методом "get":
# создаем новую переменную, присваиваем ей "название словаря".get("ключ", "Значение, когда ключа нет").
# Если ключ есть, то получим его значение, если ключа нет, получим вторую часть метода "get"
point = dictionary3.get('Points', 'No points')
print(point)
# Но если ключ будет присвоен после метода "get", мы все равно не будем его получать...


# Упражнения 6.1 - 6.3
# 6.1
favourite_person = {'first_name': 'Robert', 'last_name': 'Deniro', 'age': 80, 'city': 'New-York'}
for person in favourite_person:
    print(favourite_person[person])


# 6.2
friends_favourite_numbers = dict(Lisa=16, Misha=10, Tema=10, Idris=20)
friends_favourite_numbers['Fedia'] = 25
print(friends_favourite_numbers)
for name in friends_favourite_numbers:
    print(f'{name}"s favourite number is {friends_favourite_numbers[name]}.')

# 6.3
glossary = {
    'Переменная': 'объект, которому присваивается значение',
    'Список': 'объект, внутри которого находится н-ное количество значений, а также который можно менять',
    'Диапазон': 'объект, включающий в себя н-ное количество числовых значений в заданном промежутке',
    'Кортеж': 'объект, внутри которого находится н-ное количество значений, но который нельзя менять',
    'Цикл': 'это операция, производящая одни и те же действия определенное или бесконечное количество раз',
    }
for title in glossary:
    print(f'{title} - это {glossary[title]}.')


# Перебор словаря
# Перебор всех ПАР c помощью метода "items"
for key, value in dictionary3.items():
    print(f'Key is: {key}.\nValue for this key is: {value}.\n')

# Перебор всех КЛЮЧЕЙ в словаре методом "keys", либо просто перебором словаря "for 'название' in "словарь":"
for name in glossary.keys():
    print(name)
print()
for name in glossary:
    print(name)
print()
# Также можно обратиться к значению определенного ключа в момент цикла перебора значений словаря
for name in glossary:
    if name.lower() == 'переменная':
        print(f'{name} - это {glossary[name]}.')
    else:
        print(name)
print()
# Также можно перебирать словарь по ключам в другом порядке с помощью  "sorted"
print(glossary.keys())
print(sorted(glossary.keys()))
print()

# Перебор ЗНАЧЕНИЙ в словаре с помощью метода "values"
print(friends_favourite_numbers)
for values in friends_favourite_numbers.values():
    print(values)
print()
# Однако значения могу быть ДУБЛИКАТАМИ. Для вывода списка уникальных значений используется функция "set".
print(friends_favourite_numbers)
for values in set(friends_favourite_numbers.values()):
    print(values)
print()

# Также в Python существуют МНОЖЕСТВА. Они похожи на словари синтаксисом {}, но в них просто значения, а не "Ключ-знач."
# https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html - про множества
plenty = {'x', 'y', 'z'}
plenty.add('g')
print(plenty)
print(type(plenty))


# Упражнения 6.4 - 6.6
# 6.4 выполнено автоматически в рамках 6.3, но повторим с добавлением новых определений
glossary['Условие if'] = 'команда Python, определяющая, соблюдено ли условие'
glossary['Тип данных'] = 'определение, относятся ли данные к числовым, строчным, вещественным, спискам, кортежам и т.д.'
glossary['Функция'] = 'команда Python, выполняющая определенные действия, прописанные внутри данной функции'
glossary['Метод'] = 'функция Python, привязанная к  объекту'
glossary['Срез'] = 'метод Python, позволяющий вывесть или перебрать нужные нам элементы списка по их индексу'
for title in glossary:
    print(f'{title} - это {glossary[title]}.')
print()

# 6.5
rivers = dict(nile='egypt', amazon='brazil', enisey='russia')
for river, country in rivers.items():
    print(f'{river.title()} runs through {country.title()}.')
for river in rivers.keys():
    print(river.title())
for river in rivers.values():
    print(river.title())

# 6.6
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
survey = ['jen', 'edward', 'joe', 'moe', 'phil']
for name in survey:
    if name in favourite_languages:
        print(f'Thank\'s for u\'r survey, {name.title()}.')
    else:
        print('{}, please take the survey.'.format(name.title()))
print()


# Вложения (словарь в словаре, словари в списке, списке в словаре и так далее)
alian_01 = {'color': 'black', 'speed': 'fast', 'points': 30}
alian_02 = {'color': 'blue', 'speed': 'medium', 'points': 20}
alian_03 = {'color': 'grey', 'speed': 'low', 'points': 10}
alians_0 = [alian_01, alian_02, alian_03]
print(alians_0)
print()

# циклы "for" для создания множества словарей внутри списка, а также для изменения элементов списка
alians_1 = []
for alian in range(5):
    new_alian = {'color': 'green', 'points': 5}
    alians_1.append(new_alian)
print(alians_1)
for alian in alians_1[:1]:
    if alian['color'] == 'green':
        alian['color'] = 'yellow'
        alian['points'] = 10
print(alians_1)

# НИЖЕ ПРЕДСТАВЛЕН КОД, КОТОРЫЙ СОЗДАЕТ БАГ. Причина в том, что мы берем созданный словарь "alian_01".
# Из-за этого почему-то все наши пришельцы становятся желтыми, а не только первый. Видимо, не работает срез?
# alians_1 = []
# for alian in range(5):
#     alians_1.append(alian_01)
# print(alians_1)
# for alian in alians_1[:1]:
#     if alian['color'] == 'black':
#         alian['color'] = 'yellow'
#         alian['points'] = 10
# print(alians_1)

# Список в словаре
# Если мы в форматирующей строке хотим использовать элемент списка (который является значением ключа в словаре),
# то нужно использовать синтаксис, как представлено ниже. Индекс идет в новых скобках после указания ключа.
ps5_games = {'game': 'God of War', 'characters': ['Cratos', 'Atrey']}
print(f'I played {ps5_games["game"]}, where main characters were {(ps5_games["characters"][0])} '
      f'and {(ps5_games["characters"][1])}.')
# Тренировка со списками в словаре на примере favourite_languages (см. страницы 124 - 125)
favourite_languages = {
    'jen': ['python'],
    'sarah': ['c', 'c#'],
    'edward': ['ruby', 'go'],
    'phil': ['paskal'],
    }
# Добавил свои усовершенствования (нумерация, вывод в одну строку, если один язык программирования в списке значения)
for name, languages in favourite_languages.items():
    if len(languages) == 1:
        for language in languages:
            lang = language
        print(f'\n{name.title()}\'s favourite programming language is {lang.title()}.')
    else:
        print(f'\n{name.title()}\'s favourite programming languages are:')
        mark = 1
        for language in languages:
            print(f'{mark}) {language.title()}')
            mark += 1

# Словари в словаре на примере пользователей сайта
users_on_forum = {
    'nubmaster69': {'game': 'fortnite', 'name': 'Joe'},
    'd3m0s': {'game': 'dota2', 'name': 'Dima'}
    }
for user, info in users_on_forum.items():
    print(f'\nUser login is {user.title()}.')
    print(f'Users\'s favourite game is {info["game"].title()} and his real name is {info["name"]}.')


# Упражнения 6.7 - 6.12
# 6.7
favourite_person = {'first_name': 'Robert', 'last_name': 'Deniro', 'age': 80, 'city': 'New-York'}
friend = {'first_name': 'Michael', 'last_name': 'Venedictov', 'age': 24, 'city': 'Saint-Petersburg'}
girlfriend = {'first_name': 'Lisa', 'last_name': 'Guliaeva', 'age': 23, 'city': 'Saint-Petersburg'}
people = [girlfriend, friend, favourite_person]
for unit in people:
    for k, v in unit.items():
        print(f'{k}: {v}')
    print()

# 6.8
faust = {'name': 'faust', 'type': 'rat', 'owner': 'dima'}
flint = {'name': 'flint', 'type': 'rat', 'owner': 'lisa'}
lialia = {'name': 'lialia', 'type': 'dog', 'owner': 'olga'}
pets = [faust, flint, lialia]
for pet in pets:
    print()
    for key, value in pet.items():
        print(f'{key.title()}: {value.title()}')
    print()

# 6.9
lisa = {'first place': 'china', 'second place': 'peru'}
michael = {'first place': 'brazil', 'second place': 'USA'}
olga = {'first place': 'russia', 'second place': 'gruzia'}
favourite_places = {'lisa': lisa, 'michael': michael, 'olga': olga}
for name, info in favourite_places.items():
    print(f'\n{name.title()}\'s favourite places are:')
    marker = 1
    for v in info.values():
        print(f'\t{marker}) {v.title()}')
        marker += 1

# 6.10
lisa = {'name': 'lisa', 'numbers': [15, 16]}
michael = {'name': 'michael', 'numbers': [20, 30]}
fedya = {'name': 'fedya', 'numbers': [15, 1, 8, 10]}
friends_favourite_numbers = [lisa, michael, fedya]
for name in friends_favourite_numbers:
    for k, v in name.items():
        if k == 'name':
            print(f'\n{v.title()}\'s favourite numbers are:')
            marker1 = 1
        else:
            for num in v:
                print(f'{marker1}) {num}')
                marker1 += 1

# 6.11
new_york = {'country': 'USA', 'population': '15_000_000', 'fact': 'capital of money funds'}
moscow = {'country': 'russia', 'population': '12_000_000', 'fact': 'capital of fucking capers'}
stambul = {'country': 'turkey', 'population': '8_000_000', 'fact': 'tasty sweet food'}
cities = {'New-York': new_york, 'Moscow': moscow, 'Stambul': stambul}
for k, v in cities.items():
    print(f'\n{k.title()}:')
    for keys, value in v.items():
        print(f'{keys.title()}: {value.title()}')

# 6.12 - Изменения вносил во все упражнения выше, так что выполнено
