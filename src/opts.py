import argparse
import sys

def getOpts(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="curwthr - Display the current weather and temperature of a selected city.")

    parser.add_argument("-lj", "--ljubljana",       action="store_true", help="Ljubljana")
    parser.add_argument("-nm", "--novomesto",       action="store_true", help="Novomesto")
    parser.add_argument("-mb", "--maribor",         action="store_true", help="Maribor")
    parser.add_argument("-ms", "--murska-sobota",   action="store_true", help="Murska Sobota")
    parser.add_argument("-ng", "--nova-gorica",     action="store_true", help="Nova Gorica")
    parser.add_argument("-po", "--portoroz",        action="store_true", help="Portorož")
    
    parser.add_argument("-to", "--temp-only",       action="store_true", help="Show only the temperature(default in degrees Celsius)")
    parser.add_argument("-c",  "--celsius",         action="store_true", help="Show the temperature in degrees Celsius(default)")
    parser.add_argument("-k",  "--kelvin",          action="store_true", help="Show the temperature in Kelvin")
    
    parser.add_argument("-t",  "--time",            action="store_true", help="Show only the time")
    parser.add_argument("-w",  "--weather",         action="store_true", help="Show only the weather")

    options = parser.parse_args(args)

    cities = [
        options.ljubljana, 
        options.novomesto, 
        options.maribor, 
        options.murska_sobota,
        options.nova_gorica,
        options.portoroz
    ]

    if not (any(cities)):
        parser.error("No city chosen")
    elif sum(map(bool, cities)) > 1:
        parser.error("Only one city can be chosen")

    if (options.celsius and options.kelvin):
        parser.error("Only one unit of temperature can be chosen")

    if sum(map(bool, [options.temp_only, options.time, options.weather])) > 1:
        parser.error("Only one of the following flags can be chosen at once: -to, -t, -w")
    
    return options
