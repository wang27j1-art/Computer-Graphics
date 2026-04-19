# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 10:18:26 2026

@author: zahuo
"""

from graphics import *
win = GraphWin("Squares", 600, 600)
win.setBackground("light blue")

# The square function
def make_a_square(win, x_loc, y_loc, size, color):
    point1 = Point(x_loc, y_loc)
    point2 = Point(x_loc + size, y_loc + size)
    my_square = Rectangle(point1, point2)
    my_square.setFill(color)
    my_square.draw(win)

user_x_loc = int(input("Which x-coordinate? "))
user_y_loc = int(input("Which y-coordinate? "))
side_length = int(input("How long is each side? "))
user_color = input("What color do you want it to be? ")

make_a_square(win, user_x_loc, user_y_loc, side_length, user_color)

win.getMouse()
win.close()