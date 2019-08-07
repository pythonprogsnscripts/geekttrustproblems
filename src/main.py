import argparse

parser = argparse.ArgumentParser(prog='traffic_problem_one',
                                    usage='%(prog)s [options] climate orbit1_traffic_speed orbit2_traffic_speed',
                                    description='Geek Trust traffic problem',
                                    allow_abbrev=False)
def parse_arguments(positional_arg,metavar,action,type,help):
    parser.add_argument(positional_arg,metavar=metavar,action=action,type=type,help=help)

parse_arguments('Climate','--climate','store',str,'Current climate condition')
parse_arguments('Orbit1','--orbit1','store',int,'Orbit 1 traffic speed')
parse_arguments('Orbit2','--orbit2','store',int,'Orbit 2 traffic speed')

parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
climate = [args.Climate, args.Orbit1, args.Orbit2]