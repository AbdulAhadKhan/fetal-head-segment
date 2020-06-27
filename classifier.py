import pickle

from keras.models import load_model

class Classifier:
    def __init__(self, model_path, class_dict_path):
        self.model = load_model(model_path)
        self.class_dict_path = self._load_class_dict(class_dict_path)

    @staticmethod
    def _load_class_dict(class_dict_path):
        with open(class_dict_path, 'rb') as file:
            return pickle.load(file)

    def get_probabilites(self):
        pass

    def get_class(self):
        pass

    def prob_to_class(self):
        pass

    def translate(self):
        pass
