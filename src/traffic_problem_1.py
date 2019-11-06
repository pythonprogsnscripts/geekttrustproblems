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
from src.find_shortest_path import get_shortest_path

def create_parser():
    '''
        :param arg: Weather condition
        :param metavar: variable
        :param action: store the data
        :param type: data type
        :param help_message: help_message
    '''
    PARSER = argparse.ArgumentParser(prog='traffic_problem_one',                \
                                description='Geek Trust traffic problem',       \
                                allow_abbrev=False)

    PARSER.add_argument('Climate', metavar='--climate', action='store',         \
                        type=str, help='Climate condition')
    PARSER.add_argument('Orbit1', metavar='--orbit1', action='store',           \
                        type=int, help='Orbit 1 traffic speed')
    PARSER.add_argument('Orbit2', metavar='--orbit2', action='store',
                        type=int, help='Orbit 2 traffic speed')                 \

    return PARSER

def main():
    '''
    This function will parse the arguments from the user
    Calls --> validate_input_data(climate)
    '''
    PARSER = create_parser()
    ARGS = PARSER.parse_args()
    input_data = [ARGS.Climate, ARGS.Orbit1, ARGS.Orbit2]
    check_climate_input = validate_input_data(ARGS.Climate)
    if check_climate_input:
        get_shortest_path(climate=input_data[0], traffic_speed_orbit1=input_data[1], \
                  traffic_speed_orbit2=input_data[2])

if __name__ == "__main__":
    main()
