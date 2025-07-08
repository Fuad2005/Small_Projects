import pygame

# Initialize pygame and set up window
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Load player sprite
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()

# Set player starting position
player_rect.left = 100
player_rect.top = 500

# Set up platforms
platforms = []
platforms.append(pygame.Rect(0, 550, 800, 50))
platforms.append(pygame.Rect(150, 450, 500, 50))

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player based on key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.left -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.right += 5
    if keys[pygame.K_UP]:
        player_rect.top -= 5
    if keys[pygame.K_DOWN]:
        player_rect.bottom += 5

    # Check for collisions with platforms
    for platform in platforms:
        if player_rect.colliderect(platform):
            player_rect.bottom = platform.top

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, (0, 255, 0), platform)

    # Draw player
    screen.blit(player_image, player_rect)

    # Update screen
    pygame.display.update()

    # Limit frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
