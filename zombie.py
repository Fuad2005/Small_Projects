import time

print('============================\n\
You: Wh... what, where am I?\n\
============================\n')
input('Press enter to continue')
print('============================\n\
You: Oh God it hurts so much!\n\
============================\n')
input('Press enter to continue')
print('===================================================================\n\
You: All I remember is that I... WAIT, I DON\'T REMEMBER ANYTHING!!!\n\
===================================================================\n')
input('Press enter to continue')
print('=================================\n\
You: What happened to this place?\n\
=================================\n')
print('-You woke up in your workplace full of blood and dead bodies.\n')
input('Press enter to continue')
print('=================================\n\
You: What should I do now?\n\
=================================\n')
print('1. Go explore rooms\n2. Try to find the exit')

answer = input('\nType 1 / 2: ')

if answer == '1':
    print('==============================\n\
You: I should go explore rooms\n\
==============================\n')
    input('Press enter to continue')
    print('=================================\n\
You: Well, I see 2 rooms in front of me\n\
which one should I enter?\n\
=================================\n')
    print('1. Enter the room on the left\n2. Enter the room on the right')
    answer = input('\nType 1 / 2: ')
    if answer == '1':
        print('========================================\n\
You: I should enter the room on the left\n\
========================================\n')
        input('Press enter to continue')
        print('===========================================\n\
You: There is such a terrible mess in here\n\
===========================================\n')
        input('Press enter to continue')
        print('=========================================================================================\n\
You: Wait!! I think i see someone, he moves so strangly though, not like a normal person.\n\
=========================================================================================\n')
        input('Press enter to continue')
        print('========================================\n\
You: What should I do?\n\
========================================\n')
        print('1. Try to talk to him\n2. Try to run away')
        answer = input('\nType 1 / 2: ')
        if answer == '1':
            print('========================================\n\
You: I should try to talk to him\n\
========================================\n')
            input('Press enter to continue')
            print('==========================\n\
You: Hello? Are you ok?\n\
==========================\n')
            input('Press enter to continue')
            print('========================================\n\
Zombie turns around and looks at you.\n\
========================================\n')
            input('Press enter to continue')
            print('========================================\n\
It is growling at you. It jumped on you\n\
========================================\n')
            input('Press enter to continue')
            print('=======================\n\
And ate your face...\n\
=======================\n')
            input('Press enter to continue')
            print('=================\n\
YOU ARE DEAD!...\n\
=================\n')
            print('Restart the program to try again\n')
            time.sleep(1)
        elif answer == '2':
            print('========================================\n\
You: I should try to run away\n\
========================================\n')
            input('Press enter to continue')
    elif answer == '2':
        print('==================================\n\
You: I should enter the room on the right\n\
==================================\n')
        input('Press enter to continue')



elif answer == '2':
    print('==================================\n\
You: I should try to find the exit\n\
==================================\n')

