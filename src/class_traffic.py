'''
This class contains the manin implemenation of the Lengaburu problem
This class is separated from the main program for SRP
'''
import sys
import os
sys.path.append(os.path.dirname(__file__)+"/../")
from src.find_shortest_path import Shortest

class Traffic:
    '''
    Creating private methods and private attributes
    Encapsulation
    '''
    def __init__(self, climate, traffic_speed_orbit1, traffic_speed_orbit2):
        self._climate = climate
        self.__traffic_speed_orbit1 = traffic_speed_orbit1
        self.__traffic_speed_orbit2 = traffic_speed_orbit2
        self.__shortest_path()

    def get_climate(self):
        '''
        Getter for climate attribute
        '''
        return self.__climate

    def get_set_traffic_speed_orbit1(self):
        '''
        Getter for traffic_speed_orbit1 attribute
        '''
        return self.__traffic_speed_orbit1

    def get_set_traffic_speed_orbit2(self):
        '''
        Getter for traffic_speed_orbit2 attribute
        '''
        return self.__traffic_speed_orbit2

    def set_climate(self, climate):
        '''
        Setter for climate attribute
        '''
        self.__climate = climate

    def set_traffic_speed_orbit1(self, traffic_speed_orbit1):
        '''
        Setter for traffic_speed_orbit1 attribute
        '''
        self.__traffic_speed_orbit1 = traffic_speed_orbit1

    def set_traffic_speed_orbit2(self, traffic_speed_orbit2):
        '''
        Setter for traffic_speed_orbit2 attribute
        '''
        self.__traffic_speed_orbit2 = traffic_speed_orbit2

    def __shortest_path(self):
        s = Shortest()
        s.get_shortest_path(self._climate, self.__traffic_speed_orbit1, self.__traffic_speed_orbit2)