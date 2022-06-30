# Упражнения из главы 8 - функции
# 8.1


def display_message():
    print('Functions')


display_message()


# 8.2


def favourite_book(title):
    print(f'One of my favourite books is {title.title()}')


favourite_book('Martin iden')


# В функциях можно использовать значения по умолчанию. Параметр со значениями по умолчанию должны быть в конце списка.
# Также есть функции с позиционными и именованными параметрами:


def pets(name, animal_type='rat'):
    print(f'I have a {animal_type}. It\'s name is {name.title()}.')


pets('faust')
# Если задаем аргумент параметру, у которого есть значение по умолчанию, то все работает так, как нам надо:
pets(animal_type='dog', name='flint')


# 8.3 - 8.8
# 8.3


def make_shirt(size, text):
    print(f'На вашей футболке {size} размера будет напечатана следующая надпись: {text}.')


make_shirt(42, 'love rats')
make_shirt(text='i love rats', size=44)


# 8.4


def make_shirt(text='I love Python', size='L'):
    print(f'На вашей футболке {size} размера будет напечатана следующая надпись: {text}.')


make_shirt()
make_shirt('Some text')
make_shirt(size='M')


# 8.5


def describe_city(city, country='Russia'):
    print(f'{city.title()} is in {country.title()}.')


describe_city('moscow')
describe_city('saint-petersburg')
describe_city('new-york', 'united states of america')


# 8.6


def city_country(city, country):
    x = city.title() + ', ' + country.title()
    return x


print(f1 := city_country('Moscow', 'russia'))
print(f2 := city_country('New-York', 'USA'))
print(f3 := city_country('peru', 'brazil'))

# 8.7


def make_album(name, title, tracks=None):
    if tracks:
        result = {name.title(): title.title(), 'Количество треков': tracks}
    else:
        result = {name.title(): title.title()}
    return result


print(f1 := make_album('AC|DC', 'hells bells', 40))
print(f1 := make_album('the bitles', 'lemon tree'))
print(f1 := make_album('dolphin', 'spring'))

# 8.8
active = True
while active:
    name = input('Введите название рок-группы:\t')
    title = input('Введите название альбома:\t')
    tracks = input('Введите количество песен в альбоме (если хотите):\t')
    result = make_album(name, title, tracks)
    print(result)
    cont = input('Хотите добавить еще группу?(да/нет):\t').lower()
    while not (cont == 'да' or cont == 'нет'):
        cont = input('Ошибка. Хотите добавить еще группу?(да/нет):\t').lower()
    if cont == "нет":
        active = False

# 8.9
messages_list = ['Привет', 'как', 'дела?']


def show_messages(messages):
    for message in messages:
        print(message)


show_messages(messages_list)

# 8.10
sent_messages = []


def send_messages(message_list):
    """Функция по перемещению элементов списка в другой список.
    Также добавлен реверс, чтобы элементы в перенесенном списке были в том же порядке, что и оригинальный"""
    while message_list:
        popped_message = message_list.pop()
        sent_messages.append(popped_message)
    sent_messages.reverse()


# show_messages(messages_list)
# send_messages(messages_list)
# print(messages_list)
# print(sent_messages)

# 8.11
print()
show_messages(messages_list)
send_messages(messages_list[:])
print(f'Изначальный список: {messages_list}')
print(f'Список перенесенных значений: {sent_messages}')


# Создадим функцию с произвольным количеством последовательных аргументов
def pets_in_room(room_size, *pet):
    """Функция берет обязательный аргумент размера комнаты, а потом берет неограниченное количество аргументов,
    которые кладет в создаваемый кортеж 'pet'. Далее я объединил весь кортеж в строку,
    чтобы красиво вывести для пользователя всю инфу в одной форматирующей строке."""
    pet_str = ', '.join(pet)
    print(f'I have a {room_size} room, where lives {pet_str}.')


pets_in_room('big', 'хомяк', 'dog', 'rat', 'cat')


# Теперь создадим функцию с произвольным количеством именованных аргументов
def pet_status(pet_name, pet_location, **pet_info):
    """В случае именованных аргументов, количество которых нам неизвестно,
    лучше создавать словарь с ключем-значением."""
    pet_info['pet name'] = pet_name
    pet_info['location'] = pet_location
    print('Нам известна следующая информация о животном:')
    for k, v in pet_info.items():
        print(f'{k.title()}: {v.title()}')
    return pet_info


# Ввод необязательных аргументов следующий: ключ без кавычек, потом "равно", потом значение в кавычках.
# По аналогии с функцией "dict".
x = pet_status('faust', 'cage', status='lovely', favourite_food='eggs', lives_with='flint')
# Как сделать в обратном порядке через "reverse" - https://docs-python.ru/tutorial/operatsii-slovarjami-dict-python/obratnyj-porjadok-revers-slovarja/
y = {k: v for k, v in reversed(list(x.items()))}
print('Нам известна следующая информация о животном:')
for k, v in y.items():
    print(f'{k.title()}: {v.title()}')


# 8.12
def sandwich(*component):
    print('Вы добавили в ваш сендвич следующие компоненты:')
    for i in component:
        print(f'- {i}')


sandwich('тунец', 'курицы', 'сыр')
sandwich('тунец', 'курицы')
sandwich('тунец')

# 8.13 - Сделано выше в рамках строк кода 161 - 180 на примере фауста.
# Также добавлен "reversed" порядок, чтобы было логичнее


# 8.14
def cars(company, model, **car_info):
    """Функция возвращает название компании, модель и остальное, если введено."""
    car_info['company'] = company
    car_info['model'] = model
    print('Нам известна следующая информация о машине:')
    for k, v in car_info.items():
        print(f'{k.title()}: {v.title()}')
    # return car_info


cars('audi', 'a4', color='black', used_before='4 years')


