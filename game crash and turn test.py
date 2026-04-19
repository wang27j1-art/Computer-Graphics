# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 10:04:58 2026

@author: zahuo
"""

from graphics import *
import random
import time
import numpy as np

def rot(aPoint, rPoint, angle):
    oldX = aPoint.getX()
    oldY = aPoint.getY()
    rX = rPoint.getX()
    rY = rPoint.getY()
    newX = (oldX-rX)*np.cos(angle) - (oldY-rY)*np.sin(angle) + rX
    newY = (oldX-rX)*np.sin(angle) + (oldY-rY)*np.cos(angle) + rY
    return Point(newX, newY)

def make_car(center, angle, base_pts, color):
    rotated_points = []
    for p in base_pts:
        world_p = Point(center.getX() + p.getX(), center.getY() + p.getY())
        rotated_points.append(rot(world_p, center, angle))
    car_poly = Polygon(rotated_points)
    car_poly.setFill(color)
    car_poly.setOutline("black")
    car_poly.setWidth(2)
    return car_poly

def shape_bounds(shape):
    pts = shape.getPoints()
    xs = [p.getX() for p in pts]
    ys = [p.getY() for p in pts]
    return min(xs), min(ys), max(xs), max(ys)

def bounds_overlap(b1, b2):
    x1, y1, x2, y2 = b1
    a1, b1y, a2, b2y = b2
    return not(x2 <= a1 or a2 <= x1 or y2 <= b1y or b2y <= y1)

def dist(p1, p2):
    return ((p1.getX() - p2.getX())**2 +(p1.getY() - p2.getY())**2) ** 0.5

def car_close_to(center, target_center, threshold):
    return dist(center, target_center) <= threshold

win = GraphWin("Delivery Game", 1000, 500)
win.setBackground("gray")
win.autoflush = False

building_1 = Polygon(Point(625, 308), Point(950, 308), Point(950, 358), Point(625, 358))
building_1.setFill("gray40")
building_1.setOutline("black")
building_1.setWidth(2)

building_2 = Polygon(Point(132, 162), Point(390, 162), Point(390, 255), Point(132, 255))
building_2.setFill("gray40")
building_2.setOutline("black")
building_2.setWidth(2)

building_3 = Polygon(Point(456, 44), Point(606, 44), Point(606, 175), Point(456, 175))
building_3.setFill("gray40")
building_3.setOutline("black")
building_3.setWidth(2)

building_4 = Polygon(Point(271, 283), Point(436, 283), Point(436, 466), Point(271, 466))
building_4.setFill("gray40")
building_4.setOutline("black")
building_4.setWidth(2)

building_5 = Polygon(Point(626, 59), Point(747, 59), Point(747, 226), Point(626, 226))
building_5.setFill("gray40")
building_5.setOutline("black")
building_5.setWidth(2)

building_1.draw(win)
building_2.draw(win)
building_3.draw(win)
building_4.draw(win)
building_5.draw(win)

buildings = [building_1, building_2, building_3, building_4, building_5]
building_bounds = [shape_bounds(b) for b in buildings]

half_w = 75
half_h = 35
base_car = [Point(-half_w, -half_h), Point(half_w, -half_h), Point(half_w, half_h), Point(-half_w, half_h)]
car_center = Point(125, 85)
angle = 0

#Text(Point((x1+x2)/2, (y1+y2)/2), str(i+1)).draw(win)

crash_msg = Rectangle(Point(300, 150), Point(700, 350))
crash_msg.setFill("red")
crash_text = Text(Point(500, 250), "CRASH")
crash_text.setFill("white")
crash_text.setSize(30)
crash_text.setStyle("bold")

car_colors = ["red", "yellow", "green", "darkgreen", "teal", "blue", "darkblue", "purple", "white", "black", "gold"]
car_color = random.choice(car_colors)
car = make_car(car_center, angle, base_car, car_color)
car.draw(win)

speed = 4
crashed = False

carrying = False
deliveries = 0

pickup = Circle(Point(120, 420), 18)
pickup.setFill("green")
pickup.setOutline("black")
pickup.draw(win)

dropoff = Circle(Point(900, 80), 18)
dropoff.setFill("dodgerblue")
dropoff.setOutline("black")
dropoff.draw(win)

status = Text(Point(500, 20), "Go to PICKUP (green)")
status.setSize(24)
status.setStyle("bold")
status.draw(win)

start = time.time()
timer_text = Text(Point(900, 20), "Time: 0.0")
timer_text.draw(win)

while not crashed:
    key = win.checkKey()
    
    dx = dy = 0
    if key == "Left":
        dx -= speed
    elif key == "Right":
        dx += speed
    elif key == "Up":
        dy -= speed
    elif key == "Down":
        dy += speed
    elif key == "q":
        break
    
    if dx != 0 or dy != 0:
        
        car_center = Point(car_center.getX() + dx, car_center.getY() + dy)
        margin_x = half_w
        margin_y = half_h
        cx = max(margin_x, min(1000 - margin_x, car_center.getX()))
        cy = max(margin_y, min(500 - margin_y, car_center.getY()))
        car_center = Point(cx, cy)
        
        if dx > 0:
            angle = 0
        elif dx < 0:
            angle = np.pi
        elif dy < 0:
            angle = np.pi / 2
        elif dy > 0:
            angle = 3 * np.pi / 2
        
        car.undraw()
        car = make_car(car_center, angle, base_car, car_color)
        car.draw(win)
        
        car_bounds = shape_bounds(car)
        for bnd in building_bounds:
            if bounds_overlap(car_bounds, bnd):
                crash_msg.draw(win)
                crash_text.draw(win)
                crashed = True
                break
      
        if not crashed:
            if not carrying:
                if car_close_to(car_center, pickup.getCenter(), 30):
                    carrying = True
                    pickup.undraw()
                    status.setText("Package picked up! Go to DROP-OFF (blue)")
            else:
                if car_close_to(car_center, dropoff.getCenter(), 30):
                    deliveries += 1
                    carrying = False
                    status.setText("Delivered! Total: " + str(deliveries) + ". Return to PICKUP (green)")

                    if deliveries >= 3:
                        win_box = Rectangle(Point(250, 150), Point(750, 350))
                        win_box.setFill("darkgreen")
                        win_text = Text(Point(500, 250), "YOU WIN!")
                        win_text.setFill("white")
                        win_text.setSize(30)
                        win_text.setStyle("bold")
                        win_box.draw(win)
                        win_text.draw(win)
                        crashed = True
                    else:
                        new_p = Point(random.randint(60, 940), random.randint(60, 440))
                        pickup = Circle(new_p, 18)
                        pickup.setFill("green")
                        pickup.setOutline("black")
                        pickup.draw(win)
            
    elapsed = time.time() - start
    timer_text.setText(f"Time: {elapsed:.1f}")   
        
    win.update()
    time.sleep(0.02)
    
win.getMouse()
win.close()