from abc import ABC, abstractmethod
from components.controllers import SSLController
from decision_making.decision import Decision
from constants.robot_constants import MAX_WHEEL_SPEED
from constants.simulation_constants import DELTA_T
from constants.field_constants import WIDTH, HEIGHT
from utils import constrain_angle
import numpy as np

class Robot (ABC):
    def __init__(self, decision, pos, r, w_r, w_l) -> None:
        assert isinstance(decision, Decision), "decision must Inherit from Decision"
        self.decision = decision
        self.r = r
        self.w_r = w_r
        self.w_l = w_l
        self.original_pos = pos
        self.pos = pos
        self.psi = 0
        self.v = np.array([[0,0,0]]).T
    def reset_pos(self, random=False):
        if random:
            x = np.random.uniform(WIDTH/8, 7*WIDTH/8)
            y = np.random.uniform(HEIGHT/8, 7*HEIGHT/8)
            self.psi = np.random.uniform(-np.pi, np.pi)
            self.pos = np.array([[x,y]]).T
        else:
            self.pos = self.original_pos
            self.psi = 0
        self.v = np.array([[0,0,0]]).T
    def move(self):
        self.pos = self.pos + self.v[:2] * DELTA_T
        self.psi = constrain_angle(self.psi + self.v[2] * DELTA_T).item()
    def update(self):
        decision_function = self.decision.get_decision_ws()
        self._set_wheel_speeds(decision_function(robot=self))
        self.move()
    
    @abstractmethod
    def _initialize_controller (self):
        pass
    @abstractmethod
    def _convert_speeds (self):
        pass
    @abstractmethod
    def _set_wheel_speeds(self, ws):
        pass

    @property
    def theta(self):
        return np.arctan2(self.pos[1], self.pos[0])
    
    @property
    def R(self):
        return np.array([
        [np.cos(self.psi), -np.sin(self.psi), 0],
        [np.sin(self.psi), np.cos(self.psi), 0],
        [0, 0, 1]
    ])

    @property
    def R_inv(self):
        return np.linalg.inv(self.R)
    
    @property
    def front(self):
         return self.pos + self.r/2 * np.array([[np.cos(self.psi),np.sin(self.psi)]]).T

class SSLRobot(Robot):
    def __init__(self, decision, pos, r, w_r, w_l) -> None:
        super().__init__(decision, pos, r, w_r, w_l)
        self.ws = np.array([[0,0,0,0]]).T
        self._initialize_controller()
    def _initialize_controller(self):
        self.controller = SSLController(self.w_r, self.w_l)
    def _convert_speeds(self):
        # v = [vx,vy,w]
        ref_v = self.controller.transform_velocities(self.ws)
        # convert to global reference
        self.v = self.R @ ref_v
    def _set_wheel_speeds(self, ws):
        assert(ws.shape == (4,1))
        self.ws = np.clip(ws, -MAX_WHEEL_SPEED, MAX_WHEEL_SPEED)
        self._convert_speeds()
    def get_possible_ws_for_v(self, v):
        return self.controller.M_pinv @ self.R_inv @ v