from abc import ABC, abstractmethod
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