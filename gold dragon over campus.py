# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 10:21:23 2026

@author: zahuo
"""

from graphics import *
import numpy as np

win = GraphWin("Dragon on Campus", 500, 500)
Rainbow = Image(Point(250, 250), "Rainbow_400_300.gif")

Dragon = Image(Point(250, 250), "GoldDragon.gif")
Dragon.draw(win)
win.getMouse()

for j in range(0, 400):
    for k in range(0, 247):
        red, green, blue = Dragon.getPixel(j, k)
        if (red != 255 and green != 215 and blue != 0):
            r, g, b = Rainbow.getPixel(j, k)
            Dragon.setPixel(j, k, color_rgb(r, g, b))
            
win.getMouse()
win.close()