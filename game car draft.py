# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 09:36:01 2026

@author: zahuo
"""

from graphics import *
import random

win = GraphWin("Delivery Game Draft 2", 1000, 500)
win.setBackground("gray")

building_1 = Rectangle(Point(625, 308), Point(950, 358))
building_1.setFill("gray40")
building_1.setOutline("black")
building_1.setWidth(2)

building_2 = Rectangle(Point(132, 162), Point(390, 255))
building_2.setFill("gray40")
building_2.setOutline("black")
building_2.setWidth(2)

building_3 = Rectangle(Point(456, 44), Point(606, 175))
building_3.setFill("gray40")
building_3.setOutline("black")
building_3.setWidth(2)

building_4 = Rectangle(Point(271, 283), Point(436, 466))
building_4.setFill("gray40")
building_4.setOutline("black")
building_4.setWidth(2)

building_5 = Rectangle(Point(626, 59), Point(747, 226))
building_5.setFill("gray40")
building_5.setOutline("black")
building_5.setWidth(2)

building_1.draw(win)
building_2.draw(win)
building_3.draw(win)
building_4.draw(win)
building_5.draw(win)

#Text(Point((x1+x2)/2, (y1+y2)/2), str(i+1)).draw(win)

car_colors = ["red", "yellow", "green", "teal", "blue", "purple", "white", "black", "gold"]
car_color = random.choice(car_colors)
car = Rectangle(Point(50, 50), Point(200, 120))
car.setFill(car_color)
car.setOutline("gray40")
car.setWidth(2)
car.draw(win)

car_center = Point(125, 85)

win.getMouse()
win.close()