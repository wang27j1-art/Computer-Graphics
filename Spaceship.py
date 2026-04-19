# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 10:50:06 2026

@author: zahuo
"""

from graphics import *
import time

win = GraphWin("Spaceship", 600, 600)
win.setBackground("darkblue")

rocket = Rectangle(Point(250, 600), Point(350, 400))
rocket.setFill("lightpink")
rocket_top = Polygon(Point(250, 400), Point(300, 275), Point(350, 400))
rocket_top.setFill("lightblue")
wing1 = Polygon(Point(250, 600), Point(150, 600), Point(250, 500))
wing1.setFill("lightblue")
wing2 = Polygon(Point(350, 600), Point(450, 600), Point(350, 500))
wing2.setFill("lightblue")

rocket.draw(win)
rocket_top.draw(win)
wing1.draw(win)
wing2.draw(win)

for i in range(250):
    rocket.move(0, -3)
    rocket_top.move(0, -3)
    wing1.move(0, -3)
    wing2.move(0, -3)
    time.sleep(0.02)
    
win.getMouse()
win.close()
