import sys
import yaml

from fhs_parser import Parser
from utils import path_exists

from image import Image

def _get_save_mode(args):
    return args['o'] is not None

def _test_arguments(args):
    if not path_exists(args['path']):
        print('Input path does not exist')
        return False
    if args['o'] is not None and path_exists(args['o']):
        print('Output path does not exist')
        return False
    return True

def _get_configs():
    with open('./config.yaml', 'r') as file:
        return yaml.safe_load(file)

def _mode_sequence(args, save_mode, config):
    if args['i']:
        im_predictor = Image(args['path'],
                             config)

def execute():
    parser = Parser()
    args = parser.get_arguments()

    if not _test_arguments(args):
        sys.exit(1)

    config = _get_configs()
    save_mode = _get_save_mode(args)
    _mode_sequence(args, save_mode, config)
