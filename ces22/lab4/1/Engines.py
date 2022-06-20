from abc import ABC, abstractmethod

class AbstractEngine(ABC):
      
      def accelerate(self, mass):
           '''Increases the speed value in an amount based on mass'''
           return self.base_force/mass 

class CombustionEngine(AbstractEngine):
      def __init__(self):
          super().__init__()
          self.base_force = 10000
          self.type = 'Combustion'
          
class HybridEngine(AbstractEngine):
      def __init__(self):
          super().__init__()
          self.base_force = 8000
          self.type = 'Hybrid'

class EletricEngine(AbstractEngine):
      def __init__(self):
          super().__init__()
          self.base_force = 6000
          self.type = 'Eletric'