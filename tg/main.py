
from simulation import Simulation
from constants.field_constants import ACCELERATED_STEPS
import pygame
import sys
from decision_making.decision import ConstantVsDecision, ConstantWsDecision, ShapePathDecision
from utils import build_shape_from_center
import numpy as np

# ACCELERATED = True
ACCELERATED = False

DRAW_PATH = True
if ACCELERATED:
    steps = ACCELERATED_STEPS
else:
    steps = 1

# decision = ConstantWsDecision(np.array([[0.01,-0.01,-0.04,0.3]]).T)
# decision = ConstantVsDecision(np.array([[-0.6, 0.1, 0.02]]).T)
decision = ShapePathDecision(build_shape_from_center([[-100,100], [-100,-100], [100,-100], [100,100]]), 0.5, 0.1)
simulation = Simulation(decision)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keys = pygame.key.get_pressed()
    simulation.run(steps, draw_path=DRAW_PATH)

pygame.quit()
sys.exit()
