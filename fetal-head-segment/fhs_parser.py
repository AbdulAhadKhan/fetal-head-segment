import argparse

class Parser:
    def __init__(self):
        self._args = argparse.ArgumentParser()

    def initialize_arguments(self):
        self._args.add_argument('path', type=str, help='Path to video/image file')
        self._args.add_argument('-i', '--image', action='store_false',
                                help='Specify this option if input is an image')
        self._args.add_argument('-o', '--output', type=str, default=None,
                                help='If used the output will also be saved to specified directory')
        self._args.add_argument('-s', '--subdir', type=str, default=None,
                                help='Used with -o, make subdir with specified output directory')

    def get_arguments(self):
        return dict(self._args)
