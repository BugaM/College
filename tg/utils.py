import numpy as np
from constants.field_constants import  CENTER_X, CENTER_Y, ROBOT_MAX_WIDTH_FIELD, ROBOT_MIN_WIDTH_FIELD, ROBOT_MAX_HEIGHT_FIELD, ROBOT_MIN_HEIGHT_FIELD, PLAYER_STARTING_DISTANCE_TOLERANCE
from constants.robot_constants import MAX_VELOCITY

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
            width = np.random.uniform(ROBOT_MIN_WIDTH_FIELD,ROBOT_MAX_WIDTH_FIELD)
            height = np.random.uniform(ROBOT_MIN_HEIGHT_FIELD, ROBOT_MAX_HEIGHT_FIELD)
            new_pos = np.array([[width, height]]).T
            if all(np.linalg.norm(new_pos - pos) >= PLAYER_STARTING_DISTANCE_TOLERANCE for pos in positions):
                positions.append(new_pos)
                new_positions.append(new_pos)
                break

    return np.array(new_positions)

def generate_random_speeds(num_speeds):
    speeds = []
    for _ in range(num_speeds):
        abs_speed = np.random.normal(MAX_VELOCITY/2, MAX_VELOCITY/6)
        angle = np.random.uniform(-np.pi, np.pi)
        speed = abs_speed * np.array([[np.cos(angle), np.sin(angle)]]).T

        speeds.append(speed)
    return np.array(speeds)    
