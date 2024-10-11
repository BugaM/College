import numpy as np
from constants.field_constants import  CENTER_X, CENTER_Y, ROBOT_MAX_WIDTH, ROBOT_MIN_WIDTH, ROBOT_MAX_HEIGHT, ROBOT_MIN_HIGHT, PLAYER_STARTING_DISTANCE_TOLERANCE

def build_shape_from_center(list):
    converted = []
    for item in list:
        converted.append(np.array([(CENTER_X - item[0] , CENTER_Y - item[1])]).T)
    return converted


def constrain_angle(angle):
    return (angle + np.pi) % (2 * np.pi) - np.pi


def generate_random_positions(current_positions: list, num_positions):
    positions = current_positions.copy()
    new_positions = []

    for _ in range(num_positions):
        while True:
            width = np.random.uniform(ROBOT_MIN_WIDTH,ROBOT_MAX_WIDTH)
            height = np.random.uniform(ROBOT_MIN_HIGHT, ROBOT_MAX_HEIGHT)
            new_pos = np.array([[width, height]]).T
            if all(np.linalg.norm(new_pos - pos) >= PLAYER_STARTING_DISTANCE_TOLERANCE for pos in positions):
                positions.append(new_pos)
                new_positions.append(new_pos)
                break

    return new_positions