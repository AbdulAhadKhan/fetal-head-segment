from classifier import Classifier
from segmentor.segmentor import Segmentor
from utils import prepare_for_prediction

class Predict:
    def __init__(self,
                 segmentor_path,
                 segmentor_indims,
                 custom_object,
                 classifier_path,
                 classifier_indims,
                 class_dict_path):
        self.segmentor = Segmentor(segmentor_path, custom_object)
        self.segmentor_indims = segmentor_indims
        self.classifier = Classifier(classifier_path, class_dict_path)
        self.classifier_indims = classifier_indims

    def get_class(self, image):
        image = prepare_for_prediction(image, self.classifier_indims)
        return self.classifier.get_class(image)

    def get_segmentation(self, image):
        image = prepare_for_prediction(image, self.segmentor_indims)
        return self.segmentor.segment_image(image)

    def process_image(self, image):
        pred_class = self.get_class(image)
        if pred_class == 'Head':
            image = self.get_segmentation(image)
        return image
