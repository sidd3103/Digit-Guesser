from keras.models import load_model
import numpy as np
from keras.preprocessing import image


class Predictions:
    def __init__(self):
        self.model = load_model('model.h5')

    def evaluate(self, path):
        img = image.load_img(path, target_size=(28, 28), color_mode='grayscale')
        img = image.img_to_array(img)
        img = img.astype('float32') / 255
        img = np.expand_dims(img, axis=0)
        p = self.model.predict(img)
        return np.argmax(p)

