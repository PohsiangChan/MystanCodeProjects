"""
File: 
Name: Shawn Chan
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked


VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
action = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global action

    window = GWindow(800, 500, title='bouncing_ball.py')
    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    ball.filled = True
    window.add(ball)

    click_cnt = 0
    onmouseclicked(drop)

    while True:
        pause(DELAY)
        if action:
            click_cnt += 1
            vy = 0
            while True:
                ball.move(VX, vy)
                pause(DELAY)
                vy += GRAVITY
                if ball.y + ball.height >= window.height:
                    # 當球碰到地面
                    vy *= -REDUCE
                if ball.x >= window.width:
                    action = False
                    ball.x = START_X
                    ball.y = START_Y
                    break
        if click_cnt >= 3:
            break
        onmouseclicked(drop)


def drop(_):
    global action
    action = True

    # global click_cnt, can_click
    # if click_cnt < 3 and can_click == 1:
    #     # 球超出右側視窗3次後，球將回到原起點位置並保持不動
    #     vy = 0
    #     click_cnt += 1
    #     can_click = 0
    #     # 球在彈跳過程中不受使用者滑鼠點擊影響
    #     while True:
    #         ball.move(VX, vy)
    #         pause(DELAY)
    #         vy += GRAVITY
    #         if ball.y + ball.height >= window.height:
    #             # 當球碰到地面
    #             vy *= -REDUCE
    #         if ball.x >= window.width:
    #             ball.x = START_X
    #             ball.y = START_Y
    #             can_click = 1
    #             break


if __name__ == "__main__":
    main()
