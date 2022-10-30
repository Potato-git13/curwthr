import argparse
import sys

def getOpts(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="curwthr")

    parser.add_argument("-lj", "--ljubljana", action="store_true", help="Ljubljana")
    parser.add_argument("-nm", "--novomesto", action="store_true", help="Novomesto")
    parser.add_argument("-c",  "--celsius",   action="store_true", help="Show the temperature")
    parser.add_argument("-t",  "--time",      action="store_true", help="Show the time")

    options = parser.parse_args(args)

    if not (options.ljubljana or options.novomesto):
        parser.error("No city chosen")
    elif (options.ljubljana and options.novomesto):
        parser.error("Too many arguments given")
    
    return options
