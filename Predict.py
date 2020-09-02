from keras.models import load_model
from keras.utils import to_categorical
import mnist

test_images = mnist.test_images()
test_labels = mnist.test_labels()
test_images = test_images.reshape((10000, 28, 28, 1))
test_images = test_images.astype('float32') / 255
test_labels = to_categorical(test_labels)

model = load_model('model.h5')
loss, acc = model.evaluate(test_images, test_labels)
print(acc * 100)
