'''
Problem 1: Lengaburu traffic
King Shan wants to visit the suburb of Hallitharam, and has 2 possible orbits
and 3 possible vehicles to chose from.The coding challenge is to determine which orbit
and vehicle King Shan should take to reach Hallitharam the fastest
'''

import sys
import os
import argparse
import collections
sys.path.append(os.path.dirname(__file__)+"/../")
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

def immutable_input_from_parser():
    '''
    Creating am immutable datastructure or functional datastructure
    This is the fundamental for functional programming
    '''
    res = results()
    Lengaburu = collections.namedtuple('Lengaburu', [
        'climate',
        'first_orbit_speed',
        'second_orbit_speed'
    ])

    find_orbit_parameters = (Lengaburu(climate=res.Climate, first_orbit_speed=res.Orbit1    \
                                       , second_orbit_speed=res.Orbit2))

    check_climate_input = tuple(filter(lambda x: x in ['Sunny', 'Windy', 'Rainy'],          \
                                find_orbit_parameters))
    if len(check_climate_input) == 0:
        print('Invalid Climate input')
        sys.exit()
    else:
        return find_orbit_parameters

def getVars():
    '''
    The functions takes the results and processes. This function
    also check, whether valid climate condition has been given
    as input
    '''
    res = immutable_input_from_parser()
    find_traffic = Traffic(res.climate, res.first_orbit_speed, res.second_orbit_speed)

def main():
    '''
    Pedestal function which starts the program
    '''
    getVars()

if __name__ == "__main__":
    main()
