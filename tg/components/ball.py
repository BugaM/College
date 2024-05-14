import numpy as np

class Ball:
    def __init__(self, pos) -> None:
        self.original_pos = pos
        self.pos = pos
        self.v = np.array([[0,0]]).T
    def reset_ball(self):
        self.pos = self.original_pos
        self.v = np.array([[0,0]]).T
    def move(self):
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]
    