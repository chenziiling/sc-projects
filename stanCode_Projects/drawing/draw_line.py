"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


count = 0
w = GWindow()
cir = GOval(10, 10)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(m):
    global count, cir
    count += 1
    'to count how many times does the user click'
    if count % 2 == 1:
        'count is odd'
        cir = GOval(10, 10, x=m.x-5, y=m.y-5)
        w.add(cir)
    else:
        'count is even'
        line = GLine(cir.x, cir.y, m.x, m.y)
        w.add(line)
        w.remove(cir)


if __name__ == "__main__":
    main()
