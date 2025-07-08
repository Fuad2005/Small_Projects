import pygame
import sys

# initialize pygame
pygame.init()

# set up the window
window = pygame.display.set_mode((400, 300))

# load sound files
kick = pygame.mixer.Sound("./sounds/kick.wav")
snare = pygame.mixer.Sound("./sounds/snare.wav")
hihat = pygame.mixer.Sound("./sounds/hihat.wav")
a = pygame.mixer.Sound("./sounds/a.wav")
b = pygame.mixer.Sound("./sounds/b.wav")
c = pygame.mixer.Sound("./sounds/c.wav")
d = pygame.mixer.Sound("./sounds/d.wav")
e = pygame.mixer.Sound("./sounds/e.wav")
f = pygame.mixer.Sound("./sounds/f.wav")
g = pygame.mixer.Sound("./sounds/g.wav")


# initialize clock
clock = pygame.time.Clock()

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                kick.play()
            if event.key == pygame.K_w:
                snare.play()
            if event.key == pygame.K_e:
                hihat.play()
            if event.key == pygame.K_z:
                a.play()
            if event.key == pygame.K_x:
                b.play()
            if event.key == pygame.K_c:
                c.play()
            if event.key == pygame.K_v:
                d.play()
            if event.key == pygame.K_b:
                e.play()
            if event.key == pygame.K_n: 
                f.play()
            if event.key == pygame.K_m:
                g.play()

    
    # update the screen
    pygame.display.update()
    clock.tick(60)
