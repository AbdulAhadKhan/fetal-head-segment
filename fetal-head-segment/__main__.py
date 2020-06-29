import os
from command import execute

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '6'

if __name__ == '__main__':
    execute()
