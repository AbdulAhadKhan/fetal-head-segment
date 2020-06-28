import cv2
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
    def mask_contour(mask):
        thresh = cv2.threshold(mask, 0.8, 1, cv2.THRESH_BINARY)[1]
        thresh = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        thresh = thresh[0] if len(thresh) == 2 else thresh[1]
        return thresh

    @staticmethod
    def embed_mask(image, mask):
        for c in mask:
            cv2.drawContours(image, [c], -1, (255, 0, 0), thickness=1)
        return image

    def segment_image(self, image):
        mask = self.get_mask(image)
        return self.embed_mask(image, mask)

    def get_mask(self, image):
        mask = self.model.predict(image)[0][:, :, 0]
        return self.mask_contour(mask)
