import sys
import yaml

from fhs_parser import Parser
from utils import path_exists
from utils import make_dir
from utils import file_type

from image import Image
from video import Video

def _get_save_mode(args):
    return args['output'] is not None

def _test_arguments(args):
    if not path_exists(args['path']):
        print('Input path does not exist')
        return False
    if args['output'] is not None and not path_exists(args['output']):
        print('Output path does not exist')
        return False
    return True

def _get_configs():
    with open('./config.yaml', 'r') as file:
        return yaml.safe_load(file)

def _mode_sequence(args, save_mode, save_dir, config):
    if file_type(args['path']) == 'image':
        im_predictor = Image(args['path'],
                             config,
                             save_mode,
                             save_dir)
        im_predictor.show()
    elif file_type(args['path']) == 'video':
        vid_predictor = Video(args['path'],
                              config,
                              save_mode,
                              save_dir)
        vid_predictor.stream()

def execute():
    parser = Parser()
    args = parser.get_arguments()

    if not _test_arguments(args):
        sys.exit(1)

    config = _get_configs()
    save_mode = _get_save_mode(args)

    save_dir = args['output']
    if args['subdir'] is not None:
        save_dir = make_dir(args['output'], args['subdir'])

    _mode_sequence(args, save_mode, save_dir, config)
