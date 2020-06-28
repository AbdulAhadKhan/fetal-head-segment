import yaml
from parser import Parser

def _get_mode():
    pass

def _test_arguments():
    pass

def _get_configs():
    with open('./config.yaml', 'r') as file:
        return yaml.safe_load(file)

def _mode_sequence():
    pass

def execute():
    parser = Parser()
    args = parser.get_arguments()
    config = _get_configs()
    mode = _get_mode(args)
    _mode_sequence(mode, config)
