import random

number = random.randint(1, 100)
finished = False
atts = 10
print('\nA computer got a number between 1 and 100. Try to guess it\n')

while(not finished):
    if atts:
        answer = input('Make A Guess: ')
    else:
        print(f'You lost. The number was {number}')
        finished = True
    if int(answer) > number:
        print('Lower\n')
        atts-= 1
        print(f'{atts} attempts left')

    elif int(answer) < number:
        print('Higher\n')
        atts-= 1
        print(f'{atts} attempts left')
    else:
        print(f'You won. The number is {number}')
        finished = True
