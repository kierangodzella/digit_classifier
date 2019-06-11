# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:46:07 2019

@author: kiera
"""

#main.py

#custom imports
import find_squares_grid
import find_squares_anywhere

class RunDigitClassifier(object):
    def __init__(self, image, inverted, im_format, small, large, stride):
        self.image = image
        self.im_format = im_format # "grid" "normal"
        self.inverted = inverted # True/False
        self.smallest = small
        self.largest = large
        self.stride
    
    def run_squares(image):
        if (self.im_format == "grid"):
            digits = find_squares_grid.find(self.image)
        if (self.im_format == "normal"):
            digits = find_squares_anywhere.find(
                    self.image, self.smallest, self.largest, self.stride)
        else: raise ValueError("Invalid argument: \"format\" ")
        
        