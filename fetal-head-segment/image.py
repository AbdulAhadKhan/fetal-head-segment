import ntpath

import cv2
from utils import save_image
from utils import embed_class
from predict import Predictor
from __main__ import __file__

class Image:
    def __init__(self, image_path, predictor_settings,
                 save=False, save_dir=None):
        self.image = self._load_image(image_path)
        self.fname = ntpath.basename(image_path)
        self.save = save
        self.save_dir = save_dir
        self.predictor = Predictor(**predictor_settings)

    @staticmethod
    def _load_image(video_path):
        return cv2.imread(video_path)

    def show(self):
        image = self.predictor.process_image(self.image)
        dims = self._get_dims()
        if self.predictor.image_class == 'Head' and self.save:
            save_image(image, f'{self.save_dir}/{self.fname}.png')
        image = cv2.resize(image, (dims))
        image = embed_class(image, self.predictor.image_class)
        cv2.imshow(__file__, image)
        cv2.waitKey()

    def _get_dims(self):
        return self.image.shape[:2]
