# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 08:58:54 2026

@author: zahuo
"""

from graphics import *
import random

def overlaps(b1, b2, gap=0):
    x1, y1, x2, y2 = b1
    a1, b1y, a2, b2y = b2

    # Expand both rectangles by gap (so buildings have space between them)
    x1 -= gap
    y1 -= gap
    x2 += gap
    y2 += gap

    a1 -= gap
    b1y -= gap
    a2 += gap
    b2y += gap

    # If one is completely left/right/above/below the other => NO overlap
    return not (x2 <= a1 or a2 <= x1 or y2 <= b1y or b2y <= y1)

building_bounds = []

win = GraphWin("Delivery Game Draft 1", 1000, 500)
win.setBackground("gray")

for i in range(5):
    placed = False

    while not placed:
        x1 = random.randint(25, 900)
        y1 = random.randint(25, 400)
        x2 = random.randint(x1 + 40, 975)
        y2 = random.randint(y1 + 40, 475)

        b = (x1, y1, x2, y2)

        # Check against all existing buildings
        is_overlapping = False
        for old in building_bounds:
            if overlaps(b, old, gap=10):
                is_overlapping = True
                break

        if is_overlapping:
            continue  # try a new random rectangle

        # Accept and draw
        building_bounds.append(b)
        building = Rectangle(Point(x1, y1), Point(x2, y2))
        building.setFill("dimgray")
        building.setOutline("black")
        building.draw(win)

        placed = True

        print("Building " + str(i + 1))
        print("Coordinate 1:", x1, y1)
        print("Coordinate 2:", x2, y2)

#Text(Point((x1+x2)/2, (y1+y2)/2), str(i+1)).draw(win)

win.getMouse()
win.close()
