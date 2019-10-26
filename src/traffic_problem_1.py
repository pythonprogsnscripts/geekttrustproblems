'''
Problem 1: Lengaburu traffic
King Shan wants to visit the suburb of Hallitharam, and has 2 possible orbits
and 3 possible vehicles to chose from.The coding challenge is to determine which orbit
and vehicle King Shan should take to reach Hallitharam the fastest
'''
import sys
import os
import constants
sys.path.append(os.path.dirname(__file__)+"/../")
from src.read_files import VEHICLE_DATA
from src.main import create_parser

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

def get_orbit_time(vehicles, traffic_speed, orbit_distance, craters_count):
    '''
     :param vehicles: Based on Climate, gets the available vehicles
     :param traffic_speed: orbit traffic speed
     :param orbit_distance: orbit distance
     :param craters_count: Number of craters in particular orbit
     :return: [Vehicle Details,minimum Time takes to travel in Minutes, Craters change ]
     '''
    orbit_1_vehicles_time = []

    for i in vehicles[0]:
        if traffic_speed <= i['max_speed']:
            temp_speed = traffic_speed
        else:
            temp_speed = i['max_speed']
        temp = (orbit_distance + (vehicles[1] * craters_count)) \
                * i['cross_crater_time'] + (60 / temp_speed) * orbit_distance
        orbit_1_vehicles_time.append(temp)

    return [vehicles[0][orbit_1_vehicles_time.index(min(orbit_1_vehicles_time))], \
            min(orbit_1_vehicles_time)]

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

def main():
    '''
    This function will parse the arguments from the user
    '''
    PARSER = create_parser()
    ARGS = PARSER.parse_args()
    input_data = [ARGS.Climate, ARGS.Orbit1, ARGS.Orbit2]
    get_shortest_path(climate=input_data[0], traffic_speed_orbit1=input_data[1], \
                  traffic_speed_orbit2=input_data[2])
if __name__ == "__main__":
    main()
