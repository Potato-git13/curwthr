import argparse
import sys

def getOpts(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="curwthr")

    parser.add_argument("-lj", "--ljubljana", action="store_true", help="Ljubljana")
    parser.add_argument("-nm", "--novomesto", action="store_true", help="Novomesto")
    parser.add_argument("-to", "--temp-only", action="store_true", help="Show only the temperature(default in degrees Celsius)")
    parser.add_argument("-c",  "--celsius",   action="store_true", help="Show the temperature in degrees Celsius(default)")
    parser.add_argument("-k",  "--kelvin",    action="store_true", help="Show the temperature in Kelvin")
    parser.add_argument("-t",  "--time",      action="store_true", help="Show only the time")
    parser.add_argument("-w",  "--weather",   action="store_true", help="Show only the weather")

    options = parser.parse_args(args)

    if not (options.ljubljana or options.novomesto):
        parser.error("No city chosen")
    elif (options.ljubljana and options.novomesto):
        parser.error("Only one city can be chosen")

    if (options.celsius and options.kelvin):
        parser.error("Only one unit of temperature can be chosen")

    if sum(map(bool, [options.temp_only, options.time, options.weather])) > 1:
        parser.error("Only one of the following flags can be chosen at once: -to, -t, -w")
    
    return options
