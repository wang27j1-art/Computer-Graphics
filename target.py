# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 12:54:51 2026

@author: zahuo
"""

from graphics import *

win = GraphWin("Target", 200, 200)
win.setBackground("lightpink")

r = 60
for i in range(3):
    c = Circle(Point(100, 100), r)
    if i % 2 != 0:
        c.setFill("white")
    else:
        c.setFill("red")
    c.draw(win)
    r -= 20
    
win.getMouse()
win.close()