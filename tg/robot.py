from abc import ABC, abstractmethod
from controllers import SSLController
import numpy as np

class Robot (ABC):
    def __init__(self, pos, r, l) -> None:
        self.r = r
        self.l = l
        self.pos = pos
        self.vx = 0
        self.vy = 0
        self.w = 0
    @abstractmethod
    def initialize_controller (self):
        pass

class SSLRobot(Robot):
    def __init__(self, r, l) -> None:
        super().__init__(r, l)
        self.ws = np.array([0,0,0,0]).T
    def initialize_controller(self):
        self.controller = SSLController(self.r, self.l)
    