import joblib
import numpy as np

class Prediction():

    def __init__(self):
        self.elements = ['Fe', 'Mg', 'Zn', 'Cu', 'Ca', 'Na', 'Ni', 'P', 'Li']
        self.models = {
            'lr': joblib.load('chimiometric/static/models/ml_models_array.pkl'),
            'pls': joblib.load('chimiometric/static/models/pls_models_array.pkl'),
            'smio': joblib.load('chimiometric/static/models/smio_models_array.pkl'),
            'elastic': joblib.load('chimiometric/static/models/elastic_models_array.pkl'),
        }

    def predict(self, data):
        result_dict = {}
        for model_name, models in self.models.items():
            result_dict[model_name] = {}
            for element, model in zip(self.elements, models):
                prediction = model.predict(data)[0]  # Get the first element of the prediction array
                if isinstance(prediction, np.ndarray):  # Check if prediction is an array
                    prediction = prediction[0]  # If it is an array, get the first element
                result_dict[model_name][element] = prediction
        return result_dict
