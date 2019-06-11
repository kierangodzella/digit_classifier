# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:02:46 2019

@author: kiera
"""
#gradients.py

import numpy as np
from PIL import Image

class Gradients(object):
    def resize_square(image, size = [28,28]):
        image = Image.fromarray(image)
        image = np.array(image.resize(size))
        return image
    
    def grad_mag(image):
        # Return array with flat (x and y) gradient magnitudes for each pixel; same aspect ratio
        m,n = np.shape(image)
        image = np.ndarray.astype(image, dtype = 'float')
        std = np.std(image)
        
        #initialize arrays for magnitude calculation
        res_x = np.zeros([m,n])
        res_y = np.zeros([m,n])
        res = np.zeros([m,n])
        
        for i in range(1,m-1):
            for j in range(1,n-1):
                
                #simple before-after gradient masks applied for x, y 
                res_x[i,j] = (image[i,j-1] - image[i,j+1])
                res_y[i,j] = (image[i-1,j] - image[i+1,j])
                res[i,j] = np.sqrt(res_x[i,j]**2 + res_y[i,j]**2)
                
                #filter for minimum brightness change
                if (res[i,j] < 100): res[i,j] = 0
        
        return res