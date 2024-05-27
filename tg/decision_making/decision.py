from abc import ABC, abstractmethod
class Decision(ABC):
    @abstractmethod
    def get_decision(self):
        pass


class ConstantDecision(Decision):
    def __init__(self, v) -> None:
        super().__init__()
        self.v = v
    def get_decision(self):
        return self.v
    
class InputedDecision(Decision):
    def __init__(self, v) -> None:
        self.v = v
    def set_v(self,v):
        self.v = v
    def get_decision(self):
        return self.v