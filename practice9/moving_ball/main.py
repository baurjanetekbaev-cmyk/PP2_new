import pygame
import sys
from ball import Ball

WIDTH, HEIGHT = 800, 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball Game")
clock = pygame.time.Clock()

ball = Ball(WIDTH, HEIGHT)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                ball.move("UP")
            elif event.key == pygame.K_s:
                ball.move("DOWN")
            elif event.key == pygame.K_a:
                ball.move("LEFT")
            elif event.key == pygame.K_d:
                ball.move("RIGHT")

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (ball.x, ball.y), ball.radius)
    pygame.display.flip()
    clock.tick(60)