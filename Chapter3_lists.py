# Упражнения из главы 3



# 3.1
names = ['dima', 'lisa', 'sereza', 'ken']
print(names[0].title(), names[3].upper())
# то что представлено ниже - это срез (slice), чтобы вывести нужные элементы списка
# https://pythonworld.ru/osnovy/indeksy-i-srezy.html - инфа про срезы и индексы
print(names[2::])
print(f'My love is {names[1].title()}!')

# Упражнения 3.2 - 3.3
a = f'My name is {names[0].title()}'
b = f'My name is {names[1].title()}'
c = f'My name is {names[2].title()}'
d = f'My name is {names[3].title()}'
print(a, b, c, d, sep='\n')

# изменение элементов списка аналогично переменным
names[2] = 'kody'
print(names)
# добавление новых элементов в список
names.insert(2, 'Dan')
print(names)
names.append('Block')
print(names)
# удаление элементов списка:функция 'del' удаляет по индексу, а метод 'remove' по содержанию (но только первое значение)
# если в списке будет несколько одинаковых значение, то 'remove' удалит только первое найденное
del names[5]
print(names)
names.insert(0, 'ken')
names.insert(0, 'ken')
names.insert(0, 'ken')
names.insert(0, 'ken')
print(names)
names.remove('ken')
print(names)
# но можно обыграть путем цикла
while 'ken' in names:
    names.remove('ken')
print(f'Очищенные от КЕНа список выглядит теперь так: {names}')

# также существует метод 'pop()', который антоним 'append',
# 'pop()' убирает последний элемент списка, если не ввести индекс, но при вводе индекса убирает нужным нам элемент.
# 'pop(2)' уберет 3 элемент списка. Отличается от 'del' своим предназначением (сохранением в программе элемента)
# чтобы сохранить данный элемент в программе, нужно присвоить его новой переменной
popped_name = names.pop(3)
print(names, popped_name.title(), sep='\n')

# красиво вывести весь список для пользователя можно с помощью метода 'join', либо через цикл "for"
print(names)
list_of_names = '\n'.join(names).title()
print(f'Full list of names is: \n{list_of_names}')

# 3.4 - 3.7
# приглашение гостей. Список называть ВСЕГО В МНОЖЕСТВЕННОМ ЧИСЛЕ!
invites = ['arnold shwarznegger', 'ilon mask', 'adam']
message1 = f'Dear {invites[0].title()}, hope u will visit me tomorrow!'
message2 = f'Dear {invites[1].title()}, hope u will visit me tomorrow!'
message3 = f'Dear {invites[2].title()}, hope u will visit me tomorrow!'
print(message1, message2, message3, sep='\n')
# гость не сможет прийти
print(invites[2].title(), "не сможет прийти")
# изменение гостя 3
invites[2] = 'abraham linkoln'
message3 = f'Dear {invites[2].title()}, hope u will visit me tomorrow!'
# новые приглашения для гостей
print(message1, message2, message3, sep='\n')

# Больше гостей
print('Прибудет больше гостей')
invites.insert(0, 'george kluni')
invites.insert(len(invites) // 2, 'tom hanks ')
invites.append('mike tyson')
print(invites)


# тут я решил сымпровизировать и вместо муторного печатанья кода бахнул функцию
# также сделал небольшой задел для работы со списками - нахождение размера списка


def inv():
    name = invites[-1]
    ind = invites.index(name)
    x = 0
    while x < ind + 1:
        message = f'Dear {invites[x].title()}, hope u will visit me tomorrow!'
        print(message)
        x += 1
    return ""


# в цикле 'for' временную переменную (в случае ниже "invite_name") лучше называть так, чтобы описать содержание списка
for invite_name in invites:
    print(f'Dear {invite_name.title()}, hope u will visit me tomorrow!', 2)

# можно через цикл 'for', что куда проще, чем создание собственной функции
print(inv())

# сокращение гостей
print('Стол не привезут. ПРиглашаем только двух гостей')


def no_come():
    while len(invites) != 2:
        removed_name = invites.pop()
        print(f'Проcти, {removed_name.title()}, но ты не приглашен более')
    return ""


print(no_come())
message1 = f'Дорогой {invites[0].title()}, приглашение в силе!'
message2 = f'Дорогой {invites[1].title()}, приглашение в силе!'
print(message1, message2, sep='\n')
# 3.9
print(f'Длина списка с приглашенными гостями составляет: {len(invites)}')
# del invites[0], invites[1]
# print(invites) - пустой лист, программа ломается. Значит, выше все сделано правильно.

# сортировка методом 'sort()' и 'sorted()', а также вывод сортировки в обратно направлении 'sort(reverse=True)'
# 'sorted' сортирует список лишь для вывода. А 'sort' навсегда, что к исходному порядку уже не вернуться
new_list = [2, 4, 5, 1, 7, 9, 0]
print(new_list)
print(sorted(new_list,reverse=True))
print(new_list)

# тут я решил проверить, как будет работать сортировка с регистрами и цифрами, а также другим алфавитом
# если цифры не в скобках (имеют str тип), то сортировка не сработает, все сломается
# так, как видно из результата, сначала идут цифры, потом верхний регистр, потом нижний. Кириллица в самом конце
list2 = ['a', 'D', 'b', 'c', 'м', '2']
print(sorted(list2))
# ниже пример работы метода 'sort'
list3 = ['e', 'K', 'a', 'C', 'b', 'g']
print(list3)
list3.sort(reverse=True)
print(list3)

# 3.8 - 3.11
countries = ['США', 'Бразилия', 'Тайланд', 'Япония', 'Норвегия']
print(countries)
print(sorted(countries))
print(countries)
print(sorted(countries, reverse=True))
print(countries)
countries.reverse()
print(countries)
countries.reverse()
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)
# 3.9 ищи выше в коде
# 3.10 далее
lang1 = 'russian'
lang2 = 'english'
lang3 = 'german'
lang4 = 'brazilish'
lang5 = 'spanish'
languages = []

def lang_to_languages(lang):
    languages.append(lang)
    return languages


lang_to_languages(lang1)
lang_to_languages(lang2)
lang_to_languages(lang3)
lang_to_languages(lang4)
lang_to_languages(lang5)
print(languages)
languages.insert(0,'japanise')
print(languages)
del languages[0]
print(languages)
popped_language = languages.pop(-1)
print(languages)
print(f'popped language is {popped_language}')
print(sorted(languages, reverse=True))
print(languages)
languages.sort()
print(languages)
languages.reverse()
print(languages)
print(languages.index('russian'))
languages.remove('russian')
print(languages)
print(len(languages))