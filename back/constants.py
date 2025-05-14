from configparser import ConfigParser
import os

# location of the ini file
fic_config = 'config/config.ini'

# default values, can be overwritten by values from config/config.ini
INI_GRID_WIDTH = 12
INI_GRID_HEIGHT = 10
INI_FISH_STARTING_POPULATION = 10
INI_FISH_TIME_TO_REPRODUCE = 9
INI_SHARK_STARTING_POPULATION = 7
INI_SHARK_STARTING_ENERGY = 10
INI_SHARK_TIME_TO_REPRODUCE = 5
INI_SHARK_EATING_REGEN = 3
INI_ROCK_STARTING_POPULATION = 3
INI_AUTO_PLAY = False



def read_config(fic) -> ConfigParser|bool:
    """ Function that reads the config.ini file and returns a parser

    Args:
        fic (str): path to the ini file

    Returns:
        ConfigParser|bool: parser containing the ini file "constants" | False (file not found)
    """
    if not os.path.exists(fic):
        print(f'Ini file {fic_config} does not exist')
        return False

    parser = ConfigParser() 
    parser.read(fic)

    return parser

# Getting a parser of the ini file
ini_parser = read_config( fic_config)

# if the ini file is found we overwrite the "default" constants defined on top with the ones from the file 
if ini_parser:
    INI_GRID_WIDTH = int(ini_parser.get('grid','width'))
    INI_GRID_HEIGHT = int(ini_parser.get('grid','height'))

    INI_FISH_STARTING_POPULATION = int(ini_parser.get('fish','starting_population'))
    INI_FISH_TIME_TO_REPRODUCE = int(ini_parser.get('fish','time_to_reproduce'))

    INI_SHARK_STARTING_POPULATION = int(ini_parser.get('shark','starting_population'))
    INI_SHARK_STARTING_ENERGY = int(ini_parser.get('shark','starting_energy'))
    INI_SHARK_TIME_TO_REPRODUCE = int(ini_parser.get('shark','time_to_reproduce'))
    INI_SHARK_EATING_REGEN = int(ini_parser.get('shark','eating_regen'))

    INI_ROCK_STARTING_POPULATION = int(ini_parser.get('rock','starting_population'))

    INI_AUTO_PLAY = bool(ini_parser.get('game','auto_play'))
