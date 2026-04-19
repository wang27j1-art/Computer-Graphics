# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 09:52:36 2026

@author: zahuo
"""

from graphics import *
import numpy as np

win = GraphWin("Campus", 500, 500)
Rainbow = Image(Point(250, 250), "Rainbow_400_300.gif")
Rainbow.draw(win)
win.getMouse()

'''
for j in range(0, 400):
    for k in range(0, 300):
        r, g, b = Rainbow.getPixel(j, k)
        intensity = int((r + g + b)/3)
        Rainbow.setPixel(j, k, color_rgb(intensity, intensity, intensity))
'''
for j in range(0, 400):
    for k in range(0, 300):
        r, g, b = Rainbow.getPixel(j, k)
        intensity = int((r*0.299 + g*0.587 + b*0.114))
        Rainbow.setPixel(j, k, color_rgb(intensity, intensity, intensity))
        
win.getMouse()  
win.close()