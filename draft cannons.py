# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 08:56:44 2026

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
win = GraphWin("Draft Cannon", 1000, 500)
win.setBackground("lightblue")

grass = Rectangle(Point(0, 500), Point(999, 475))
grass.setFill("green")
grass.draw(win)

cannonBall = Circle(Point(45, 460), 12)
cannonBall.setFill('black')
cannonBall.draw(win)

#this should be read in
degrees = 45
velocity = 180
xpos, ypos = trajectory(degrees, velocity)
for k in range(2, 50):
    cannonBall = Circle(Point(xpos[k], 500 - ypos[k]), 12)
    cannonBall.draw(win)
    time.sleep(0.15)
    
win.getMouse()
win.close()