# Упражнения из главы 7 - Пользовательский ввод и цикл "while"

# Если с функцией "input" мы хотим вывести длинную подсказку, то можно сделать по примеру ниже:
your_text_for_input = 'Допустим мы здесь хотим оставить оооочень длинную подсказку для пользователя, в которой будет '
your_text_for_input += 'много всякого текстаааа, который очень поможет поользователю.'
your_text_for_input += "\nНу, в общем понятно."
x = input(your_text_for_input)

# Упражнения 7.1 - 7.10
# 7.1
car = input('What car do u want to drive?: ')
print(f'Let me see if I can find a {car.title()} for you.')
# 7.2
table = int(input('For how many persons do u want to book the table?:'))
if table > 8:
    print('Sorry, u have to wait...')
else:
    print('U\'r table is ready!')
# 7.3
number = int(input('Please enter an integer number: '))
if number % 10 == 0:
    print('U\' number is multiple of 10')
else:
    print('U\' number is NOT multiple of 10')
# 7.4
toppings = []
while True:
    x = input('Что хотите добавить в вашу пиццу?(Для выхода введите "выход"):\t')
    stop_list = ['выход', 'стоп', 'ничего']
    if x.lower() in stop_list:
        break
    toppings.append(x)
    print(f'{x} - дополнение добавлено в ваш заказ. \nНа данный момент список добавок следующий:')
    order = 1
    for topping in toppings:
        print(f'{order}) {topping}')
        order += 1
# 7.5
prices = [0, 10, 15]
active = True
while active:
    age = input('Пожалуйста введите ваш возраст (Для выхода введите "выход"):\t')
    if age.lower() in stop_list:
        active = False
        break
    age = int(age)
    if age < 3:
        print(f'Ваш билет будет стоить {prices[0]}$.')
    if 3 <= age <= 12:
        print(f'Ваш билет будет стоить {prices[1]}$.')
    if age > 12:
        print(f'Ваш билет будет стоить {prices[2]}$.')
# 7.6 Выполнено в рамках 7.4 и 7.5
# 7.7 - бесконечный цикл представлен в комментариях ниже:
# a = 1
# while True:
#     print(a)
# 7.8 и 7.9 (2 в одном)
sandwich_orders = ['pastrami', 'с мясом', 'с сыром и ветчиной', 'pastrami', 'с грибами и картошкой', 'с курицей',
                   'с лососем', 'pastrami']
finished_sandwiches = []
print('There\'s no more pastrami, sorry!')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    x = sandwich_orders.pop()
    print(f'Готовлю для вас сэндвич {x}!')
    finished_sandwiches.append(x)
mark = 1
print('Список готовых сэндвичей:')
for sandwich in finished_sandwiches:
    print(f'{mark}) {sandwich}')
    mark += 1
# 7.10
poll = {}
while True:
    name = input('Как вас зовут?:\t')
    question = input('Где бы вы хотели провести отпуск?:\t')
    active = True
    poll[name] = question
    next_person = input('Позовете друга, чтобы он тоже прошел опрос?(Да/нет):\t')
    correct_answers = ['да', 'нет']
    while next_person.lower() not in correct_answers:
        next_person = input('Вы ошиблись, пожалуйста, введите "да" иди "нет":\t')
    if next_person.lower() == 'нет':
        break
for k,v in poll.items():
    print(f'{k.title()} wants to spend a vacation {v}.')
