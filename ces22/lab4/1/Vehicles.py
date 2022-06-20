from abc import ABC, abstractclassmethod, abstractmethod


class Vehicle(ABC):
      def __init__(self, engine):
          self.speed = 0
          self.engine = engine

      def accelerate(self):
            self.speed += self.engine.accelerate(self.mass)
      def stop(self):
            self.speed = 0
      def get_status(self):
            print('Driving at {}'.format(self.speed))

      def print_engine(self):
            print('Engine is {}'.format(self.engine.type))

      @abstractmethod     
      def print_type():
            '''Prints the type of vehicle'''
            pass

class Truck(Vehicle):
      def __init__(self, engine):
          super().__init__(engine)
          self.mass = 5000
      def print_type():
          print('Truck')

class Car(Vehicle):
      def __init__(self, engine):
          super().__init__(engine)
          self.mass = 1000
      def print_type():
          print('Car')

class Motorcycle(Vehicle):
      def __init__(self, engine):
          super().__init__(engine)
          self.mass = 100
      def print_type():
          print('Motorcycle')


      