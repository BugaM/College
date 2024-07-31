
from simulation import Simulation
from constants.field_constants import ACCELERATED_STEPS
import pygame
import sys
from decision_making.decision import ConstantVsDecision, ConstantWsDecision, ShapePathDecision
from utils import build_shape_from_center
import numpy as np

# ACCELERATED = True
ACCELERATED = True

DRAW_PATH = True

GET_HISTORY = True

if ACCELERATED:
    steps = ACCELERATED_STEPS
else:
    steps = 1

# decision = ConstantWsDecision(np.array([[0.01,-0.01,-0.01,0.01]]).T)
# decision = ConstantVsDecision(np.array([[-0.06, 0.0, 0.00]]).T)
decision = ShapePathDecision(build_shape_from_center([[-100,100], [-100,-100], [100,-100], [100,100]]), 0.6, 0.05)
simulation = Simulation(decision)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            simulation.draw_ws_graphs()
            running = False

    # keys = pygame.key.get_pressed()
    simulation.run(steps, draw_path=DRAW_PATH, get_history=GET_HISTORY)

pygame.quit()
sys.exit()
