# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 09:26:57 2026

@author: zahuo
"""

from graphics import *
import numpy as np

def trajectory(degrees, v0):
    theta = degrees*(np.pi/180)
    xarray = np.zeros(100)
    yarray = np.zeros(100)
    for t in np.arange(0, 100):
        real_t = t*0.2
        x = v0*np.cos(theta)*real_t
        y = v0*np.sin(theta)*real_t - 16*real_t**2
        y = max(25, y)
        xarray[t] = x
        yarray[t] = y
    return xarray, yarray

#Main
win = GraphWin("Cannon Target", 1000, 500)
win.setBackground("lightblue")
win.autoflush = False

grass = Rectangle(Point(0, 500), Point(999, 475))
grass.setFill("green")
grass.draw(win)

cannonBall = Circle(Point(45, 460), 12)
cannonBall.setFill('black')
cannonBall.draw(win)

target = Line(Point(750, 325), Point(800, 310))
target.setFill("red")
target.setWidth(5)
target.draw(win)

hit_msg = Text(Point(500, 125), "HIT")
hit_msg.setFill("red")
hit_msg.setSize(30)
hit_msg.setStyle("bold")

#this should be read in
degrees = 45
velocity = 180
xpos, ypos = trajectory(degrees, velocity)

for k in range(2, 50):
    cannonBall.undraw()
    cannonBall = Circle(Point(xpos[k], 500 - ypos[k]), 12)
    cannonBall.setFill("black")
    cannonBall.draw(win)
    
    if (750 <= xpos[k] <= 850) and (310 <= 500 - ypos[k] <= 325):
        hit_msg.draw(win)
        
    win.update()
    time.sleep(0.15)
    
win.getMouse()
win.close()