
from simulation import Simulation
from constants.field_constants import ACCELERATED_STEPS, RIGHT_MARGIN, CENTER_X, BOTTOM_MARGIN, CENTER_Y, LEFT_MARGIN
import pygame
import sys
from decision_making.decision import ConstantVsDecision, ConstantWsDecision, ShapePathDecision
import math
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

decision = ConstantWsDecision(np.array([[0,0,0,0]]).T)
# decision = ConstantVsDecision(np.array([[0.5, 0.5, 2]]).T)
simulation = Simulation(decision, render=True, num_opps=0)
simulation.run(steps, draw_path=DRAW_PATH, get_history=GET_HISTORY)
lidar_read = simulation.lidar(4)
assert lidar_read[0] == RIGHT_MARGIN - CENTER_X
assert lidar_read[1] == BOTTOM_MARGIN - CENTER_Y
assert lidar_read[2] == CENTER_X - LEFT_MARGIN

lidar_read = simulation.lidar(8)
assert lidar_read[0] == RIGHT_MARGIN - CENTER_X
assert lidar_read[2] == BOTTOM_MARGIN - CENTER_Y
assert lidar_read[4] == CENTER_X - LEFT_MARGIN
assert math.isclose(lidar_read[1], lidar_read[3])
assert math.isclose(lidar_read[5], lidar_read[7])

pygame.quit()
sys.exit()
