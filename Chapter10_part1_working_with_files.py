# Упражнения из главы 10, часть 1 - работа с файлами

# С помощью функции "open" программа открывает файл. Затем с помощью "as" мы даем файлу название в программе.
# Затем с помощью метода "read()" мы присваиваем переменной "content" данные файла, а потом выводим их на экран (print).
with open("some_text.txt") as f:
    content = f.read()
print(content.rstrip())
# Конструкция с "with" закроет файл, когда надобность в нем отпадет. Помогает предотвращать ошибки в отличие от "close".
# Функция "open" оставляет пустую строку в конце. Чтобы ее убрать нужно использовать метод "rstrip", удаляющий пробелы
# справа.

# Также можно открыть файл, находящийся в другом директории, но нужно указать полный путь к этому файлу.
with open('/home/dkhorkov/Документы/bash_scripts/function.sh') as f:
    bass_content = f.read()
print(bass_content.rstrip())


# Программа ниже посчитает, сколько в файле, содержащем текст, встречается слово "яблоки":
with open("some_text.txt") as f:
    apples = f.read().split(" ")
#     count = 0
#     for apple in apples:
#         if apple == "яблоки":
#             count += 1
# print(count, end='\n\n')
    print(apples.count("яблоки"))


# Упражнения 10.1 - 10.2
# 10.1 - сделано на основе файла "some_text.txt":
    # 1) Чтение всего файла представлено в строках кода 5-7
    # 2) Перебор строк и их дальнейший вывод:
file = 'some_text.txt'
with open(file) as f:
    for line in f:
        print(line.strip())
print()
    # 3) Сохранение строк вв списке и их дальнейший вывод.
with open(file) as f:
    some_text_list = list(f)
for line in some_text_list:
    print(line.strip())
print()

# 10.2 также сделано на основе файла "some_text.txt":
with open(file) as f:
    text = f.read().replace("яблоки".lower(), 'груши'.upper())
print(text)


# Python может и записывать данные (похоже на команду "nano" и "touch" в bash-скриптах).
# В случае записи передается два аргумента: название файла, режим открытия файла:
# (r - чтение, w - запись, r+ (r +w), a - присоединение).
with open("writing_file.txt", 'w') as f:
    f.write('Here is some text to write it in new file with help of Python!')

# Поскольку режим записи удалит все данные из файла и запишет новые,
# то для добавления данных в файл (в конец файла) используем присоединение "а".
file_2 = "writing_file.txt"
with open(file_2, 'a') as f:
    f.write('\nAnd here is some text to add in this file.')


# Упражнения 10.3 - 10.5
# 10.3
guest_name = input('Please enter u\'r name: ')
with open("guest.txt", "w") as f:
    f.write(f'Guest\'s name is {guest_name.title()}.')

# 10.4
with open("guest_book.txt", "w") as f:
    mark = 1
    while True:
        guest_name = input('Please enter u\'r name: ')
        f.write(f'{mark}) Guest\'s name is {guest_name.title()}.\n')
        mark += 1
        cont = input('Do u wan\'t to add another guest\'s name?(y/n): ')
        while cont.lower() != 'y' and cont.lower() != 'n':
            cont = input('Error! Press "y" to add another guest\'s name or press "n" to end: ')
        if cont.lower() == 'n':
            break

# 10.5
with open("reasons_to_love_Python.txt", "w") as f:
    mark = 1
    while True:
        guest_name = input('Please enter u\'r name: ')
        reason = input('Please enter a reason, why u love Python: ')
        f.write(f'{mark}) {guest_name.title()} loves Python, because {reason.lower()}!\n')
        mark += 1
        cont = input('Do u wan\'t to add another reason?(y/n): ')
        while cont.lower() != 'y' and cont.lower() != 'n':
            cont = input('Error! Press "y" to add another reason or press "n" to end: ')
        if cont.lower() == 'n':
            break
