from abc import ABC, abstractclassmethod
from Vehicles import *
from Engines import *

class AbstractVehicleFactory(ABC):
      @abstractclassmethod
      def create_eletric_engine_vehicle():
            '''Creates a vehicle with eletric engine'''
            pass
      @abstractclassmethod
      def create_combustion_engine_vehicle():
            '''Creates a vehicle with combustion engine'''
            pass
      @abstractclassmethod
      def create_hybrid_engine_vehicle():
            '''Creates a vehicle with combustion engine'''
            pass

class CarFactory(AbstractVehicleFactory):
      def create_eletric_engine_vehicle():
            return Car(EletricEngine())
      def create_combustion_engine_vehicle():
           return Car(CombustionEngine)
      def create_hybrid_engine_vehicle():
            return Car(HybridEngine)

class TruckFactory(AbstractVehicleFactory):
      def create_eletric_engine_vehicle():
            return Truck(EletricEngine())
      def create_combustion_engine_vehicle():
           return Truck(CombustionEngine)
      def create_hybrid_engine_vehicle():
            return Truck(HybridEngine)

class MotorcycleFactory(AbstractVehicleFactory):
      def create_eletric_engine_vehicle():
            return Motorcycle(EletricEngine())
      def create_combustion_engine_vehicle():
           return Motorcycle(CombustionEngine)
      def create_hybrid_engine_vehicle():
            return Motorcycle(HybridEngine)