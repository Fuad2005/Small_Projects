import pygame, random, time, sys


pygame.init()
 
WIDTH, HEIGHT = 800, 600
 
FONT = pygame.font.SysFont("Consolas", int(WIDTH/20))
 
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
CLOCK = pygame.time.Clock()
player = pygame.Rect(WIDTH/2-20, HEIGHT-100, 30, 30)
enemy = pygame.Rect(random.randint(0, WIDTH-30), random.randint(0, HEIGHT/2.5), 30, 30)
bullet = pygame.Rect(WIDTH/2-10, HEIGHT-100, 10, 20)
dx, dy = 1, 0
bdx, bdy = 0, 0
while True:

    bullet.x += bdx
    bullet.y += bdy

    key_pressed = pygame.key.get_pressed()
    if key_pressed [pygame.K_LEFT]:
        player.left -= 1
    elif key_pressed [pygame.K_RIGHT]:
        player.right += 1.5
    if key_pressed [pygame.K_SPACE]:
        bullet.x = player.x
        bdx, bdy = 0, -2
        pygame.draw.rect(SCREEN, "yellow", bullet)

            



    if enemy.x > WIDTH-30 or enemy.x < 0:
        dx = -dx
        enemy.y = enemy.y + 30
    enemy.x = enemy.x + dx
    enemy.y = enemy.y + dy

    for event in pygame.event.get():
    
    
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    SCREEN.fill("black")
    pygame.draw.rect(SCREEN, "white", player)
    pygame.draw.rect(SCREEN, "yellow", bullet)
    pygame.draw.rect(SCREEN, "red", enemy)

    pygame.display.update()
    CLOCK.tick(300)