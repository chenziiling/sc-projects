"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 20
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
cir = GOval(SIZE, SIZE, x=START_X, y=START_Y)
cir.filled = True
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(cir)
    onmouseclicked(bump)


def bump(m):
    global count
    if cir.x == START_X:
        v = 0
        count += 1
        while True:
            if cir.x < window.width and count <= 3:
                if cir.y < window.height:
                    v += 1
                    fall(cir, v)
                elif cir.y+SIZE >= window.height:
                    a = GRAVITY+GRAVITY*v
                    rebound(cir, v, a)
                    v = 0
            else:
                window.remove(cir)
                window.add(cir, x=START_X, y=START_Y)
                break


def fall(c, v):
    """
    :param c: OVal, the ball will fall down until touch the ground
    :param v: int, to make the ball fall faster
    """
    c.move(VX, GRAVITY+GRAVITY*v)
    pause(DELAY)


def rebound(c, vy, a):
    """
    :param c: OVal, the ball will back to the highest point
    :param vy: int, to reduce the velocity of the ball
    :param a: int, the velocity when the ball touch the ground
    """
    for i in range(vy):
        a *= REDUCE
        c.move(VX, -a)
        pause(DELAY)


if __name__ == "__main__":
    main()
