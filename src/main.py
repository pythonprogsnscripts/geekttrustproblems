'''
Main program for geek trust traffic problem
to accept input as arguments
'''
import argparse

PARSER = argparse.ArgumentParser(prog='traffic_problem_one', \
                                usage= \
                                    '%(prog)s [options] climate \
                                    orbit1_traffic_speed orbit2_traffic_speed', \
                                description='Geek Trust traffic problem', \
                                allow_abbrev=False)

def parse_arguments(positional_arg, metavar, action, data_type, help_message):
    '''
        :param arg: Weather condition
        :param metavar: variable
        :param action: store the data
        :param type: data type
        :param help_message: help_message
    '''
    PARSER.add_argument(positional_arg, metavar=metavar, action=action, \
                        type=data_type, help=help_message)

parse_arguments('Climate', '--climate', 'store', str, 'Current climate condition')
parse_arguments('Orbit1', '--orbit1', 'store', int, 'Orbit 1 traffic speed')
parse_arguments('Orbit2', '--orbit2', 'store', int, 'Orbit 2 traffic speed')

PARSER.add_argument("--verbose", help="increase output verbosity", \
                    action="store_true")
ARGS = PARSER.parse_args()

CLIMATE = [ARGS.Climate, ARGS.Orbit1, ARGS.Orbit2]
