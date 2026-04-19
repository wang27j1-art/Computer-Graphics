# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 12:01:44 2026

@author: zahuo
"""

from graphics import *

def reflect_scaled(prev_p2, p0, alpha=0.6):
    vX = p0.getX() - prev_p2.getX()
    vY = p0.getY() - prev_p2.getY()
    return Point(p0.getX() + alpha*vX, p0.getY() + alpha*vY)

def seg(p0, p1, p2, p3, n, win):
    bcurve(p0, p1, p2, p3, n, win)
    return p2, p3

def seg_join(prev_p2, p0, p2, p3, n, win,
             alpha=0.6,      # strength of inherited tangent
             dx=20, dy=12,   # soft reset direction (handwriting “entry”)
             mix=0.35):       # 0 = pure C1, 1 = pure soft reset
    
    # C1 handle (inherited direction)
    p1_c1 = reflect_scaled(prev_p2, p0, alpha)

    # Soft-reset handle (manual direction)
    p1_soft = Point(p0.getX() + dx, p0.getY() + dy)

    # Blend
    p1 = Point(
        (1-mix)*p1_c1.getX() + mix*p1_soft.getX(),
        (1-mix)*p1_c1.getY() + mix*p1_soft.getY()
    )

    bcurve(p0, p1, p2, p3, n, win)
    return p2, p3

def seg_c1(prev_p2, p0, p2, p3, n, win, alpha=0.6):
    p1 = reflect_scaled(prev_p2, p0, alpha)
    bcurve(p0, p1, p2, p3, n, win)
    return p2, p3

def soft_entry(p0, dx, dy):
    return Point(p0.getX() + dx, p0.getY() + dy)
    
def bcurve(p0, p1, p2, p3, num_points, win):
    prev = None
    for i in range(num_points + 1):
        t = i / num_points
        x = (1-t)**3 * p0.getX() + 3*(1-t)**2 * t * p1.getX() + 3*(1-t)*t**2 * p2.getX() + t**3 * p3.getX()
        y = (1-t)**3 * p0.getY() + 3*(1-t)**2 * t * p1.getY() + 3*(1-t)*t**2 * p2.getY() + t**3 * p3.getY()
        cur = Point(x, y)
        if prev is not None:
            seg = Line(prev, cur)
            seg.setWidth(3)
            seg.draw(win)
        prev = cur

def draw_j():
    J0 = Point(170, 200)
    J1 = Point(140, 120)
    J2 = Point(250, 120)
    J3 = Point(250, 210)
    bcurve(J0, J1, J2, J3, 300, win)
    
    J4 = Point(310, 360)
    J5 = Point(310, 640)
    J6 = Point(240, 780)
    bcurve(J3, J4, J5, J6, 600, win)
    
    J7 = Point(120, 900)
    J8 = Point(90, 720)
    J9 = Point(260, 710)
    bcurve(J6, J7, J8, J9, 450, win)
    
    Jendo1 = Point(320, 690)
    Jendo2 = Point(380, 650)
    Jendo3 = Point(420, 620)
    Jp2, Jp3 = seg(J9, Jendo1, Jendo2, Jendo3, 220, win)
    return Jp2, Jp3

def draw_o(prev_p2, start, win):
    oX, oY = start.getX(), start.getY()

    o0 = start
    o2 = Point(oX + 70, oY + 90)     # old p2
    o3 = Point(oX + 40, oY + 140)    # endpoint
    op2, op3 = seg_c1(prev_p2, o0, o2, o3, 250, win, alpha=0.65)

    o5 = Point(oX - 60, oY + 170)    # old p2 (NOT o4)
    o6 = Point(oX - 40, oY + 120)    # endpoint
    op2, op3 = seg_c1(op2, op3, o5, o6, 250, win, alpha=0.65)

    o8 = Point(oX + 30, oY + 40)     # old p2 (NOT o7)
    oendy = Point(oX + 80, oY + 70)  # endpoint
    op2, op3 = seg_c1(op2, op3, o8, oendy, 250, win, alpha=0.65)

    return op2, op3

def draw_y(prev_p2, start, win):
    yX, yY = start.getX(), start.getY()

    y0 = start
    y2 = Point(yX + 75, yY + 20)     # old p2
    y3 = Point(yX + 55, yY + 55)     # endpoint
    yp2, yp3 = seg_c1(prev_p2, y0, y2, y3, 200, win, alpha=0.65)

    y5 = Point(yX + 15, yY + 140)    # old p2 (NOT y4)
    y6 = Point(yX + 5,  yY + 165)    # endpoint
    yp2, yp3 = seg_c1(yp2, yp3, y5, y6, 260, win, alpha=0.55)

    y8 = Point(yX + 40, yY + 165)    # old p2
    y9 = Point(yX + 55, yY + 145)    # endpoint
    yp2, yp3 = seg_c1(yp2, yp3, y8, y9, 180, win, alpha=0.60)

    yendc2 = Point(yX + 150, yY + 95) # old p2 (NOT yendc1)
    yendc  = Point(yX + 210, yY + 85) # endpoint
    yp2, yp3 = seg_c1(yp2, yp3, yendc2, yendc, 200, win, alpha=0.70)

    return yp2, yp3

def draw_c(prev_p2, start, win):
    cX, cY = start.getX(), start.getY()
    c0 = start

    # Use + because y grows DOWN on the screen
    c2 = Point(cX + 60, cY + 10)
    c3 = Point(cX + 35, cY + 35)

    cp2, cp3 = seg_join(prev_p2, c0, c2, c3, 220, win,
                        alpha=0.55, dx=20, dy=+15, mix=0.6)

    c5 = Point(cX - 5,  cY + 20)
    c6 = Point(cX + 80, cY + 25)

    # C1 smooth internal join at c3
    cp2, cp3 = seg_c1(cp2, c3, c5, c6, 220, win, alpha=0.6)

    return cp2, cp3

def draw_e(prev_p2, start, win):
    eX, eY = start.getX(), start.getY()
    e0 = start

    e2 = Point(eX + 35, eY + 55)
    e3 = Point(eX - 10, eY + 45)

    ep2, ep3 = seg_join(prev_p2, e0, e2, e3, 220, win,
                        alpha=0.50, dx=18, dy=+12, mix=0.7)

    e5 = Point(eX + 15, eY + 5)
    e_end = Point(eX + 90, eY + 25)

    ep2, ep3 = seg_c1(ep2, e3, e5, e_end, 240, win, alpha=0.6)

    return ep2, ep3

win = GraphWin("Bezier", 1000, 1000)

j_p2, j_p3 = draw_j()
o_p2, o_p3 = draw_o(j_p2, j_p3, win)  
y_p2, y_p3 = draw_y(o_p2, o_p3, win)
c_p2, c_p3 = draw_c(y_p2, y_p3, win)
e_p2, e_p3 = draw_e(c_p2, c_p3, win)

win.getMouse()
win.close()