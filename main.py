# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:46:07 2019

@author: kiera
"""

#main.py
import numpy as np
import pandas as pd

#custom imports
import find_squares_grid
import find_squares_anywhere
import gradients

class RunDigitClassifier(object):
    def __init__(self, first_run, image, inverted, im_format, small=20, large=30, stride=2):
        self.first_run = first_run # bool
        self.image = image
        self.im_format = im_format # "grid" "normal"
        self.inverted = inverted # bool
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
    def classify():
        

if __name__=='__main__':
    params = {30, 50, 2}
    RunDigitClassifier(image=image, first_run=True, inverted=True, im_format='normal', **params)
        