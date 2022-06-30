# Упражнения из главы 5
# 5.1
car = 'bwm'.upper()
print('Is can BWM? I guess True.')
print(car == 'BWM')
print('Is can BWN? I guess False.')
print(car == 'BWN')
color = 'black'
print('Is color black? I guess True.')
print(color == 'black')
print('Is color blue? I guess False.')
print(color == 'blue')
print('Is color BLACK? I guess False.')
print(color == 'BLACK')

# 5.2
color = input('Enter color:')
print('Color is blue?', color == 'blue')
color = color.lower()
print('Color is blue?', color == 'blue')
x = 5
y = 5 - 2
print('x = y?', x == y)
if x >= y and y <= 3:
    print(x)
elif x >= y or y <= 4:
    print(y)
names = ['андрей', 'дима', 'света', 'вера']
if 'ВЕРА'.lower() in names:
    print(True)
if not 'Петр'.lower() in names:
    print(False)

# 5.3
color = 'green'
if color == 'red':
    print('U earned 5 points')

# 5.4
# 1st version
color = 'green'
if color == 'red':
    print('U earned 5 points')
else:
    print('U earned 10 point')
# 2nd version
color = 'red'
if color == 'red':
    print('U earned 5 points\n')
else:
    print('U earned 10 point\n')

# 5.5
# 1st version
color = 'green'
if color == 'green':
    print('U earned 5 points')
elif color == 'yellow':
    print('U earned 10 points')
else:
    print('U earned 15 points')
# 1st version
color = 'yellow'
if color == 'green':
    print('U earned 5 points')
elif color == 'yellow':
    print('U earned 10 points')
else:
    print('U earned 15 points')
# 3rd version
color = 'red'
if color == 'green':
    print('U earned 5 points')
elif color == 'yellow':
    print('U earned 10 points')
else:
    print('U earned 15 points')

# 5.6
age = int(input('Enter u\'r age:'))
if age < 2:
    print('baby')
elif 2 <= age < 4:
    print('child')
elif 4 <= age < 13:
    print('kid')
elif 13 <= age < 20:
    print('teenager')
elif 20 <= age < 65:
    print('adult')
else:
    print('old')

# 5.7
favourite_fruits = ['banana', 'apple', 'pineapple']
if 'banana' in favourite_fruits:
    print('U really like bananas.')
if 'strawberry' in favourite_fruits:
    print('U really like strawberry.')
if 'cherry' in favourite_fruits:
    print('U really like cherry.')
if 'apple' in favourite_fruits:
    print('U really like apple.')
if 'pineapple' in favourite_fruits:
    print('U really like pineapple.')


# 5.8
user_names = ['admin', 'd3m0s', 'dracula', 'shaman', 'konin', 'hikfe']
for user_name in user_names:
    if user_name == 'admin':
        print('Hello, admin, would you like to see a status report?')
    else:
        print('Hello Jaden, thank you for logging in again.')

# 5.9
user_names2 = []
if user_names2:
    for user_name in user_names2:
        if user_name == 'admin':
            print('Hello, admin, would you like to see a status report?')
        else:
            print('Hello Jaden, thank you for logging in again.')
else:
    print('We need to ind some users!')

# 5.10
current_users = ['siso', 'piso', 'miso', 'diso', 'liso']
new_users = ['liso', 'siso', 'kiso', 'hiso', 'jiso']
for new_user in new_users:
    if new_user in current_users:
        print(f'Match with current users: {new_user}')
    else:
        print(f'Really new user: {new_user}\n')

current_users = ['siso', 'piso', 'miso', 'diso', 'liso']
new_users = ['Liso', 'SisO', 'kiSo', 'hiSo', 'jIso']
for new_user in new_users:
    if new_user.lower() in current_users:
        match = current_users.index(new_user.lower())
        print(f'User must take another login: {new_user} vs {current_users[match]}')
    else:
        print(f'Login is free: {new_user}')

# 5.11
number_list = list(range(1, 10))
for number in number_list:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')
