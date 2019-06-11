# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:09:48 2019

@author: kiera
"""
import numpy as np
import pandas as pd
import gradients

class Find_squares_anywhere(object):
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
            
    def find_squares_anywhere(image, smallest, largest, stride):
        
        gradient = gradients.grad_mag(image)
        m,n = np.shape(gradient)
        squares = []
        locs = []
        res = []
        max_count = 0
        stop = 0
        index = 0
        
        for k in range(smallest, largest, 2):
            
            gradient_copy = gradient
            count = 0
            
            for i in range(0,n-k,stride):
                for j in range(0,m-k,stride):
                    
                    window = gradient_copy[j:j+k,i:i+k]
                    
                    if(np.sum(window) >= (np.std(gradient)*((k**2)/8))):
                        a = np.sum(window[0,:])
                        b = np.sum(window[k-1,:])
                        c = np.sum(window[:,0])
                        d = np.sum(window[:,k-1])
                        if (a + b + c + d < np.std(gradient)*4):
                            selection = image[j:j+k,i:i+k]
                            squares.append(gradients.resize_square(selection))
                            gradient_copy[j:j+k,i:i+k] = 0
                            count += 1
                            locs.append([index,j,i])
                            index += 1
            if (count >= max_count):
                max_count = count
            else: 
                stop += 1
                if (stop > 1): break
                continue
        locs = pd.DataFrame(np.array(locs))
        locs = locs.sort_values(by=[locs.columns[1], locs.columns[2]])
        for item in np.array(locs):
            index = item[0]
            res.append(squares[index])
        
        
        return res        