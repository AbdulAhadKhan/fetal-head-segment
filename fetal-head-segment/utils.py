import cv2
import numpy as np

def prepare_for_prediction(image, dims):
    image = cv2.resize(image, dims, cv2.INTER_NEAREST)
    image = cv2.cvtColor(cv2, cv2.COLOR_BGR2GRAY)
    image = np.expand_dims(image, -1)
    image = np.expand_dims(image, 0)
    return image

def save_image():
    pass

def dir_exists():
    pass

def make_dir():
    pass

def path_exists():
    pass

def path_type():
    pass

def yes_no():
    pass
