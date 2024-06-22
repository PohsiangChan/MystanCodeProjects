"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    while True:
        graphics.bounce()
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        graphics.ball.move(dx, dy)
        # graphics.set_dx(dx)
        # graphics.set_dy(dy)
        pause(FRAME_RATE)
        graphics.restart()


if __name__ == '__main__':
    main()
