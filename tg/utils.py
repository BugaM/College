import numpy as np
from constants.field_constants import  CENTER_X, CENTER_Y

def build_shape_from_center(list):
    converted = []
    for item in list:
        converted.append(np.array([(CENTER_X - item[0] , CENTER_Y - item[1])]).T)
    return converted


def constrain_angle(angle):
    return (angle + np.pi) % (2 * np.pi) - np.pi