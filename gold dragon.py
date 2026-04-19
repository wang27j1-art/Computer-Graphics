# -*- coding: utf-8 -*-
"""
class first dragon

Created on Tue Jan 13 10:07:51 2026

@author: zahuo
"""

from graphics import *
import numpy as np

win = GraphWin("First Dragon Program", 500, 500)
win.setBackground(color_rgb(150, 150, 150))

#Display the original image
Dragon = Image(Point(250, 250), "NCSSM_Dragon_400_247.gif")
Dragon.draw(win)
win.getMouse()

#Change to a Gold Dragon
for j in range(0, 400):
    for k in range(0, 247):
        red, green, blue = Dragon.getPixel(j, k)
        if (red != 255 and green != 255 and blue != 255):
            Dragon.setPixel(j, k, color_rgb(255, 215, 0))
        else:
            Dragon.setPixel(j, k, color_rgb(150, 150, 150))
win.getMouse()
Dragon.save("GoldDragon.gif")
win.close()