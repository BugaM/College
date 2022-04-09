import abc


class Vehicle:
    __metaclass__ = abc.ABCMeta

    parts = ['engine']

    # Abstract Method
    @classmethod
    @abc.abstractmethod
    def get_parts(cls):
        return cls.parts

    # Static method
    @staticmethod
    def start_engine():
        return 'Vrummmm'


class Car(Vehicle):
    def get_parts(self):
        return ['wheels'] + super(Car, self).get_parts()


class Airplane(Vehicle):
    def __init__(self, pilot):
        self.pilot = pilot


    # Class method
    @classmethod
    def specification(cls):
        return 'Boeing 757'

    def my_pilot(self):
        return 'Pilot is {0}'.format(self.pilot)


car = Car()
airplane = Airplane('John')

# abstractmethod use
print(car.get_parts())

# static method use
print(Vehicle.start_engine())

# class method use
print(Airplane.specification())

# instance method use
print(airplane.my_pilot())
