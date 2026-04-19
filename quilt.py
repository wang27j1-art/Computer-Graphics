# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 13:16:51 2026

@author: zahuo
"""

from graphics import *

win = GraphWin("Quilt", 200, 200)
win.setBackground("blue")

def make_square_quilt(color_1, color_2):
    win.setBackground(color_1)
    
    big_red_square_1 = Rectangle(Point(200, 0), Point(100, 100))
    big_red_square_1.setFill(color_2)
    
    big_red_square_2 = big_red_square_1.clone()
    big_red_square_2.move(-100, 100)
    
    small_red_square_1 = Rectangle(Point(25, 25), Point(75, 75))
    small_red_square_1.setFill(color_2)
    
    small_red_square_2 = small_red_square_1.clone()
    small_red_square_2.move(100, 100)
    
    small_blue_square_1 = small_red_square_1.clone()
    small_blue_square_1.setFill(color_1)
    small_blue_square_1.move(0, 100)
    
    small_blue_square_2 = small_blue_square_1.clone()
    small_blue_square_2.move(100, -100)
    
    big_red_square_1.draw(win)
    big_red_square_2.draw(win)
    small_red_square_1.draw(win)
    small_red_square_2.draw(win)
    small_blue_square_1.draw(win)
    small_blue_square_2.draw(win)

make_square_quilt("blue", "red")

win.getMouse()
win.close()

