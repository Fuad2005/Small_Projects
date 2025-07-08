import pygame, sys, random, time

pygame.init()

WIDTH, HEIGHT = 1280, 720

FONT = pygame.font.SysFont("Consolas", int(WIDTH/20))

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong!")
CLOCK = pygame.time.Clock()

#Paddles

player1 = pygame.Rect(WIDTH-60, HEIGHT/2-50, 10, 100)
# ai = pygame.Rect(50, HEIGHT/2-50, 10, 100)
player2 = pygame.Rect(50, HEIGHT/2-50, 10, 100)
p1_score, p2_score = 0, 0

#Ball
ball = pygame.Rect(WIDTH/2-10, HEIGHT/2-10, 20, 20)
dx, dy = 1, 1

while True:
    if p1_score == 5:
        SCREEN.fill("black")
        p1_win = FONT.render("Player 1 Wins!", True, "white")
        SCREEN.blit(p1_win, (WIDTH/2 - 230, HEIGHT/2))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()


    if p2_score == 5:
        SCREEN.fill("black")
        p2_win = FONT.render("Player 2 Wins!", True, "white")
        SCREEN.blit(p2_win, (WIDTH/2 - 230, HEIGHT/2))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_KP8]:
        if player1.top > 0:
            player1.top -= 2
    if key_pressed[pygame.K_KP5]:
        if player1.bottom < HEIGHT:
            player1.bottom += 2

    if key_pressed[pygame.K_w]:
        if player2.top > 0:
            player2.top -= 2
    if key_pressed[pygame.K_s]:
        if player2.bottom < HEIGHT:
            player2.bottom += 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
#Ball Logic
    if ball.y >= HEIGHT:
        dy = -1
    if ball.y <= 0:
        dy = 1
    if ball.x <= 0:
        p1_score += 1
        ball.center = (WIDTH/2, HEIGHT/2)
        dx, dy = random.choice([1, -1]), random.choice([1, -1])
    if ball.x >= WIDTH:
        p2_score += 1
        ball.center = (WIDTH/2, HEIGHT/2)
        dx, dy = random.choice([1, -1]), random.choice([1, -1])
    if player1.x - ball.width <= ball.x <= player1.x and ball.y  in range(player1.top - ball.width, player1.bottom + ball.width):
        dx = -1
    if player2.x - ball.width <= ball.x <= player2.x and ball.y  in range(player2.top - ball.width, player2.bottom + ball.width):
        dx = 1
    # if ai.x - ball.width <= ball.x <= ai.x and ball.y  in range(ai.top - ball.width, ai.bottom + ball.width):
    #     dx = 1
    

    ball.x += dx * 2
    ball.y += dy * 2
    

    # if ai.y < ball.y:
    #     ai.top += 1.5
    # if ai.y > ball.y:
    #     ai.top -= 1


    p1_score_txt = FONT.render(str(p1_score), True, "white")
    p2_score_txt = FONT.render(str(p2_score), True, "white")
    


    SCREEN.fill((0,0,0))
    pygame.draw.rect(SCREEN, "white", player1)
    pygame.draw.rect(SCREEN, "white", player2)
    pygame.draw.circle(SCREEN, "white", ball.center, 10)
    SCREEN.blit(p1_score_txt, (WIDTH/2 + 25, 50)) 
    SCREEN.blit(p2_score_txt, (WIDTH/2 - 50, 50))
    
    # pygame.draw.rect(SCREEN, "white", ai)
    pygame.display.update()
    CLOCK.tick(300)