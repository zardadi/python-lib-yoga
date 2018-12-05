#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:14:09 2018

@author: rajeevroy
"""

#import pyplot module
import matplotlib.pyplot as plt 

class Plot:
    def __init__(self):
        pass
    def revenue(pobject):   
        x=[]
        y=[]
        for i in pobject:
            x.append(i.id)
            y.append(i.getRev())     
        plt.bar(x,y) 
        plt.title('Revenue by Customer') 
        plt.xlabel('User ID') 
        plt.ylabel('Revenue') 
        plt.show()
        return True
    def exercise(pobject):   
        x=[]
        y=[]
        for i in pobject:
            x.append(i.name)
            y.append(i.time)     
        plt.bar(x,y) 
        plt.title('Time by Exercise') 
        plt.xlabel('User ID') 
        plt.ylabel('Time') 
        plt.show()
        return True