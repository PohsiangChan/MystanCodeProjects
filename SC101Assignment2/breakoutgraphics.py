"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window_width-paddle_width)/2, y=(self.window_height-paddle_offset))
        self.window.add(self.paddle)
        self.paddle.fill_color = True
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.window.add(self.ball, x=(self.window_width-self.ball.width)/2, y=(self.window_height-self.ball.height)/2)
        self.ball.fill_color = True

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        self.count = 0
        self.bricks_num = brick_cols * brick_rows

        # Initialize our mouse listeners
        onmouseclicked(self.velocity)
        onmousemoved(self.change_position)
        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.bricks = GRect(brick_width, brick_height, x=j*(brick_spacing+brick_width), y=brick_offset+i*(brick_spacing+brick_height))
                self.window.add(self.bricks)
                if i == 0 or i == 1:
                    self.bricks.filled = True
                    self.bricks.fill_color = 'red'
                    self.bricks.color = 'red'
                if i == 2 or i == 3:
                    self.bricks.filled = True
                    self.bricks.fill_color = 'lightsalmon'
                    self.bricks.color = 'lightsalmon'
                if i == 4 or i == 5:
                    self.bricks.filled = True
                    self.bricks.fill_color = 'yellow'
                    self.bricks.color = 'yellow'
                if i == 6 or i == 7:
                    self.bricks.filled = True
                    self.bricks.fill_color = 'green'
                    self.bricks.color = 'green'
                if i == 8 or i == 9:
                    self.bricks.filled = True
                    self.bricks.fill_color = 'blue'
                    self.bricks.color = 'blue'

    def velocity(self, event):
        if self.__dx == 0 and self.__dy == 0:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self, dx):
        self.__dx = dx

    def set_dy(self, dy):
        self.__dy = dy

    # paddle 隨滑鼠移動
    def change_position(self, mouse):
        self.paddle.x = mouse.x - self.paddle.width / 2
        if self.paddle.x < 0:
            self.paddle.x = 0
        if self.paddle.x + self.paddle.width > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width

    def bounce(self):
        for i in range(2):
            for j in range(2):
                test_x = self.ball.x + (BALL_RADIUS * 2) * i
                test_y = self.ball.y + (BALL_RADIUS * 2) * j
                maybe_obj = self.window.get_object_at(test_x, test_y)

                # is not None
                if maybe_obj:
                    if maybe_obj is self.paddle:
                        if self.__dy > 0:
                            self.__dy = -self.__dy
                    else:
                        self.__dy = -self.__dy
                        self.window.remove(maybe_obj)
                        self.bricks_num -= 1

        # c1 = self.window.get_object_at(self.ball.x, self.ball.y)
        # c2 = self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y)
        # c3 = self.window.get_object_at(self.ball.x, self.ball.y + BALL_RADIUS * 2)
        # c4 = self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y + BALL_RADIUS * 2)

        if self.ball.x <= 0 or self.ball.x + BALL_RADIUS * 2 >= self.window_width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy

        # if c1 is self.paddle or c2 is self.paddle:
        #     self.__dy = -self.__dy
        # else:
        #     # 確認c1
        #     if c1 is not None and c1 is not self.paddle:
        #         self.__dy = -self.__dy
        #         self.window.remove(c1)
        #         self.bricks_num -= 1
        #     # 確認c2
        #     elif c2 is not None and c2 is not self.paddle:
        #         self.__dy = -self.__dy
        #         self.window.remove(c2)
        #         self.bricks_num -= 1
        #     # 確認c3
        #     elif c3 is not None and c3 is not self.paddle:
        #         self.__dy = -self.__dy
        #         self.window.remove(c3)
        #         self.bricks_num -= 1
        #     # 確認c4
        #     elif c4 is not None and c4 is not self.paddle:
        #         self.__dy = -self.__dy
        #         self.window.remove(c4)
        #         self.bricks_num -= 1

    def restart(self):
        if self.bricks_num == 0:
            self.__dx = 0
            self.__dy = 0

        if self.ball.y > self.window.height:
            if self.count <= 1:
                self.window.add(self.ball, x=(self.window_width - self.ball.width) / 2, y=(self.window_height - self.ball.height) / 2)
                self.count += 1
                self.__dx = 0
                self.__dy = 0
