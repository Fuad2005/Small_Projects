from turtle import screensize
import pygame, sys, random, time
 
pygame.init()
 
WIDTH, HEIGHT = 1280, 720
gravity = 2.5

 
FONT = pygame.font.SysFont("Consolas", int(WIDTH/20))
 
player = pygame.Rect(WIDTH/2, HEIGHT/2, 20, 20)

ground = pygame.Rect(0, HEIGHT-80, WIDTH, 20)


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer demo")
CLOCK = pygame.time.Clock()
 
while True:
    SCREEN.fill((0,0,0))
    pygame.draw.rect(SCREEN, (255,255,255), player)
    pygame.draw.rect(SCREEN, ('green'), ground)
    player.y += gravity
    
    

    if player.y >= ground.y-20:
        player.y = ground.y-20

    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_LEFT]:
        player.x -= 2
        
    if key_pressed[pygame.K_RIGHT]:
        player.x += 2
    
    if key_pressed [pygame.K_SPACE]:
        gravity = -2.3
        time.sleep(0.5)
        gravity = 2.5
            
        
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    pygame.display.update()
    CLOCK.tick(300)


