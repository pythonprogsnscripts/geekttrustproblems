import sys, os
sys.path.append(os.path.dirname(__file__)+"/../")

class Vehicle():
    '''
    This class creates Vehicle object
    '''
    def __init__(self):
        pass
    
    def setVehicle(self, vehicle_type, max_speed, cross_cater, can_travel):
        '''
        Initializes the attributes of vehicle
        '''
        self.vehicle_type = vehicle_type
        self.max_speed = max_speed
        self.cross_cater = cross_cater
        self.can_travel = can_travel