# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 10:04:58 2026

@author: zahuo

Delivery Game (graphics.py)
- Drive the car to the green pickup circle, then deliver to the blue dropoff circle
- Avoid buildings (collision detection)
- Deliver 3 packages to win
Controls: Arrow keys to move, "q" to quit.

Collision system:
Buildings are polygons, but collisions use padded axis-aligned bounding boxes (AABB)
for simpler and faster detection.
"""

from graphics import *
import random
import time

# ------------------------- GEOMETRY / COLLISION HELPERS ------------------------- #

def shape_bounds(shape):
    """
    Returns an axis aligned bounding box for a Polygon/shape:
    (min_x, min_y, max_x, max_y)
    Used to make collision checks fast.
    """
    pts = shape.getPoints()
    xs = [p.getX() for p in pts]
    ys = [p.getY() for p in pts]
    return min(xs), min(ys), max(xs), max(ys)

def bounds_overlap(b1, b2):
    """
    Returns True if two axis-aligned bounding boxes overlap.
    Each box is (min_x, min_y, max_x, max_y).
    """
    x1, y1, x2, y2 = b1
    a1, y1b, a2, y2b = b2
    return not(x2 <= a1 or a2 <= x1 or y2 <= y1b or y2b <= y1)

def dist(p1, p2):
    """Euclidean distance between two points."""
    return ((p1.getX() - p2.getX())**2 +(p1.getY() - p2.getY())**2) ** 0.5

def car_close_to(center, target_center, threshold):
    """
    Returns True when the car center is within 'threshold' pixels of a target.
    Used for pickup/dropoff detection
    """
    return dist(center, target_center) <= threshold

def hitbox_bounds(center, w, h):
    """
    Returns a bounding box for a rectangle centered at 'center' with width w and height h.
    This is the car's collision hitbox.
    """
    return(center.getX() - w/2, center.getY() - h/2, center.getX() + w/2, center.getY() + h/2)

def inflate_bounds(b, pad):
    """
    Expands a bounding box by 'pad' pixels in all directions.
    - For cars: small pad (tighter driving).
    - For pickup spawning: bigger pad (prevents packages spawning too close to buildings.)
    """
    x1, y1, x2, y2 = b
    return(x1 - pad, y1 - pad, x2 + pad, y2 + pad)

def blocked(center, w, h, bounds_list):
    """Returns True if the car hitbox at 'center' overlaps ANY building bound in bounds_list."""
    tb = hitbox_bounds(center, w, h)
    return any(bounds_overlap(tb, bnd) for bnd in bounds_list)

# ------------------------- PICKUP SPAWNING ------------------------- #

def random_pickup_center(r, building_bounds, W, H, BANNER_H, car_center, dropoff_center, trials=200):
    """
    Chooses a random Point for the pickup circle (radius r) that:
    - stays on-screen (below the top banner)
    - not too close (within 80px) to car or dropoff
    Tries up to 'trials' random points, otherwise uses a safe fallback point.
    """
    for _ in range(trials):
        p = Point(random.randint(r, W - r), random.randint(BANNER_H + r, H - r))
        pb = (p.getX() - r, p.getY() - r, p.getX() + r, p.getY() + r)
        if any(bounds_overlap(pb, bnd) for bnd in building_bounds):
            continue
        if dist(p, car_center) < 80:
            continue
        if dist(p, dropoff_center) < 80:
            continue
        return p
    return Point(W//2, (BANNER_H + H)//2)

# ------------------------- MOVEMENT CLAMPING ------------------------- #

def clamp(v, lo, hi):
    """Clamps a value v into the interval [lo, hi]."""
    return max(lo, min(hi, v))

def clamp_center(p, w, h, W, H, BANNER_H):
    """
    Keeps the car fully inside the window bounds.
    - x stays inside [w/2, W - w/2]
    - y stays inside [BANNER_H + h/2, H - h/2] so it can't drive into the top banner area
    """
    cx = clamp(p.getX(), w/2, W - w/2)
    cy = clamp(p.getY(), BANNER_H + h/2, H - h/2)
    return Point(cx, cy)

# ------------------------- UI HELPERS ------------------------- #

def show_popup(box, text, secs):
    """
    Temporarily shows a message on screen (ex: WALL or BUMP).
    This is used when the car tries to move into a wall/building.
    """
    box.draw(win); text.draw(win); win.update()
    time.sleep(secs)
    box.undraw(); text.undraw()

def show_win():
    """Draws the win overlay when the player reaches 3 deliveries."""
    win_box = Rectangle(Point(250, 150), Point(750, 350))
    win_box.setFill("darkgreen")
    win_text = Text(Point(500, 250), "YOU WIN!")
    win_text.setFill("white")
    win_text.setSize(30)
    win_text.setStyle("bold")
    win_box.draw(win)
    win_text.draw(win)

# ------------------------- CAR SPRITE HELPERS ------------------------- #

def move_car(dx, dy):
    """
    Moves the visual car sprite. We track 'car_center' ourselves.
    Note: car_w/car_h represent the collision box and may differ from the image size.
    """
    car_sprite.move(dx, dy)
 
def set_facing(new_face):
    """
    Swaps the car image file so the car appears to face the direction of travel.
    new_face is one of: 'L', 'R', 'U', 'D'
    """
    global facing, car_sprite
    if new_face == facing:
        return
    facing = new_face
    car_sprite.undraw()
    car_sprite = Image(car_center, car_files[facing])
    car_sprite.draw(win)

# ------------------------- MOVEMENT + COLLISION LOGIC ------------------------- #

def try_move(dx, dy):
    """
    Attempts to move the car by (dx, dy).
    Movement rules:
    1) Clamp proposed position so the car stays inside the screen.
    2) If the full move is not blocked, take it.
    3) Otherwise, try sliding horizontally only.
    4) Otherwise, try sliding vertically only.
    5) If all are blocked, show a bump message.
    """
    global car_center

    old = car_center
    proposed = clamp_center(Point(old.getX() + dx, old.getY() + dy), car_w, car_h, W, H, BANNER_H)

    # If clamping prevented movement (hit the window border), show "WALL!"
    if proposed.getX() == old.getX() and proposed.getY() == old.getY():
        show_popup(bump_box, wall_text, 0.08)
        return
    
    # Try full move first
    if not blocked(proposed, car_w, car_h, building_bounds_car):
        move_car(proposed.getX() - old.getX(), proposed.getY() - old.getY())
        car_center = proposed
        return
    
    # If full move hits a building, try sliding in X only
    proposed_x = clamp_center(Point(old.getX() + dx, old.getY()), car_w, car_h, W, H, BANNER_H)
    if not blocked(proposed_x, car_w, car_h, building_bounds_car):
        move_car(proposed_x.getX() - old.getX(), 0)
        car_center = proposed_x
        return
    
    # If X slide fails, try sliding in Y only
    proposed_y = clamp_center(Point(old.getX(), old.getY() + dy), car_w, car_h, W, H, BANNER_H)
    if not blocked(proposed_y, car_w, car_h, building_bounds_car):
        move_car(0, proposed_y.getY() - old.getY())
        car_center = proposed_y
        return
    
    # If everything is blocked, show "BUMP!"
    show_popup(bump_box, bump_text, 0.12)

# Main
# ============================================================================= #
#                                GAME SETUP                                     #
# ============================================================================= #

# Create Window
win = GraphWin("Delivery Game", 1000, 500)
win.setBackground("gray")
win.autoflush = False

# Window constants
W = 1000
H = 500
BANNER_H = 70 # top UI area the car cannot enter

# ------------------------- BUILDINGS -------------------------
# Buildings are polygons; we create padded bounding boxes for collision checks.

building_1 = Polygon(Point(730, 340), Point(900, 340), Point(900, 390), Point(730, 390))
building_1.setFill("gray40")
building_1.setOutline("black")
building_1.setWidth(2)

building_2 = Polygon(Point(132, 140), Point(280, 140), Point(280, 255), Point(132, 255))
building_2.setFill("gray40")
building_2.setOutline("black")
building_2.setWidth(2)

building_3 = Polygon(Point(456, 80), Point(606, 80), Point(606, 150), Point(456, 150))
building_3.setFill("gray40")
building_3.setOutline("black")
building_3.setWidth(2)

building_4 = Polygon(Point(271, 283), Point(436, 283), Point(436, 466), Point(271, 466))
building_4.setFill("gray40")
building_4.setOutline("black")
building_4.setWidth(2)

building_5 = Polygon(Point(626, 100), Point(747, 100), Point(747, 267), Point(626, 267))
building_5.setFill("gray40")
building_5.setOutline("black")
building_5.setWidth(2)

building_1.draw(win)
building_2.draw(win)
building_3.draw(win)
building_4.draw(win)
building_5.draw(win)

buildings = [building_1, building_2, building_3, building_4, building_5]

PAD_CAR = 2         # small pad for driving collision
PAD_PICKUP = 10     # larger pad so pickup doesn't spawn too close to buildings

building_bounds_car = [inflate_bounds(shape_bounds(b), PAD_CAR) for b in buildings]
building_bounds_pickup = [inflate_bounds(shape_bounds(b), PAD_PICKUP) for b in buildings]

# ------------------------- CAR SETUP ------------------------- #

car_files = {
    "R": "car_red_160_90_r-removebg-preview.png",
    "L": "car_red_160_90_l-removebg-preview.png",
    "U": "car_red_160_90_u-removebg-preview.png",
    "D": "car_red_160_90_d-removebg-preview.png"
}

facing = "R"
car_center = Point(125, 85)

# Car hitbox size (used for collisions)
car_w = 90
car_h = 45

car_sprite = Image(car_center, car_files[facing])
car_sprite.draw(win)

# ------------------------- POPUPS / UI ------------------------- #

wall_text = Text(Point(500, 250), "WALL!")
wall_text.setFill("white")
wall_text.setSize(24)
wall_text.setStyle("bold")

bump_text = Text(Point(500, 250), "BUMP!")
bump_text.setFill("white")
bump_text.setSize(24)
bump_text.setStyle("bold")
bump_box = Rectangle(Point(420, 215), Point(580, 285))
bump_box.setFill("red")

# ------------------------- GAME OBJECTS ------------------------- #

speed = 3
crashed = False # used to end the main loop

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

# Timer UI
start = time.time()
timer_text = Text(Point(900, 20), "Time: 0.0")
timer_text.draw(win)

# ============================================================================= #
#                                MAIN GAME LOOP                                 #
# ============================================================================= #

# Game loop runs at ~50 FPS (sleep 0.02) and updates timer + screen each frame.
while not crashed:
    # Read keyboard input (non-blocking)
    key = win.checkKey()
    
    dx = dy = 0
    if key == "Left":
        set_facing("L")
        dx -= speed
    elif key == "Right":
        set_facing("R")
        dx += speed
    elif key == "Up":
        set_facing("U")
        dy -= speed
    elif key == "Down":
        set_facing("D")
        dy += speed
    elif key == "q":
        break  # quit game
    
    # Attempt movement if a direction key was pressed.
    if dx or dy:
        try_move(dx, dy)
        
    # ------------------- PICKUP / DROPOFF LOGIC ------------------- #
    # If not carrying: touching pickup circle picks up the package.
    # If carrying: touching dropoff circle delivers and increments deliveries.
    
    if not carrying and car_close_to(car_center, pickup.getCenter(), 40):
        carrying = True
        pickup.undraw()
        status.setText("Package picked up! Go to DROP-OFF (blue)")
        
    elif carrying and car_close_to(car_center, dropoff.getCenter(), 40):
        deliveries += 1
        carrying = False
        status.setText(f"Delivered! Total: {deliveries}. Return to PICKUP (green)")
          
        # Win condition: 3 deliveries ends game
        if deliveries >= 3:
            show_win()
            break
        
        # Respawn pickup in a random safe location
        r = 18
        new_p = random_pickup_center(r, building_bounds_pickup, W, H, BANNER_H, car_center, dropoff.getCenter())
        pickup = Circle(new_p, r)
        pickup.setFill("green")
        pickup.setOutline("black")
        pickup.draw(win)

    # ------------------- TIMER UPDATE + FRAME UPDATE ------------------- #
    elapsed = time.time() - start
    timer_text.setText(f"Time: {elapsed:.1f}")      
    win.update()
    time.sleep(0.02)

# Wait for click to close after win/quit
win.getMouse()
win.close()