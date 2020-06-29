from classifier import Classifier
from segmentor.segmentor import Segmentor
from utils import prepare_for_prediction

class Predictor:
    def __init__(self,
                 segmentor_path,
                 segmentor_indims,
                 classifier_path,
                 classifier_indims,
                 class_dict_path):
        self.segmentor = Segmentor(segmentor_path)
        self.segmentor_indims = tuple(segmentor_indims)
        self.classifier = Classifier(classifier_path, class_dict_path)
        self.classifier_indims = tuple(classifier_indims)
        self.image_class = ''

    def get_class(self, image):
        image = prepare_for_prediction(image, self.classifier_indims)
        self.image_class = self.classifier.get_class(image)

    def get_segmentation(self, image):
        image = prepare_for_prediction(image, self.segmentor_indims)
        return self.segmentor.segment_image(image)

    def process_image(self, image):
        self.get_class(image)
        if self.image_class == 'Head':
            image = self.get_segmentation(image)
        return image
