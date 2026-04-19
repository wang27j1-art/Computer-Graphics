# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 10:46:55 2026

@author: zahuo
"""

from graphics import *
import numpy as np

win = GraphWin("flip the dragon", 500, 500)

#Display the original image
Dragon = Image(Point(250, 250), "NCSSM_Dragon_400_247.gif")
Dragon.draw(win)
win.getMouse()

for j in range(0, 200):
    for k in range(0, 247):
        red, green, blue = Dragon.getPixel(j, k)
        r, g, b = Dragon.getPixel(399 - j, k)
        Dragon.setPixel(399 - j, k, color_rgb(red, green, blue))
        Dragon.setPixel(j, k, color_rgb(r, g, b))
        
win.getMouse()     
win.close()