from abc import ABC, abstractmethod
from cake import Cake

class AbstractCakeFactory(ABC):
      def __init__(self) -> None:
          super().__init__()
      
      @abstractmethod
      def createChocolateCake(self):
            '''Creates chocolate cake of a factory.'''
      @abstractmethod
      def createCarrotCake(self):
            '''Creates carrot cake of a factory.'''
      @abstractmethod
      def createManiocCake(self):
            '''Creates chocolate cake of a factory.'''

class BirthdayCakeFactory(AbstractCakeFactory):
      def __init__(self, flavor) -> None:
          super().__init__()
          self.flavor = flavor
          self.style = 'birthday'
      def createChocolateCake(self):
          return Cake(self.style, 'chocolate')
      def createCarrotCake(self):
          return Cake(self.style, 'carrot')
      def createManiocCake(self):
          return Cake(self.style, 'manioc')