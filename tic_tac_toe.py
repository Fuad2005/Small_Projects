board = [x+1 for x in range(9)]

game = '|{}||{}||{}|\n|{}||{}||{}|\n|{}||{}||{}|'.format(
    board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8])
finished = False
player = 'X'
print(game)


def victory_check():
    if (board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or (board[1] == 'X' and board[4] == 'X' and board[7]) or (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or (board[2] == 'X' and board[4] == 'X' and board[6] == 'X'):
        print('Player X Won')
        return True
    if (board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or (board[6] == 'O' and board[7] == 'O' and board[8] == 'O') or (board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or (board[1] == 'O' and board[4] == 'O' and board[7]) or (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or (board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or (board[2] == 'O' and board[4] == 'O' and board[6] == 'O'):
        print('Player O Won')
        return True



board = [" " for x in range(9)]
while (not finished):
    if player == 'X':
        value = input('Player X: ')
        if value == '1' and board[0] == ' ':
            board[0] = 'X'
        elif value == '2' and board[1] == ' ':
            board[1] = 'X'
        elif value == '3' and board[2] == ' ':
            board[2] = 'X'
        elif value == '4' and board[3] == ' ':
            board[3] = 'X'
        elif value == '5' and board[4] == ' ':
            board[4] = 'X'
        elif value == '6' and board[5] == ' ':
            board[5] = 'X'
        elif value == '7' and board[6] == ' ':
            board[6] = 'X'
        elif value == '8' and board[7] == ' ':
            board[7] = 'X'
        elif value == '9' and board[8] == ' ':
            board[8] = 'X'
        else:
            player = 'X'
            print('That tile is already taken')
            continue
        player = 'O'
        game = '|{}||{}||{}|\n|{}||{}||{}|\n|{}||{}||{}|'.format(
            board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8])
        print(game)
        if victory_check():
            finished = True
    else:
        value = input('Player O: ')
        if value == '1' and board[0] == ' ':
            board[0] = 'O'
        elif value == '2' and board[1] == ' ':
            board[1] = 'O'
        elif value == '3' and board[2] == ' ':
            board[2] = 'O'
        elif value == '4' and board[3] == ' ':
            board[3] = 'O'
        elif value == '5' and board[4] == ' ':
            board[4] = 'O'
        elif value == '6' and board[5] == ' ':
            board[5] = 'O'
        elif value == '7' and board[6] == ' ':
            board[6] = 'O'
        elif value == '8' and board[7] == ' ':
            board[7] = 'O'
        elif value == '9' and board[8] == ' ':
            board[8] = 'O'
        else:
            player = 'O'
            print('That tile is already taken')
            continue
        player = 'X'
        game = '|{}||{}||{}|\n|{}||{}||{}|\n|{}||{}||{}|'.format(
            board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8])
        print(game)
        if victory_check():
            finished = True
    if ' ' not in board:
        print('Draw!')
        finished = True
