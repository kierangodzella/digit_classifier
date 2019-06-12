# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 00:09:51 2019

@author: kiera
"""

# CNN basis for digit_classifier
import numpy as np
import torchvision
import tensorflow
from keras import models, layers, optimizers
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.preprocessing.image import img_to_array, array_to_img
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split

class Network_builder(object):
    def __init__(self, squares, first_run):
        self.squares = squares
        self.first_run = first_run
        
    def cnn_model(self):    
        net = Sequential()
        
        net.add(Conv2D(10, kernel_size=(5,5), activation='relu', 
                           kernel_initializer='glorot_normal', padding='same',
                           input_shape=(28,28,1)))
        net.add(Conv2D(20, kernel_size=(3,3), activation='relu',
                           padding='same'))
        net.add(MaxPooling2D(pool_size=(2,2)))
        net.add(Dropout(0.2))
        
        net.add(Flatten())
        net.add(layers.Dense(units=320, activation='relu'))
        net.add(layers.Dense(units=10, activation='softmax'))
        
        net.compile(loss='categorical_crossentropy', optimizer='Adam',
                        metrics=['accuracy'])
        self.network = net
    
    def process_data(self):
        (x, y), (_,_) = tensorflow.keras.datasets.mnist.load_data()
        x, y = x.reshape(np.shape(x)[0],28,28,1), to_categorical(y)
        self.data = train_test_split(x, y, test_size = 0.1)
    
    def fit_model(self):
        x_train, x_val, y_train, y_val = self.data
        fit_network = self.network.fit(x_train, y_train, batch_size=500, 
                      epochs=10, verbose=0, validation_data=(x_val, y_val))
        self.fitted = fit_network
    def predict(self):
        if self.first_run==True:
            network = self.fitted
            self.predictions = network.predict(self.squares)
        else: self.predictions = network.predict(self.squares)
    def output(self):
        self.output = self.predictions
            
    
        