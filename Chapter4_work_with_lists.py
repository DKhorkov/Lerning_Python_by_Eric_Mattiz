# Упражнения из главы 4

# 4.1 - 4.2
pizzas = ['peperoni', '4 cheeses', 'havana']
for pizza in pizzas:
    print(f' My favourite pizza is {pizza}!')
print('\nPizza is great!')

animals = ['Cat', 'Dog', 'Rat']
for animal in animals:
    print(f'A {animal} is beautiful')
print('\nAll these animals have four legs.')

# числовой список через функцию 'range'
range_list = list(range(0, 10))
print(range_list)

# список - матрица и его сортировка (по первой цифре внутри мини-списка)
list_of_lists = [
    [1, 1, 1],
    [3, 5, 8],
    [0, 1, 2]
]
print(sorted(list_of_lists, reverse=True))
print(list_of_lists[0::2])

# в 'range' как и в срезе можно использовать шаг
x = range(1, 10, 2)
for number in x:
    print(number)

# чтобы создать диапозон от нуля до числа (в данном случае "6"), можно сделать по примеру ниже.
# также тут решил использовать моржа ('Walrus'), чтобы сделать принт в одну строчку и сократить код
print(zero_start_range := list(range(6)))

# По аналогии с примером в книге, хочу вывести список удвоения чисел в диапозоне от 0 до 20:
double = []
for number in range(0, 21):
    number *= 2
    double.append(number)
print(double)
# или альтернатива по упрощению кода, но уже на примере взятия числа во 2 степень
double2 = []
for number in range(0, 21):
    double2.append(number ** 2)
print(double2)

# повторим базовые функции числовых списков
basic_list = []
for number in range(-10, 5):
    basic_list.append(number)
print(basic_list)
print(f'Сумма чисел в списке составляет: {sum(basic_list)}')
print(f'Сумма чисел в списке, взятая по модулю, составляет: {abs(sum(basic_list))}')
print(f'Самое большое число в списке: {max(basic_list)}')
print(f'Самое большое число в списке: {min(basic_list)}')
basic_list.append(1)
print(basic_list)
print(f'Сколько единиц в данном списке: {basic_list.count(1)}')

# пример генератора списков для сокращения кода. Использовал еще и 'Walrus', чтобы вывести в одну строку.
# стоит также не забывать в данном случае про КВАДРАТНЫЕ СКОБКИ, чтобы генератор вывел нам СПИСОК
# итог равен тому, что получается по результату кода на строках 37 - 41
print(double3 := [number * 2 for number in range(0, 11)])

# Задания 4.3 - 4.9
for number in range(1, 21):
    print(number)
# 4.4 заменил миллион на тысячу. В 4.5 также работал с тысячей
thousand = []
for i in range(1, 1_001):
    thousand.append(i)
print(thousand)
print(min(thousand))
print(max(thousand))
print(sum(thousand))
print(odd_numbers := list(range(1, 21, 2)))

dev_by_3 = []
for num in range(3, 31):
    if num % 3 == 0:
        dev_by_3.append(num)
print(dev_by_3)
for num in dev_by_3:
    print(num)
# задание 4.8 и 4.9 выполнены ниже одновременно
print(cube := [num ** 3 for num in range(1, 11)])
# в случае использовании среза с отрицательным значением - получим последние элементы списка, равные заданному числу (3)
print(cube[-3:])

# копирование списков делается через '[:]' чтобы скопировать все элементы текущего списка
my_food = ['meat', 'milk', 'tea', 'cheese']
her_food = my_food[:]
# при добавлении новых элементов в первостепенный список, копированный список не удлинняется
my_food.append('bread')
her_food.append('potato')
print(my_food, her_food, sep='\n')
# но если мы просто приравниваем списки, а не копируем, то добавление элемента в любой из них,
#                                                                             добавляет элемент и во второй список

# Задания 4.10 - 4.12
print(f'The first three items in list my_food are: {my_food[:3]}')
lenght = int(len(my_food)/2)
print(f'The first three items in the middle of list my_food are: {my_food[lenght - 1:lenght+2]}')
print(f'The last three items in list my_food are: {my_food[-3:]}')

friend_pizza = pizzas[:]
pizzas.append('mozarella')
friend_pizza.append('with mushrooms')
print('my favourite pizzas are:')
for pizza in pizzas:
    print(pizza)
print('my friend\'s favourite pizzas are:')
for pizza in friend_pizza:
    print(pizza)

restaraunt_menu = ('Pizza', 'Sushi', 'Scramble', 'steak', 'Fish')
for food in restaraunt_menu:
    print(f'There is a {food} in menu.')
# ниже безуспешная попытка изменить кортеж, а также пример вывода его элемента по индексу
# restaraunt_menu[0] = 'Eggs'
print(restaraunt_menu[0])
restaraunt_menu = ('Pizza', 'Sushi', 'Scramble', 'Eggs', 'Ice cream')
for food in restaraunt_menu:
    print(f'There is a {food} in menu.')
