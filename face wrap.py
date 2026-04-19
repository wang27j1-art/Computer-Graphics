# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 12:23:51 2026

@author: zahuo
"""

from graphics import *
import numpy as np

win = GraphWin(("Face Wrap"), 1500, 500)
win.setBackground(color_rgb(203, 197, 234))

my_face_1 = Image(Point(250, 250), "my_face.gif")
my_face_1.draw(win)

my_face_2 = Image(Point(750, 250), "my_face.gif")
my_face_2.draw(win)

my_face_3 = Image(Point(1250, 250), "my_face.gif")
my_face_3.draw(win)
win.getMouse()

for j in range(0, 192):
    for k in range(0, 384):
        rl, gl, bl = my_face_2.getPixel(j, k)
        my_face_2.setPixel(383 - j, k, color_rgb(rl, gl, bl))

for j in range(192, 384):
    for k in range(0, 384):
        rr, gr, br = my_face_3.getPixel(j, k)
        my_face_3.setPixel(383 - j, k, color_rgb(rr, gr, br))
    
win.getMouse()
win.close()