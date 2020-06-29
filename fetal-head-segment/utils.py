import os

import cv2
import numpy as np

def prepare_for_prediction(image, dims):
    image = cv2.resize(image, dims, cv2.INTER_NEAREST)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = np.expand_dims(image, -1)
    image = np.expand_dims(image, 0)
    return image

def save_image(image, path):
    cv2.imwrite(path, image)

def path_exists(path):
    return os.path.exists(path)

def make_dir(path, dir_name):
    path = os.path.join(path, dir_name)
    if not path_exists(path):
        os.mkdir(path)
    return path

def path_type(path):
    if os.path.isdir(path):
        return 'dir'
    if os.path.isfile(path):
        return path.split('.')[-1]
    raise Exception(f'Could not process \'{path}\'. Check if path exists')

def yes_no(question):
    print(question)
    res = input('[yes/no]')
    if not isinstance(res, str):
        raise Exception('Invalid input type')
    res = res.lower()[0]
    return True if res == 'y' else False if res == 'n' else yes_no(question)

def embed_class(frame, text):
    image = cv2.putText(frame, text,
                        (50, 50), cv2.FONT_HERSHEY_COMPLEX,
                        1, (0, 0, 255), 1, cv2.LINE_AA)
    return image
