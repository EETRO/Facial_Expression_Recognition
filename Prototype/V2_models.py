"""
Prototype V2
Different Keras Models
By: Xiaochi (George) Li
Nov.2018
"""

import tensorflow as tf
from tensorflow.keras import layers

def first_model():
    model = tf.keras.Sequential([
        layers.Conv2D(64, kernel_size=3, activation='relu', input_shape=(100,100,3)),
        layers.Conv2D(32, kernel_size=3, activation='relu'),
        layers.Flatten(),
        layers.Dense(7, activation='softmax')
    ])

    model.compile(optimizer=tf.train.AdadeltaOptimizer(0.001),
                  loss='categorical_crossentropy',
                 metrics=[tf.keras.metrics.categorical_accuracy])

    return model

# models 2

# model 3
