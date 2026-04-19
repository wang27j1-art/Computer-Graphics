# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 10:39:43 2026

@author: zahuo
"""

from graphics import *
import random

win = GraphWin("Circle Fun", 500, 500)
win.setBackground("lightyellow")

def draw_random_circle():
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "black", "white", "brown", "gray", "lightgreen", "darkgreen", "lightblue", "darkblue", "lightpink", "magenta"]
    picked_color = random.choice(colors)
    radius = random.randint(25, 75)
    
    randX = random.randint(0, 500)
    randY = random.randint(0, 500)
    
    circle = Circle(Point(randX, randY), radius)
    circle.setFill(picked_color)
    circle.draw(win)
    
close_btn = Rectangle(Point(420, 0), Point(500, 40))
close_btn.setFill("red")

circle_btn = Rectangle(Point(340, 0), Point(420, 40))
circle_btn.setFill("green")

circle_text = Text(Point(380, 20), "Circle O")
circle_text.setTextColor("lightgreen")

close_text = Text(Point(460, 20), "Close X")
close_text.setTextColor("lightpink")

circle_btn.draw(win)
close_btn.draw(win)
circle_text.draw(win)
close_text.draw(win)

while True:
    clickPoint = win.getMouse()
    xVal = clickPoint.getX()
    yVal = clickPoint.getY()
    if yVal < 40:
        if (xVal > 340 and xVal < 420):
            draw_random_circle()
        elif xVal > 420:
            win.close()
            break
            