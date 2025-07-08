# import pygame, time, random, sys


# pygame.init()
# width = 640
# height = 600
# screen = pygame.display.set_mode((width, height))
# done = False
# CLOCK = pygame.time.Clock()
# player_x = width//2 -50
# player_y = height-30






# while not done:
#     player = pygame.Rect(player_x, player_y, 100, 20)
#     ball_x = width//2
#     ball_y = 30
#     ball_dy = 2.5
#     ball = pygame.Rect(width//2, height//2, 20, 20)
#     ball.center = (ball_x, ball_y)
#     ball_y+=ball_dy
#     if ball_y == player_y-20 and ball_x in range(player_x, player_x+100):
#         ball_dy = -ball_dy
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#         elif event.type == pygame.MOUSEMOTION:
#             player_x = event.pos[0] - 50
    
    
#     screen.fill((0, 0, 0))
#     pygame.draw.rect(screen, 'white', player)
#     pygame.draw.circle(screen, 'white', ball.center, 10)

#     pygame.display.update()
#     CLOCK.tick(300)





import pygame
import random, time

pygame.init()
height = 500
width = 400
FONT = pygame.font.SysFont("Consolas", int(width/10))
screen = pygame.display.set_mode((width, height))
score = 0

pad_color = (255, 0, 0)
pad_x = 200
pad_y = height - 20
pad_width = 100
pad_height = 20

ball_color = (0, 255, 0)
ball_x = random.randint(0, 400)
ball_y = 0
ball_radius = 12

clock = pygame.time.Clock()
score_txt = FONT.render(str(score), True, "white")
game_over = False
running = True
while running:
    if(game_over):
        screen.fill((0,0,0))
        msg = FONT.render("Game Over!", True, (255,255,255))
        screen.blit(msg,[width//3, height//3])
        screen.blit(score_txt, [width//3+16, height//3+30])
        time.sleep(2)
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            pad_x = event.pos[0] - 50
    
    ball_y += 18
    
    if (ball_x + ball_radius >= pad_x and ball_x - ball_radius <= pad_x + pad_width) and (ball_y + ball_radius >= pad_y):
        ball_x = random.randint(0, 400)
        ball_y = 0
        score += 1
    
    if ball_y > height:
        ball_x = random.randint(0, 400)
        ball_y = 0
        game_over = True
    

    
    screen.fill((0,0,0))
    
    score_txt = FONT.render(str(score), True, "white")
    pygame.draw.rect(screen, pad_color, (pad_x, pad_y, pad_width, pad_height))
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    screen.blit(score_txt, (width//2-10, 50))
    pygame.display.update()
    
    clock.tick(60)


pygame.quit()
