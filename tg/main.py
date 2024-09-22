
from simulation import Simulation
from constants.field_constants import ACCELERATED_STEPS
import pygame
import sys
from decision_making.decision import ConstantVsDecision, ConstantWsDecision, ShapePathDecision
from utils import build_shape_from_center
import numpy as np

ACCELERATED = True
# ACCELERATED = False

DRAW_PATH = True

GET_HISTORY = True

if ACCELERATED:
    steps = ACCELERATED_STEPS
else:
    steps = 1

# decision = ConstantWsDecision(np.array([[10,-10,-10,10]]).T)
# decision = ConstantVsDecision(np.array([[0.5, 0.5, 2]]).T)
decision = ShapePathDecision(build_shape_from_center([[-1,1], [-1,-1], [1,-1], [1,1]]), 2, 15)
simulation = Simulation(decision, render=True)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            simulation.draw_ws_graphs()
            running = False

    simulation.run(steps, draw_path=DRAW_PATH, get_history=GET_HISTORY)

pygame.quit()
sys.exit()
