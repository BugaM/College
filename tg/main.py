import pygame
import sys
from simulation import *

ACCELERATED = True
# ACCELERATED = False


def draw():
    screen.fill(FIELD_COLOR)
    pygame.draw.circle(screen, PLAYER_COLOR, player_pos, PLAYER_RADIUS)
    pygame.draw.circle(screen, BALL_COLOR, ball_pos, BALL_RADIUS)
    for goal in goals:
        pygame.draw.rect(screen, GOAL_COLOR, goal)
    pygame.display.flip()

# Main game loop
running = True
steps = 1
# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
if ACCELERATED:
    steps = ACCELERATED_STEPS
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    for i in range(steps):
        update_player(keys)
        update_ball()
        check_goal()
        check_collision()
    draw()

    clock.tick(60)

pygame.quit()
sys.exit()
