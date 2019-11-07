'''
Separating code for SRP
'''
import sys
import os
sys.path.append(os.path.dirname(__file__)+"/../")
from src import constants
from src.get_vehicles import getvehicles
from src.find_orbit_time import get_orbit_time

# class Shortest(object):
#   def __init__(self, climate, traffic_speed_orbit1, traffic_speed_orbit2):
#     self._climate = climate
#     self._traffic_speed_orbit1 = traffic_speed_orbit1
#     self._traffic_speed_orbit2 = traffic_speed_orbit2

#   def get_climate(self):
#     return self._climate

#   def get_traffic_speed_orbit1(self):
#     return self._traffic_speed_orbit1

#   def traffic_speed_orbit2(self):
#     return self._traffic_speed_orbit2

#   def set_climate(self, )
def get_shortest_path(climate, traffic_speed_orbit1, traffic_speed_orbit2):
    '''
      :param climate: User input  CLimate
      :param traffic_speed_orbit1: Orbit 1 Traffic Speed
      :param traffic_speed_orbit2: Orbit 2 Traffic Speed
      :return: Shortest time and Vehicle details
      '''
    print("Weather is", climate)
    print("Orbit1 traffic speed is {0} megamiles/hour".format(traffic_speed_orbit1))
    print("Orbit1 traffic speed is {0} megamiles/hour".format(traffic_speed_orbit2))
    vehicles = getvehicles(climate)
    orbit1 = get_orbit_time(vehicles=vehicles, traffic_speed=traffic_speed_orbit1, \
                            orbit_distance=constants.ORBIT1_ORBIT_DISTANCE,
                            craters_count=constants.ORBIT1_CRATERS_COUNT)
    orbit2 = get_orbit_time(vehicles=vehicles, traffic_speed=traffic_speed_orbit2, \
                            orbit_distance=constants.ORBIT2_ORBIT_DISTANCE,
                            craters_count=constants.ORBIT2_CRATERS_COUNT)
    if orbit1[1] < orbit2[1]:
        print("Vehicle {0} on Orbit1".format(orbit1[0]['name']))
    else:
        print("Vehicle {0} on Orbit2".format(orbit2[0]['name']))
        