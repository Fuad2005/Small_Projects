import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_chars = '''!@#$%^&*()_-+={}[]|\:;"/'<>,.?/~`'''


print('\nThis is custom password generator. Please indicate all parameters\n')


while True:
    pass_length = int(input('Numeber of characters(4-99): '))

    if 4 <= pass_length <= 99:
        break
    else:
        print('Enter a number between 4-99')


while True:
    option = int(input('\nChoose option(1-4):\n1. Only numeric\n2. Only alphabetic\n3. Alpha-numeric\n4. Everything included\n>>>'))

    if 1 <= option <= 4:
        break
    else:
        print('Enter a value between 1-4')



if option == 1:
    password = [random.choice(numbers) for _ in range(pass_length)]
elif option == 2:
    password = [random.choice(letters) for _ in range(pass_length)]
elif option == 3:
    password = [random.choice(numbers + letters) for _ in range(pass_length)]
elif option == 4:
    password = [random.choice(numbers + letters + special_chars) for _ in range(pass_length)]


print(*password, sep='')
