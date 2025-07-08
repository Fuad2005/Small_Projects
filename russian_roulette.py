import random
numbers = [1, 2, 3, 4, 5, 6]
dead = False
p1 = True

print('Player 1')
while(not dead):
    if input() == 's':
        p1 = not p1
        number = random.choice(numbers)
        if(number == 1):
            print('\nDEAD\n')
            if p1:
                print('Player 1 Won')
            else:
                print('Player 2 Won')
            dead=True
        else:
            print(f'{len(numbers)-1} bullets left')
            if p1:
                print('Player 1')
            else:
                print('Player 2')
            numbers.remove(number)
            number = random.choice(numbers)