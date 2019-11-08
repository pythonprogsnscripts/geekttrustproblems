'''
Problem 1: Lengaburu traffic
King Shan wants to visit the suburb of Hallitharam, and has 2 possible orbits
and 3 possible vehicles to chose from.The coding challenge is to determine which orbit
and vehicle King Shan should take to reach Hallitharam the fastest
'''

import sys
import os
import argparse
sys.path.append(os.path.dirname(__file__)+"/../")
from src.validate_input_data import validate_input_data
from src.class_traffic import Traffic

PARSER = argparse.ArgumentParser(prog='traffic_problem_one',                \
                            description='Geek Trust traffic problem',       \
                            allow_abbrev=False)

PARSER.add_argument('Climate', metavar='--climate', action='store',         \
                    type=str, help='Climate condition')
PARSER.add_argument('Orbit1', metavar='--orbit1', action='store',           \
                    type=int, help='Orbit 1 traffic speed')
PARSER.add_argument('Orbit2', metavar='--orbit2', action='store',
                    type=int, help='Orbit 2 traffic speed')                 \

def results():
    '''
    This function returns data from the options specified using parse_args()
    The return value from parse_args() is a Namespace containing the arguments
    to the command. The object holds the argument values as attributes
    '''
    return PARSER.parse_args()

def getVars():
    '''
    The functions takes the results and processes. This function
    also check, whether valid climate condition has been given
    as input
    '''
    res = results()
    check_climate_input = validate_input_data(res.Climate)
    if check_climate_input:
        find_traffic = Traffic()
        find_traffic.set_climate(res.Climate)
        find_traffic.set_traffic_speed_orbit1(res.Orbit1)
        find_traffic.set_traffic_speed_orbit2(res.Orbit2)

def main():
    '''
    Pedestal function which starts the program
    '''
    getVars()

if __name__ == "__main__":
    main()
