# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 14:44:56 2026

@author: zahuo
"""

from graphics import *
from math import sqrt
import random

def check_boundaries(stat_text):
    new_click = win.getMouse()
    new_X = new_click.getX()
    new_Y = new_click.getY()
    
    code = None
    msg = None
    
    if new_Y < 50:
        if new_X < 150:
            code = "r"
            msg = "Default color set to red."
        elif new_X > 150 and new_X < 300:
            code = "g"
            msg = "Default color set to green."
        elif new_X > 300 and new_X < 450:
            code = "b"
            msg = "Default color set to blue."
        elif new_X > 450 and new_X < 600:
            code = "x"
            
    elif new_Y > 50 and new_Y < 100:
        if new_X < 200:
            code = "sq"
            msg = "Click two points to draw a rectangle."
        elif new_X > 200 and new_X < 400:
            code = "tri"
            msg = "Click three points to draw a triangle."
        elif new_X > 400 and new_X < 600:
            code = "c"
            msg = "Click two points to draw a circle."
    
    if msg is None:
        msg = "Click on a box."
    stat_text.setText(msg)
    return code

def draw_rectangle(color):   
    user_click1 = win.getMouse()
    user_click1.draw(win)
    user_click2 = win.getMouse()
    rect = Rectangle(user_click1, user_click2)
    rect.setFill(color)
    rect.draw(win)
    
def draw_triangle(color): 
    user_click1 = win.getMouse()
    user_click1.draw(win)
    user_click2 = win.getMouse()
    Line(user_click1, user_click2).draw(win)
    user_click3 = win.getMouse()
    tri = Polygon(user_click1, user_click2, user_click3)
    tri.setFill(color)
    tri.draw(win)

def distance(x1, x2, y1, y2):
    return sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

def draw_circle(color):   
    user_click1 = win.getMouse()
    user_X1 = user_click1.getX()
    user_Y1 = user_click1.getY()
    user_click1.draw(win)
    user_click2 = win.getMouse()
    user_X2 = user_click2.getX()
    user_Y2 = user_click2.getY()
    radius = distance(user_X1, user_X2, user_Y1, user_Y2)
    centerX_choices = [user_X1, user_X2]
    centerX = random.choice(centerX_choices)
    if centerX == user_X1:
        centerY = user_Y1
    else:
        centerY = user_Y2   
    full_circ = Circle(Point(centerX, centerY), radius)
    full_circ.setFill(color)
    full_circ.draw(win)

win = GraphWin("Shapes Drawing Tool", 600, 600)  

red_btn = Rectangle(Point(0, 0), Point(150, 50))
red_btn.setFill("red")
green_btn = Rectangle(Point(150, 0), Point(300, 50))
green_btn.setFill("green")
blue_btn = Rectangle(Point(300, 0), Point(450, 50))
blue_btn.setFill("blue")
exit_btn = Rectangle(Point(450, 0), Point(600, 50))
exit_btn.setFill("lightpink")
rect_btn = Rectangle(Point(0, 50), Point(200, 100))
tri_btn = Rectangle(Point(200, 50), Point(400, 100))
circ_btn = Rectangle(Point(400, 50), Point(600, 100))
red_text = Text(Point(75, 25), "Red")
red_text.setFill("white")
red_text.setStyle("bold")
green_text = Text(Point(225, 25), "Green")
green_text.setFill("white")
green_text.setStyle("bold")
blue_text = Text(Point(375, 25), "Blue")
blue_text.setFill("white")
blue_text.setStyle("bold")
rect_text = Text(Point(100, 75), "Rectangle")
rect_text.setStyle("bold")
tri_text = Text(Point(300, 75), "Triangle")
tri_text.setStyle("bold")
circ_text = Text(Point(500, 75), "Circle")
circ_text.setStyle("bold")
exit_line1 = Line(Point(460, 10), Point(590, 40))
exit_line1.setFill("magenta")
exit_line1.setWidth(5)
exit_line2 = Line(Point(590, 10), Point(460, 40))
exit_line2.setFill("magenta")
exit_line2.setWidth(5)
red_btn.draw(win)
green_btn.draw(win)
blue_btn.draw(win)
rect_btn.draw(win)
tri_btn.draw(win)
circ_btn.draw(win)
exit_btn.draw(win)
red_text.draw(win)
green_text.draw(win)
blue_text.draw(win)
rect_text.draw(win)
tri_text.draw(win)
circ_text.draw(win)
exit_line1.draw(win)
exit_line2.draw(win)

color_list = ["orange", "yellow", "purple"]
default_color = random.choice(color_list)

stat_text = Text(Point(300, 150), "Click on a box.")
stat_text.draw(win)

while True:
    do_this = check_boundaries(stat_text)
    
    if do_this == "r":
        default_color = "red"
    elif do_this == "g":
        default_color = "green"
    elif do_this == "b":
        default_color = "blue"
    elif do_this == "sq":
        draw_rectangle(default_color)
    elif do_this == "tri":
        draw_triangle(default_color)
    elif do_this == "c":
        draw_circle(default_color)
    elif do_this == "x":
        win.close()
        break