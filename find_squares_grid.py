# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:57:18 2019

@author: kiera
"""
#find_squares_grid.py
import numpy as np

#custom imports
import gradients

class Find_squares_grid(object):
    def scan_y(image, y, n):
        for i in range(n):
            if (image[y,i] > 0):
                return True
            else: return False
        
    def scan_x(image, x, m):
        for i in range(0,m):
            if(image[i,x] > 0):
                return True
            else: return False
            
    def find(image):
        gradient = gradients.grad_mag(image)
        m,n = np.shape(gradient)
        lines = []
        bounds_y = []
        squares = []
        res = []
        value_1 = False
        value_2 = False
        mode = (stats.mode(np.ravel(im))[0])
        
        for i in range(m):
            if (bool(scan_y(gradient, i, n)) ^ bool(value_1)):
                bounds_y.append(i)
            value_1 = scan_y(gradient,i,n)
        
        for i in range(0,len(bounds_y)-1,2):
                lines.append(image[bounds_y[i]:bounds_y[i+1],:])
                
        for line in lines:
            
            y,x = np.shape(line)
            line_grad = grad_mag(line)
            bounds_x = []
            
            for i in range(x):
                if (bool(scan_x(line_grad, i, y)) ^ bool(value_2)):
                    bounds_x.append(i)
                value_2 = scan_x(line_grad, i, y)
            
            for i in range(0,len(bounds_x)-1,2):
                square = line[:,bounds_x[i]:bounds_x[i+1]]
                y, x = np.shape(square)
                pad = np.int(abs(np.round((y-x)/2)))
                if (y>x):
                    bezel = np.full((y,pad),mode)
                    square = np.concatenate([square, bezel], axis=1)
                    square = np.concatenate([bezel, square], axis=1)
                if (x>y):
                    bezel = np.full((pad,x),mode)
                    square = np.concatenate([square, bezel], axis=0)
                    square = np.concatenate([bezel, square], axis=0)
            
                squares.append(Gradients.resize_square(square))
                
        return squares