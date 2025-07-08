from ast import While
import pygame
import random
import time

pygame.init()

width, height = 400, 400
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Snake Game")


x,y = 200, 200
dx, dy = 10, 0

food_x, food_y = random.randrange(0, width)//10*10, random.randrange(0, height)//10*10
body_list = [(x, y), (x-10, y), (x-20, y)]

clock = pygame.time.Clock()

game_over = False
font = pygame.font.SysFont("bahnschriftl", 30)


def snake():
    global x, y, food_x, food_y, game_over, score

    x = (x + dx) % width
    y = (y + dy) % height
    

    if((x, y) in body_list):
        game_over = True
        print("Game Over")
        
        return


    body_list.append((x, y))


    if(food_x == x and food_y == y):
        while((food_x, food_y) in body_list):
            food_x, food_y = random.randrange(0, width)//10*10, random.randrange(0, height)//10*10
            body_list.append((x, y))

    else:
        del body_list[0]
    
    game_screen.fill((0,0,0))
    score = font.render("Score: "+ str(len(body_list)), True, (255, 255, 0))
    game_screen.blit(score, [0, 0])
    pygame.draw.rect(game_screen, (255,0,0), [food_x, food_y, 10, 10])
    for i in body_list:
        pygame.draw.rect(game_screen, (0,255,0), [i[0], i[1], 10, 10])
    pygame.display.update()

while True:
    if(game_over):
        game_screen.fill((0,0,0))
        msg = font.render("Game Over!", True, (255,255,255))
        game_screen.blit(msg,[width//3, height//3])
        game_screen.blit(score, [width//3+16, height//3+30])
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        quit()
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if dx !=10:
                    dx = -10
                    dy = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if dx !=-10:
                    dx = 10
                    dy = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                if dy !=10:
                    dx = 0
                    dy = -10
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if dy !=-10:
                    dx = 0
                    dy = 10
            else:
                continue
            snake()
    if not events:
        snake()
    clock.tick(20)


