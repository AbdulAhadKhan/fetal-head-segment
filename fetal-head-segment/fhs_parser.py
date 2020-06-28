import argparse

class Parser:
    def __init__(self):
        self._arg_parser = argparse.ArgumentParser()

        self._arg_parser.add_argument('path', type=str, help='Path to video/image file')
        self._arg_parser.add_argument('-i', '--image', action='store_false',
                                      help='Specify this option if input is an image')
        self._arg_parser.add_argument('-o', '--output', type=str, default=None,
                                      help='If used the output will also be saved to ' +
                                      'specified directory')
        self._arg_parser.add_argument('-s', '--subdir', type=str, default=None,
                                      help='Used with -o, make subdir with specified ' +
                                      'output directory')

    def get_arguments(self):
        args = self._arg_parser.parse_args()
        return vars(args)
