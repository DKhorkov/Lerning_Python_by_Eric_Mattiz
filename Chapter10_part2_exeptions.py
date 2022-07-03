# Упражнения из главы 10, часть 2 - работа с исключениями

# Упражнения 10.6 - 10.10
# 10.6
print('Summing two numbers')
n1 = input('Enter first number: ')
n2 = input('Enter second number: ')
try:
    result = int(n1)+ int(n2)
except ValueError:
    print('Operation couldn\'t be done!U have entered a string, not a number!\n')
else:
    print(result,end='\n\n')

# 10.7
print('Summing two numbers')
while True:
    print('Enter "q" to quit.')
    n1 = input('Enter first number: ')
    if n1.lower() == 'q':
        break
    n2 = input('Enter second number: ')
    if n2.lower() == 'q':
        break
    try:
        result = int(n1) + int(n2)
    except ValueError:
        print('Operation couldn\'t be done!U have entered a string, not a number!\n')
    else:
        print(result)


# 10.8
def pet_names(file):
    """Выводит имена питомцев из файлов."""

    try:
        with open(file) as f:
            names = f.read().split()
    except FileNotFoundError:
        print(f'Error. File "{file}" wasn\'t found!')
    else:
        mark = 1
        for name in names:
            print(f'{mark}) {name}')
            mark += 1


pet_names('cats.txt')
pet_names('dogs.txt')
pet_names('dogs_names/dogs.txt')


# 10.9 - Убираем уведомление пользователя о том, что файла нет в заданном директории.
def pet_names(file):
    """Выводит имена питомцев из файлов."""

    try:
        with open(file) as f:
            names = f.read().split()
    except FileNotFoundError:
        pass
    else:
        mark = 1
        for name in names:
            print(f'{mark}) {name}')
            mark += 1


pet_names('cats.txt')
pet_names('dogs.txt')


# 10.10
def count_word(file):
    """Считает количество повторений заданного слово в выбранном файле."""
    with open(file) as f:
        text = f.read()
    word = input(f"Enter the word to know how many times does it occurs in {file}:")
    print(f'The word "{word}" occurs in "{file}" {text.count(word.lower())} times.')


count_word("my_family.txt")
