import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageOps
from keras.models import load_model
from segmentor.dice_coef_loss import dice_coef_loss

class Segmentor:
    def __init__(self, model_path, custom_objects=None):
        self.model = self.get_model(model_path, custom_objects)

    @staticmethod
    def get_model(model_path, custom_objects=None):
        if custom_objects is None:
            custom_objects = {'dice_coef_loss': dice_coef_loss}
        return load_model(model_path, custom_objects=custom_objects)

    @staticmethod
    def drawContour(m, s, c, RGB):
        thisContour = s.point(lambda p: p == c and 255)
        thisEdges = thisContour.filter(ImageFilter.FIND_EDGES)
        thisEdgesN = np.array(thisEdges)
        m[np.nonzero(thisEdgesN)] = RGB
        return m

    def embed_mask(self, image, mask):
        mask = Image.fromarray(np.uint8(mask*255)).convert('L')
        mask = ImageOps.invert(mask)
        image = cv2.cvtColor(image[0], cv2.COLOR_GRAY2BGR)
        masked = self.drawContour(image, mask, 0, (0, 255, 255))
        return masked

    def segment_image(self, image):
        mask = self.get_mask(image)
        return self.embed_mask(image, mask)

    def get_mask(self, image):
        return self.model.predict(image)[0][:, :, 0]
