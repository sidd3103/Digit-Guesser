import mnist
from keras import layers
from keras import models
from keras.utils import to_categorical

train_images = mnist.train_images()
train_labels = mnist.train_labels()
train_images = train_images.reshape((60000, 28, 28, 1))
train_images = train_images.astype('float32') / 255
train_labels = to_categorical(train_labels)


class Model:
    def __init__(self):
        """
        Define the convolutional model
        """

        self.c = False
        self.t = False
        # Define the convolutional base
        self.model = models.Sequential()
        self.model.add(layers.Conv2D(16, (3, 3), activation='relu', input_shape=(28, 28, 1)))
        self.model.add(layers.MaxPooling2D(2, 2))
        self.model.add(layers.Conv2D(32, (3, 3), activation='relu'))
        self.model.add(layers.MaxPooling2D(2, 2))
        self.model.add(layers.Conv2D(64, (3, 3), activation='relu'))

        # Define the densely connected classifier
        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(64, activation='relu'))
        self.model.add(layers.Dense(10, activation='softmax'))

    def compile(self):
        """
        Compile the model
        :return: None
        """
        self.model.compile(optimizer='rmsprop',
                           loss='categorical_crossentropy',
                           metrics=['acc'])
        self.c = True

    def fit(self):
        """
        Fit the model on the mnist digit dataset
        :return: None
        """
        if self.c:
            self.model.fit(train_images, train_labels, epochs=5, batch_size=64)
            self.t = True
        else:
            print('Compile the model first')

    def save(self):
        self.model.save('model.h5')


model = Model()
model.compile()
model.fit()
model.save()
