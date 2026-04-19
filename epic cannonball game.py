# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 10:35:39 2026

@author: zahuo
"""

from graphics import *
import numpy as np
import time
import random

def barrel_points(center, degrees, base_points):
    theta = degrees * np.pi / 180
    p1, p2, p3, p4 = base_points
    return (rot(p1, center, theta), rot(p2, center, theta), rot(p3, center, theta), rot(p4, center, theta))

def redraw_cannon(win, cannon_obj, center, degrees, base_points):
    if cannon_obj is not None:
        cannon_obj.undraw()
    
    p1, p2, p3, p4 = barrel_points(center, degrees, base_points)
    new_cannon = Polygon(p1, p2, p3, p4)
    new_cannon.setFill("darkgray")
    new_cannon.setOutline("black")
    new_cannon.setWidth(3)
    new_cannon.draw(win)
    win.update()
    return new_cannon
    
def rot(aPoint, rPoint, angle):
    oldX = aPoint.getX()
    oldY = aPoint.getY()
    rX = rPoint.getX()
    rY = rPoint.getY()
    newX = (oldX-rX)*np.cos(angle) - (oldY-rY)*np.sin(angle) + rX
    newY = (oldX-rX)*np.sin(angle) + (oldY-rY)*np.cos(angle) + rY
    return Point(newX, newY)
        
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
win = GraphWin("Epic Cannon Game", 1000, 500)
win.setBackground("lightblue")
win.autoflush = False

grass = Rectangle(Point(0, 500), Point(999, 475))
grass.setFill("green")
grass.draw(win)

cannonBall = Circle(Point(45, 460), 12)
cannonBall.setFill('black')
cannonBall.draw(win)

cannon_center = Point(45, 460)
base_barrel = (Point(20, 400), Point(20, 480), Point(70, 480), Point(70, 400))
cannon = redraw_cannon(win, None, cannon_center, 45, base_barrel)

easy_target = Rectangle(Point(690, 380), Point(860, 460))
easy_target.setFill("lightyellow")
easy_target.setOutline("black")
easy_target.setWidth(2)
easy_target.draw(win)

medium_target = Polygon(
    Point(760, 220), Point(800, 240), Point(820, 290),
    Point(780, 330), Point(740, 290), Point(760, 240)
)
medium_target.setFill("steelblue")
medium_target.setOutline("black")
medium_target.setWidth(3)
medium_target.draw(win)

hard_target = Polygon(Point(910, 300), Point(940, 320), Point(930, 360), Point(890, 360), Point(880, 320))
hard_target.setFill("cyan")
hard_target.setOutline("white")
hard_target.setWidth(3)
hard_target.draw(win)

bonus_star = Polygon(
    Point(965, 285),
    Point(970, 300),
    Point(985, 300),
    Point(973, 310),
    Point(978, 325),
    Point(965, 315),
    Point(952, 325),
    Point(957, 310),
    Point(945, 300),
    Point(960, 300)
)
bonus_star.setFill("gold")
bonus_star.setOutline("black")
bonus_star.setWidth(2)
bonus_star.draw(win)


hit_msg = Text(Point(500, 150), "HIT")
hit_msg.setFill("red")
hit_msg.setSize(30)
hit_msg.setStyle("bold")

play_again_btn = Rectangle(Point(400, 175), Point(600, 275))
play_again_btn.setFill("lightgreen")
play_again_msg = Text(Point(500, 225), "Shoot Again?")
play_again_msg.setStyle("bold")


#this should be read in
input_degrees_text = Text(Point(425, 50), "Enter Degrees:")
input_degrees_text.draw(win)
input_velocity_text = Text(Point(425, 100), "Enter a Velocity:")
input_velocity_text.draw(win)
input_degrees = Entry(Point(525, 50), 4)
input_degrees.draw(win)
input_degrees.setFill("lightpink")
input_velocity = Entry(Point(525, 100), 4)
input_velocity.draw(win)
input_velocity.setFill("lightpink")

input_dv_error = None
while True:
    win.getMouse()
    try:
        degrees = int(input_degrees.getText())
        velocity = int(input_velocity.getText())
        if input_dv_error is not None:
            input_dv_error.undraw()
            input_dv_error = None
        break
    except:
        input_degrees.setText("")
        input_velocity.setText("")
        if input_dv_error is not None:
            input_dv_error.undraw()
        input_dv_error = Text(Point(500, 150), "Error: Value must be an integer.")
        input_dv_error.setFill("red")
        input_dv_error.setStyle("bold")
        input_dv_error.draw(win)

degrees = max(0, min(90, degrees))
velocity = max(1, velocity)

cannon = redraw_cannon(win, cannon, cannon_center, degrees, base_barrel)
xpos, ypos = trajectory(degrees, velocity)

total_shots = 10
num_shots = 0
total_score = 0
shot_score = 0
round_number = 1
score_cordy = 25

easy_x = 775
easy_y = 420
medium_x = 780
medium_y = 275
hard_x = 910
hard_y = 330
bonus_x = 965
bonus_y = 305

# Initial hitboxes
bonus_minx, bonus_maxx = bonus_x - 20, bonus_x + 20
bonus_miny, bonus_maxy = bonus_y - 20, bonus_y + 20

hard_minx, hard_maxx = hard_x - 30, hard_x + 30
hard_miny, hard_maxy = hard_y - 30, hard_y + 30

for round_number in range(1, total_shots + 1):
    shot_score = 0
    hit_shown = False
    for k in range(2, 75):
        cannonBall.undraw()
        cannonBall = Circle(Point(xpos[k], 500 - ypos[k]), 12)
        cannonBall.setFill("black")
        cannonBall.draw(win)
        bx = xpos[k]
        by = 500 - ypos[k]
        
        if bonus_minx <= bx <= bonus_maxx and bonus_miny <= by <= bonus_maxy:
            shot_score = 10
            if not hit_shown:
                hit_msg.draw(win)
                hit_shown = True

                bonus_star.undraw()
                bonus_x = random.randint(920, 980)
                bonus_y = random.randint(220, 360)

                bonus_star = Polygon(
                    Point(bonus_x,     bonus_y - 20),
                    Point(bonus_x + 5, bonus_y - 5),
                    Point(bonus_x + 20, bonus_y - 5),
                    Point(bonus_x + 8, bonus_y + 5),
                    Point(bonus_x + 12, bonus_y + 20),
                    Point(bonus_x,     bonus_y + 10),
                    Point(bonus_x - 12, bonus_y + 20),
                    Point(bonus_x - 8, bonus_y + 5),
                    Point(bonus_x - 20, bonus_y - 5),
                    Point(bonus_x - 5, bonus_y - 5)
                )
                bonus_star.setFill("gold")
                bonus_star.setOutline("black")
                bonus_star.setWidth(2)
                bonus_star.draw(win)
        
                bonus_minx, bonus_maxx = bonus_x - 20, bonus_x + 20
                bonus_miny, bonus_maxy = bonus_y - 20, bonus_y + 20
                
        elif hard_minx <= bx <= hard_maxx and hard_miny <= by <= hard_maxy:
            shot_score = 5
            if not hit_shown:
                hit_msg.draw(win)
                hit_shown = True

                hard_target.undraw()
                hard_x = random.randint(860, 940)
                hard_y = random.randint(240, 380)
        
                hard_target = Polygon(
                    Point(hard_x,      hard_y - 30),
                    Point(hard_x + 30, hard_y - 10),
                    Point(hard_x + 20, hard_y + 30),
                    Point(hard_x - 20, hard_y + 30),
                    Point(hard_x - 30, hard_y - 10)
                )
                hard_target.setFill("cyan")
                hard_target.setOutline("white")
                hard_target.setWidth(3)
                hard_target.draw(win)
        
                hard_minx, hard_maxx = hard_x - 30, hard_x + 30
                hard_miny, hard_maxy = hard_y - 30, hard_y + 30
            
        elif (medium_x - 40 <= bx <= medium_x + 40) and (medium_y - 40 <= by <= medium_y + 60):
            shot_score = 2
            if not hit_shown:
                hit_msg.draw(win)
                hit_shown = True

                medium_target.undraw()
                medium_x = random.randint(650, 850)
                medium_y = random.randint(200, 350)

                medium_target = Polygon(
                Point(medium_x - 20, medium_y - 40),
                Point(medium_x + 20, medium_y - 20),
                Point(medium_x + 40, medium_y + 20),
                Point(medium_x,      medium_y + 60),
                Point(medium_x - 40, medium_y + 20),
                Point(medium_x - 20, medium_y - 20)
                )   
                medium_target.setFill("steelblue")
                medium_target.setOutline("black")
                medium_target.setWidth(3)
                medium_target.draw(win)
                
        elif 690 <= xpos[k] <= 860 and 380 <= 500 - ypos[k] <= 460:
            if not hit_shown:
                shot_score = 1
                hit_msg.draw(win)
                hit_shown = True
        win.update()
        time.sleep(0.15)
        
    total_score += shot_score
    num_shots += 1
    score_text = "Round " + str(round_number) + " Score: " + str(shot_score)
    score_notif = Text(Point(100, score_cordy), score_text)
    score_notif.draw(win)
    score_cordy += 30
    hit_msg.undraw()
    
    play_again_btn.draw(win)
    play_again_msg.draw(win)
    
    player_click = win.getMouse()
    playerX = player_click.getX()
    playerY = player_click.getY()
    if (400 < playerX < 600) and (175 < playerY < 275):
        play_again_btn.undraw()
        play_again_msg.undraw()
        cannonBall.undraw()

        input_degrees.setText("")
        input_velocity.setText("")

        while True:
            win.getMouse()
            try:
                degrees = int(input_degrees.getText())
                velocity = int(input_velocity.getText())
                if input_dv_error is not None:
                    input_dv_error.undraw()
                    input_dv_error = None
                break
            except:
                input_degrees.setText("")
                input_velocity.setText("")
                if input_dv_error is not None:
                    input_dv_error.undraw()
                input_dv_error = Text(Point(500, 150), "Error: Value must be an integer.")
                input_dv_error.setFill("red")
                input_dv_error.setStyle("bold")
                input_dv_error.draw(win)
        degrees = max(0, min(90, degrees))
        velocity = max(1, velocity)
        cannon = redraw_cannon(win, cannon, cannon_center, degrees, base_barrel)
        cannonBall = Circle(Point(45, 460), 12)
        cannonBall.setFill("black")
        cannonBall.draw(win)
        xpos, ypos = trajectory(degrees, velocity)
    else:
        break

        
total_score_msg = "Total Score: " + str(total_score)
total_score_text = Text(Point(100, 350), total_score_msg)
total_score_text.setStyle("bold")
total_score_text.draw(win)
   
win.getMouse()
win.close()