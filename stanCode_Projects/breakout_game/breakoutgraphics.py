"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # total bricks
        self.all = brick_rows*brick_cols*10

        # set up score
        self.score = 0
        self.scorelabel = GLabel('score='+str(self.score), x=5, y=self.window.height-5)
        self.scorelabel.font = '-25'
        self.window.add(self.scorelabel)

        # set up lives
        self.lives = 3
        self.liveslabel = GLabel('lives=' + str(self.lives), x=320, y=self.window.height-5)
        self.liveslabel.font = '-25'
        self.window.add(self.liveslabel)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window.width-paddle_width)/2, y=self.window.height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        self.ball_radius = ball_radius
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, (self.window.width-ball_radius)/2, (self.window.height-ball_radius)/2)

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)  # dx is randomly picked from 1 to MAX_X_SPEED.
        if random.random() > 0.5:
            self.__dx = -self.__dx

        # Draw bricks.
        for i in range(brick_rows):
            self.brick = GRect(brick_width, brick_height, x=(brick_width + brick_spacing) * i, y=0)
            self.brick.fill_color = (0, 0, 255 - (i * 20))
            self.brick.color = (0, 0, 255 - (i * 20))
            self.brick.filled = True
            self.window.add(self.brick)
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height, x=(brick_width + brick_spacing) * i,
                                   y=(brick_height + brick_spacing) * j)
                self.brick.fill_color = (0, 0, 255 - (j * 20))
                self.brick.color = (0, 0, 255 - (i * 20))
                self.brick.filled = True
                self.window.add(self.brick)

        # Initialize our mouse listeners.
        onmousemoved(self.paddle_move)
        onmouseclicked(self.play)

        # click to start
        self.user_click = False

    # to detect if user clicked or not
    def play(self, m):
        if 0 <= m.x <= self.window.width and 0 <= m.y <= self.window.height:
            self.user_click = True

    def paddle_move(self, m):
        if m.x <= self.window.width-self.paddle.width:
            self.paddle.x = m.x

    def reset_ball(self):
        self.ball = GOval(self.ball_radius * 2, self.ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, (self.window.width - self.ball_radius) / 2, (self.window.height-self.ball_radius)/2)

    def resetscore(self, new):
        self.window.remove(self.scorelabel)
        self.score = new
        self.scorelabel = GLabel('score=' + str(self.score), x=5, y=self.window.height - 5)
        self.scorelabel.font = '-25'
        self.window.add(self.scorelabel)

    def resetlive(self, new):
        self.window.remove(self.liveslabel)
        self.lives = new
        self.liveslabel = GLabel('lives=' + str(self.lives), x=320, y=self.window.height - 5)
        self.liveslabel.font = '-25'
        self.window.add(self.liveslabel)

    def is_hitup(self):
        if self.ball.y < 0:
            return True

    def is_hitside(self):
        if self.ball.x < 0 or self.ball.x+self.ball.width > self.window.width:
            return True

    def is_hitpaddle(self):
        if self.window.get_object_at(self.ball.x+self.ball_radius*2, self.ball.y+self.ball_radius*2) == self.paddle or\
            self.window.get_object_at(self.ball.x, self.ball.y) == self.paddle or\
            self.window.get_object_at(self.ball.x+self.ball_radius*2, self.ball.y) == self.paddle or\
                self.window.get_object_at(self.ball.x, self.ball.y+self.ball_radius*2) == self.paddle:
            return True

    def is_hitground(self):
        if self.ball.y > self.window.height:
            return True

    # if wh is brick , it will be true and enter a loop to remove the brick
    def is_brick(self, wh):
        if wh is not self.paddle and wh is not self.scorelabel and wh is not self.liveslabel:
            return True

    # to check four angle of the ball is None or not
    def is_hit_something(self):
        if self.window.get_object_at(self.ball.x, self.ball.y) is None:
            if self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y) is None:
                if self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y + self.ball_radius * 2) is None:
                    if self.window.get_object_at(self.ball.x, self.ball.y + self.ball_radius * 2) is not None:
                        return True
                else:
                    return True
            else:
                return True
        else:
            return True

    # if the ball hit something, this function will return what thing is this
    def hit_something(self):
        if self.window.get_object_at(self.ball.x, self.ball.y) is None:
            if self.window.get_object_at(self.ball.x+self.ball_radius*2, self.ball.y) is None:
                if self.window.get_object_at(self.ball.x+self.ball_radius*2, self.ball.y+self.ball_radius*2) is None:
                    return self.window.get_object_at(self.ball.x, self.ball.y+self.ball_radius*2)
                else:
                    return self.window.get_object_at(self.ball.x+self.ball_radius*2, self.ball.y+self.ball_radius*2)
            else:
                return self.window.get_object_at(self.ball.x+self.ball_radius*2, self.ball.y)
        else:
            return self.window.get_object_at(self.ball.x, self.ball.y)

    # get dx and dy
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    # run out of all lives
    def lose(self):
        lose = GLabel('You Lose:(')
        lose.font = '-40'
        self.window.add(lose, x=(self.window.width-lose.width)/2, y=(self.window.height-lose.width)/2)

    # clean all the bricks
    def win(self):
        win = GLabel('You win:D')
        win.font = '-40'
        self.window.add(win, x=(self.window.width-win.width)/2, y=(self.window.height-win.width)/2)