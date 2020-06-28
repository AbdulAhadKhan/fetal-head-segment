import pickle
import numpy as np

from keras.models import load_model
from keras.initializers import glorot_normal

class Classifier:
    def __init__(self, model_path, class_dict_path, thresh=0.85):
        self.model = load_model(model_path, custom_objects={'GlorotUniform'})
        self.class_dict = self._load_class_dict(class_dict_path)
        self.thresh = thresh

    @staticmethod
    def _load_class_dict(class_dict_path):
        with open(class_dict_path, 'rb') as file:
            return pickle.load(file)

    def get_class(self, image):
        probs = self.get_probabilites(image)
        return self.prob_to_class(probs)

    def get_probabilites(self, image):
        return self.model.predict(image)

    def prob_to_class(self, probs):
        index = np.argmax(probs)
        if probs[index] < self.thresh:
            return 'No Class'
        return self.class_dict[index]
