import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def load_model_with_custom_loss(self):
        # Load model without compiling it to avoid reduction issues
        model = load_model(os.path.join("model", "model.h5"), compile=False)
        return model

    def predict(self):
        # Load the model
        model = self.load_model_with_custom_loss()

        # Load and preprocess the image
        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        # Make a prediction
        result = np.argmax(model.predict(test_image), axis=1)

        # Determine prediction result
        if result[0] == 1:
            prediction = 'Tumor'
            return [{ "image" : prediction}]
        else:
            prediction = 'Normal'
            return [{ "image" : prediction}]