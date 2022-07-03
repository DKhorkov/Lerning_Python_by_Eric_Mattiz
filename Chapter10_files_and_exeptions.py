# Упражнения из главы 10 - работа с файлами и исключениями

# С помощью функции "open" программа открывает файл. Затем с помощью "as" мы даем файлу название в программе.
# Затем с помощью метода "read()" мы присваиваем переменной "content" данные файла, а потом выводим их на экран (print).
with open("some_text.txt") as some_text:
    content = some_text.read()
print(content.rstrip())
# Конструкция с "with" закроет файл, когда надобность в нем отпадет. Помогает предотвращать ошибки в отличие от "close".
# Функция "open" оставляет пустую строку в конце. Чтобы ее убрать нужно использовать метод "rstrip", удаляющий пробелы
# справа.

# Также можно открыть файл, находящийся в другом директории, но нужно указать полный путь к этому файлу.
with open('/home/dkhorkov/Документы/bash_scripts/function.sh') as bash:
    bass_content = bash.read()
print(bass_content.rstrip())


# Программа ниже посчитает, сколько в файле, содержащем текст, встречается слово "яблоки":
with open("some_text.txt") as some_text:
    apples = some_text.read().split(" ")
    count = 0
    for apple in apples:
        if apple == "яблоки":
            count += 1
print(count, end='\n\n')


# Упражнения 10.1 - 10.2
# 10.1 - сделано на основе файла "some_text.txt":
    # 1) Чтение всего файла представлено в строках кода 5-7
    # 2) Перебор строк и их дальнейший вывод:
file = 'some_text.txt'
with open(file) as some_text:
    for line in some_text:
        print(line.strip())
print()
    # 3) Сохранение строк вв списке и их дальнейший вывод.
with open(file) as some_text:
    some_text_list = list(some_text)
for line in some_text_list:
    print(line.strip())
print()

# 10.2 также сделано на основе файла "some_text.txt":
with open(file) as some_text:
    text = some_text.read().replace("яблоки".lower(), 'груши'.upper())
print(text)


# Python может и записывать данные (похоже на команду "nano" и "touch" в bash-скриптах).
# В случае записи передается два аргумента: название файла, режим открытия файла:
# (r - чтение, w - запись, r+ (r +w), a - присоединение).
with open("writing_file.txt", 'w') as writing_file:
    writing_file.write('Here is some text to write it in new file with help of Python!')

# Поскольку режим записи удалит все данные из файла и запишет новые,
# то для добавления данных в файл (в конец файла) используем присоединение "а".
file_2 = "writing_file.txt"
with open(file_2, 'a') as writing_file:
    writing_file.write('\nAnd here is some text to add in this file.')


# Упражнения 10.3 - 10.5
# 10.3
guest_name = input('Please enter u\'r name: ')
with open("guest.txt", "w") as g_name:
    g_name.write(f'Guest\'s name is {guest_name.title()}.')

# 10.4
with open("guest_book.txt", "w") as g_book:
    mark = 1
    while True:
        guest_name = input('Please enter u\'r name: ')
        g_book.write(f'{mark}) Guest\'s name is {guest_name.title()}.\n')
        mark += 1
        cont = input('Do u wan\'t to add another guest\'s name?(y/n): ')
        while cont.lower() != 'y' and cont.lower() != 'n':
            cont = input('Error! Press "y" to add another guest\'s name or press "n" to end: ')
        if cont.lower() == 'n':
            break

# 10.5
with open("reasons_to_love_Python.txt", "w") as poll_book:
    mark = 1
    while True:
        guest_name = input('Please enter u\'r name: ')
        reason = input('Please enter a reason, why u love Python: ')
        poll_book.write(f'{mark}) {guest_name.title()} loves Python, because {reason.lower()}!\n')
        mark += 1
        cont = input('Do u wan\'t to add another reason?(y/n): ')
        while cont.lower() != 'y' and cont.lower() != 'n':
            cont = input('Error! Press "y" to add another reason or press "n" to end: ')
        if cont.lower() == 'n':
            break
