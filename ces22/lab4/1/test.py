from VehicleFactory import *

taycan = CarFactory.create_eletric_engine_vehicle()
print('Taycan:')
taycan.print_engine()
taycan.print_type()
taycan.get_status()
for i in range(5):
      taycan.accelerate()
taycan.get_status()

print('\n\nHarley:')
harley = MotorcycleFactory.create_combustion_engine_vehicle()
harley.print_engine()
harley.print_type()
harley.get_status()
for i in range(5):
      harley.accelerate()
harley.get_status()
