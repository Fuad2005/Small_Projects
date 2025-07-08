import random
import art
print("""
==========================================================================
Hey, this is a Rock Paper Scissors game in console.
You have to pick Rock, Paper, or Scissors. Then AI will make its choice.
Winner gets 1 point.
Game continues until the score of 5.
===========================================================================
""")

allowed_options = ['s', 'r', 'p']
notation = {
    'r': 'Rock',
    'p': 'Paper',
    's': 'Scissors',
}
game = True
player = 0
bot = 0

while game:
    choice = input('Make Your Choice(r, p, s): ')
    bot_choice = random.choice(allowed_options)
    if not choice in allowed_options:
        print('Pick Rock, Paper, or Scissors')
        continue
    

    if allowed_options.index(choice) > allowed_options.index(bot_choice):
        if allowed_options.index(choice) - allowed_options.index(bot_choice) <= 1:
            player+=1
        else:
            bot+=1
    elif allowed_options.index(choice) < allowed_options.index(bot_choice):
        if allowed_options.index(bot_choice) - allowed_options.index(choice) <= 1:
            bot+=1
        else:
            player+=1



    print(f'\n  Player  |    Bot   \n-----------------------\n{notation[choice].center(9)} |{notation[bot_choice].center(10)}\n')
    print(f'Player: {player}\nBot: {bot}')



    if bot == 5 or player == 5:
        print(art.text2art("Y0u Lost") if bot==5 else art.text2art("You Won"))
        game = False

