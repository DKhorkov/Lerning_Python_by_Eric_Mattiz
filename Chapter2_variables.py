import this
# Упражнения из главы 2

message = 'hello world'
print(message.title())

# 'title' метод выводит каждое слово с заглавной буквы
message = 'hello my dear world'
print(message.title())

# f- строки
first_name = 'dima'
last_name = 'khorkov'
# помним про пробел между двумя значениями форматирующей строки. Разницы между двумя принтами нет. Тут уж как удобнее
full_name = f'{last_name.title()} {first_name.title()}'
print(f'Hello, {full_name}')
print('Hello, ' + full_name)

# 'rstrip', 'lstrip' и 'strip методы удаляют пропуски (справа, слева и с обеих сторон текста).
# чаще всего используются для очистки пользовательского ввода перед его сохранением в БД или системе
# тут в программе я немного поэкспериментировал:
# 1) проверил, что 'strip' удаляет только пробелы до текста и в конце, но не по середине
# 2) вспомнил, как работает метод 'replace' для текстовых переменных
# 3) попрактиковался с форматирующей строкой и методом 'title' внутри нее
first_name = input('Введите ваше Имя с пробелом справа, слева или с обеих сторон:\t')
print(first_name)
first_name = first_name.strip()
first_name = first_name.replace(' ', '')
print(f'!{first_name.title()}!')


# Упражнения 2.3 - 2.6

first_name = 'Lisa'
print(f"Hello, {first_name}, do u want to learn some Python?")
print(first_name.lower(),first_name.upper(),first_name.title())
# ниже поигрались с возможностями вывода текстовой информации или вообще формата 'string'
print('Мартин Иден - Персонаж произведения романа Джека лондона сказал одну прекрасную фразу:\n'
      '"Умные люди часто бывают жестоки. Глупые люди жестоки сверх всякой меры"')
famous_preson = 'Мартин Иден - Персонаж произведения романа Джека лондона сказал одну прекрасную фразу:\n'
message = 'Умные люди часто бывают жестоки. Глупые люди жестоки сверх всякой меры'
print(famous_preson + '"' + message + '"')
print(f'{famous_preson}"{message}"')
# упражнение 2.7 см. выше в самом начале


# тут небольшой эксперимент с вещественными числами и функцией окргуления 'round'
x = float(input('Enter "x"'))
y = float(input('Enter "y"'))
print(round(x*y, 2))
# символы подчеркивания "_" в числах нужны для облегчения чтения больших чисел в коде
num = 14_999_252_252
print(f'Number is {num}')
# множестевнно присвоение переменных - изи для питоняши
x, y, z = int(input('Enter number')), int(input('Enter number')), int(input('Enter number'))
print(y*z)
# в питоне нет встроенных констант. Но их можно легко сделать путем создания новой переменной.
# названия таких переменных принято писать в верхнем регистре
CONST = 10

# Упражнение 2.8 - 2.9
print(3+5)
print(int(16/2))
print(2*4)
print(12-4)
MY_FAV_NUM = 16
message = 'My favourite mumber is {}'
print(message.format(MY_FAV_NUM))
# 2.10 - это комментарии. Представлены выше
