import keyboard
import os

n = 10
board = [[0]*n for _ in range(n)]

x = 0
y = 0
direction = ''




while True:

    board[int(y)][int(x)] = 1

    if keyboard.is_pressed('left'):
        direction = 'left'

    if keyboard.is_pressed('right'):
        direction = 'right'

    if keyboard.is_pressed('up'):
        direction = 'up'

    if keyboard.is_pressed('down'):
        direction = 'down'


    if direction == 'left':
        x-=0.3
        y+=0

    if direction == 'right':
        x+=0.3
        y+=0

    if direction == 'up':
        x+=0
        y-=0.3

    if direction == 'down':
        x+=0
        y+=0.3  
    
    os.system('cls')
    for row in board:
        print(row)
    print(f"[{x},{y}]")
    print('\n')












