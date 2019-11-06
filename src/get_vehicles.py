'''
SRP Separation
'''
import sys
import os
sys.path.append(os.path.dirname(__file__)+"/../")
from src.read_files import VEHICLE_DATA
from src import constants

def getvehicles(climate):
    '''
       :param climate: type of climate
       :return: Based on climate, return available vehicles
    '''

    bike = VEHICLE_DATA['bike']
    tuktuk = VEHICLE_DATA['tuktuk']
    car = VEHICLE_DATA['car']

    if climate == "Sunny":
        vehicle = [[bike, tuktuk, car], constants.CRATER_CHANGE_WHEN_SUNNY]
    elif climate == "Rainy":
        vehicle = [[car, tuktuk], constants.CRATER_CHANGE_WHEN_RAINY]
    else:
        vehicle = [[car, bike], constants.CRATER_CHANGE_WHEN_WINDY]
    #
    return vehicle
