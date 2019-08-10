'''
Main program for geek trust traffic problem
to accept input as arguments
'''
import argparse

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
    creating the parser
    '''
    PARSER = create_parser()
    ARGS = PARSER.parse_args()
    return [ARGS.Climate, ARGS.Orbit1, ARGS.Orbit2]

if __name__ == "__main__":
    main()
    