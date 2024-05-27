from abc import ABC, abstractmethod
from constants.robot_constants import TOLERANCE
import math
import numpy as np
class Decision(ABC):
    @abstractmethod
    def get_decision_ws(self) -> callable:
        pass


class ConstantWsDecision(Decision):
    def __init__(self, w) -> None:
        super().__init__()
        self.w = w
    def constant_ws(self, **kwargs):
        return self.w
    def get_decision_ws(self):
        return self.constant_ws
    
class ConstantVsDecision(Decision):
    def __init__(self, v) -> None:
        self.v = v

    def get_ws(self, **kwargs):
        assert "robot" in kwargs, "robot must be an argument"
        return kwargs["robot"].get_possible_ws_for_v(self.v)
    
    def get_decision_ws(self):
        return self.get_ws
    
class ShapePathDecision(Decision):
    def __init__(self, shape, abs_v, w) -> None:
        self.shape = shape
        self.current = 0
        self.abs_v = abs_v
        self.w = w
        self.size = len(shape)
    def get_ws_for_path(self, **kwargs):
        assert "robot" in kwargs, "robot must be an argument"
        robot = kwargs["robot"]

        current_destination = self.shape[self.current]
        if math.dist(current_destination, robot.pos) < TOLERANCE:
            self.current = (self.current + 1) % self.size
            current_destination = self.shape[self.current]
        pos_vector = current_destination - robot.pos  
        vxy = self.abs_v * pos_vector/ np.linalg.norm(pos_vector)
        v = np.append(vxy, [[self.w]], axis=0)
        return robot.get_possible_ws_for_v(v)
    def get_decision_ws(self):
        return self.get_ws_for_path