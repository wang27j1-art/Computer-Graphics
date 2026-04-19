# -*- coding: utf-8 -*-
"""
flip the dragon

@author: zahuo
"""

from graphics import *
import numpy as np

win = GraphWin("flip the dragon", 500, 500)

#Display the original image
Dragon = Image(Point(250, 250), "NCSSM_Dragon_400_247.gif")
Dragon.draw(win)
win.getMouse()

for j in range(0, 400):
    for k in range(0, 125):
        red, green, blue = Dragon.getPixel(j, k)
        r, g, b = Dragon.getPixel(j, 246 - k)
        Dragon.setPixel(j, 246 - k, color_rgb(red, green, blue))
        Dragon.setPixel(j, k, color_rgb(r, g, b))
win.getMouse()     
win.close()


