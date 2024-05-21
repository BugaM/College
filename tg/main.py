
from simulation import Simulation
from constants.field_constants import  ACCELERATED_STEPS
import pygame
import sys

# ACCELERATED = True
ACCELERATED = False

DRAW_PATH = True
if ACCELERATED:
    steps = ACCELERATED_STEPS
else:
    steps = 1

simulation = Simulation()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keys = pygame.key.get_pressed()
    simulation.run(steps, draw_path=DRAW_PATH)

pygame.quit()
sys.exit()
