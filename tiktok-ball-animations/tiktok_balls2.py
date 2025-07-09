"""
Every time ball hits the circle, it gets bigger
"""


import pygame
import numpy as np
import math
import random

pygame.init()




WIDTH = 800
HEIGHT = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
CIRCLE_CENTER = np.array([WIDTH/2, HEIGHT/2], dtype=np.float64)
CIRCLE_RADIUS = 150
GRAVITY = 0.2

ball_radius = 10
ball_pos = np.array([WIDTH/2, HEIGHT/2 - 120], dtype=np.float64)
ball_vel = np.array([random.uniform(-4 ,4), random.uniform(-1 ,1)], dtype=np.float64)
ball_is_in = True

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False





    ball_vel[1] += GRAVITY
    ball_pos += ball_vel

    dist = np.linalg.norm(ball_pos - CIRCLE_CENTER)
    if dist + ball_radius > CIRCLE_RADIUS:
        ball_radius += 2

        if ball_is_in:
            d = ball_pos - CIRCLE_CENTER
            d_unit = d / np.linalg.norm(d)
            ball_pos = CIRCLE_CENTER + (CIRCLE_RADIUS - ball_radius) * d_unit
            tangent = np.array([-d[1], d[0]], dtype=np.float64)
            proj_v_t = (np.dot(ball_vel, tangent) / np.dot(tangent, tangent)) * tangent
            ball_vel = 2*proj_v_t - ball_vel



    window.fill(BLACK)
    pygame.draw.circle(window, WHITE, CIRCLE_CENTER, CIRCLE_RADIUS, 3)
    pygame.draw.circle(window, RED, ball_pos, ball_radius)
    pygame.display.flip()

    clock.tick(60)


pygame.quit()