from abc import ABC, abstractmethod
import numpy as np

class Controller(ABC):
    def __init__(self, radius, length) -> None:
        self.r = radius
        self.l = length
    def transform_velocities(self, ws: np.array)-> np.array:
        return self.M @ ws
    @abstractmethod
    def build_transformation_matrix(self):
        pass


class SSLController(Controller):
    def __init__(self, radius, length) -> None:
        super().__init__(radius, length)
        self.M = self.build_transformation_matrix()
        # Pseudo Inverse
        self.M_pinv = np.linalg.pinv(self.M)

    def build_transformation_matrix(self):
        sqrt2 = np.sqrt(2)
        l4 = self.l * 4
        T = np.array([
            [ -sqrt2/4, -sqrt2/4, sqrt2/4, sqrt2/4],
            [ sqrt2/4, -sqrt2/4, -sqrt2/4, sqrt2/4],
            [ 1/l4, 1/l4, 1/l4, 1/l4]
        ]
        )
        return self.r * T
