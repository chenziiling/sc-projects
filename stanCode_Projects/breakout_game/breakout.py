"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()
    live = NUM_LIVES
    score = 0
    dx = graphics.get_dx()
    dy = graphics.get_dy()

    # Add animation loop here!
    while True:
        pause(FRAME_RATE)
        if graphics.user_click:
            graphics.ball.move(dx, dy)
        if graphics.is_hitup() or graphics.is_hitpaddle():
            dy = -dy
        if graphics.is_hitside():
            dx = -dx

        # detect if the ball hit bricks or not
        if graphics.is_hit_something():
            what = graphics.hit_something()
            if graphics.is_brick(what):
                graphics.window.remove(what)
                score += 10
                graphics.resetscore(score)
                if score == graphics.all:
                    graphics.win
                dy = -dy
        if graphics.is_hitground():
            live -= 1
            graphics.resetlive(live)
            graphics.window.remove(graphics.ball)
            graphics.user_click = False
            if graphics.lives == 0:
                graphics.window.clear()
                graphics.lose()
                break
            else:
                graphics.reset_ball()
                if graphics.user_click:
                    graphics.ball.move(dx, dy)



"""
            The code below is my original though, and I think I can modify these after lessons so I didn't delete them.

            if graphics.is_hitbrick_left():
                graphics.window.remove(graphics.window.get_object_at(graphics.ball.x, graphics.ball.y))
                score += 10
                graphics.resetscore(score)
                graphics.dx = -graphics.dx
                graphics.dy = -graphics.dy
            if graphics.is_hitbrick_right():
                graphics.window.remove(graphics.window.get_object_at(graphics.ball.x, graphics.ball.y))
                score += 10
                graphics.resetscore(score)
                graphics.dx = -graphics.dx
                graphics.dy = -graphics.dy
            if graphics.is_hitbrick_up():
                graphics.window.remove(graphics.window.get_object_at(graphics.ball.x, graphics.ball.y))
                score += 10
                graphics.resetscore(score)
                graphics.dy = -graphics.dy
            if graphics.is_hitbrick_down():
                graphics.window.remove(graphics.window.get_object_at(graphics.ball.x, graphics.ball.y))
                score += 10
                graphics.resetscore(score)
                graphics.dy = -graphics.dy
"""


if __name__ == '__main__':
    main()
