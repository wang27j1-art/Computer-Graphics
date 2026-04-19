# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 13:02:47 2026

@author: zahuo
"""

from graphics import *

win = GraphWin("Traffic Light", 200, 200)
win.setBackground("lightblue")

rect = Rectangle(Point(75, 25), Point(125, 175))
rect.setFill("gray")

yellow_light = Circle(Point(100, 100), 25)
yellow_light.setFill("yellow")

red_light = yellow_light.clone()
red_light.setFill("red")
red_light.move(0, -50)

green_light = yellow_light.clone()
green_light.setFill("green")
green_light.move(0, 50)

rect.draw(win)
yellow_light.draw(win)
red_light.draw(win)
green_light.draw(win)

win.getMouse()
win.close()