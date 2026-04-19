# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 09:58:54 2026

@author: zahuo
"""

from graphics import *
import random

win = GraphWin("Tic Tac Toe", 600, 700)
win.setBackground("black")

def play_tic_tac_toe():
    outcomes = ["X", "O"]
    tries = 0

    while tries < 10:
        click = win.getMouse()
        click_x = click.getX()
        click_y = click.getY()
        
        x_o = random.choice(outcomes)
        
        if click_y > 600:
            win.close()
            break
        
        if click_x < 200:
            if click_y < 200:
                mark = Text(Point(100, 100), x_o)
            elif click_y > 200 and click_y < 400:
                mark = Text(Point(100, 300), x_o)
            elif click_y > 400 and click_y < 600:
                mark = Text(Point(100, 500), x_o)
        elif click_x > 200 and click_x < 400:
            if click_y < 200:
                mark = Text(Point(300, 100), x_o)
            elif click_y > 200 and click_y < 400:
                mark = Text(Point(300, 300), x_o)
            elif click_y > 400 and click_y < 600:
                mark = Text(Point(300, 500), x_o)
        elif click_x > 400 and click_x < 600:
            if click_y < 200:
                mark = Text(Point(500, 100), x_o)
            elif click_y > 200 and click_y < 400:
                mark = Text(Point(500, 300), x_o)
            elif click_y > 400 and click_y < 600:
                mark = Text(Point(500, 500), x_o)
        mark.setTextColor("lightgreen")
        mark.setSize(30)
        mark.draw(win)
            
hline_1 = Line(Point(0, 200), Point(600, 200))
hline_1.setOutline("lightgreen")
hline_1.setWidth(5)

hline_2 = hline_1.clone()
hline_2.move(0, 200)

vline_1 = Line(Point(200, 0), Point(200, 600))
vline_1.setOutline("lightgreen")
vline_1.setWidth(5)

vline_2 = vline_1.clone()
vline_2.move(200, 0)

quit_btn = Rectangle(Point(0, 600), Point(600, 700))
quit_btn.setFill("lightgreen")

quit_message = Text(Point(300, 650), "QUIT GAME")
quit_message.setStyle("bold")
quit_message.setSize(15)

hline_1.draw(win)
hline_2.draw(win)
vline_1.draw(win)
vline_2.draw(win)
quit_btn.draw(win)
quit_message.draw(win)

play_tic_tac_toe()