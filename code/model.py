import tensorflow as tf
from tensorflow.keras.layers import \
    Conv2D, MaxPool2D, Dropout, Flatten, Dense, BatchNormalization, Activation

import hyperparameters as hp

class Model(tf.keras.Model):
    """ Subclassing the model """

    def __init__(self):
        super(Model, self).__init__()

        self.optimizer = tf.keras.optimizers.Adam(learning_rate=hp.learning_rate)

        ###MAIN
        self.architecture = [
            # Block 1
            Conv2D(filters=128, kernel_size=3, padding="same", activation="relu"),
            Conv2D(filters=128, kernel_size=3, padding="same", activation="relu"),
            MaxPool2D(pool_size=2),
            BatchNormalization(),

            #Block 2
            Conv2D(filters=256, kernel_size=3, padding="same", activation="relu"),
            Conv2D(filters=256, kernel_size=3, padding="same", activation="relu"),
            MaxPool2D(pool_size=2),
            BatchNormalization(),

            #Block 3
            Conv2D(filters=512, kernel_size=3, padding="same", activation="relu"),
            Conv2D(filters=512, kernel_size=3, padding="same", activation="relu"),
            MaxPool2D(pool_size=2),
            BatchNormalization(),

            Dropout(0.2),

            #Block 4
            Conv2D(filters=1028, kernel_size=3, padding="same", activation="relu"),
            Conv2D(filters=1028, kernel_size=3, padding="same", activation="relu"),
            MaxPool2D(pool_size=2),
            BatchNormalization(),

            Dropout(0.2),
            Flatten(),
            Dense(units=128, activation="relu"),
            Dense(units=64, activation="relu"),

            Dense(units=32, activation="relu"),
            Dense(units=hp.num_classes, activation="softmax")
        ]


    def call(self, x):
        """ Forward pass. """

        for layer in self.architecture:
            x = layer(x)
        return x

    @staticmethod
    def loss_fn(labels, predictions):
        """ Loss function. """

        scce = tf.keras.losses.SparseCategoricalCrossentropy()
        return scce(labels, predictions)
