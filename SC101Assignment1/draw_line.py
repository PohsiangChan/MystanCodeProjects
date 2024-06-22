"""
File: 
Name: Shawn Chan
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

draw_circle = True
SIZE = 10
window = GWindow()
circle = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(click)


def click(event):
    # 需要讓畫圓跟直線在同一個 function 中
    global draw_circle
    # Variable
    if draw_circle == True:
        window.add(circle, x=event.x - SIZE / 2, y=event.y - SIZE / 2)
        draw_circle = False

    elif draw_circle == False:
        line = GLine(circle.x + SIZE / 2, circle.y + SIZE / 2, event.x + SIZE / 2, event.y + SIZE / 2)
        window.add(line)
        window.remove(circle)
        draw_circle = True

# def create_circle(event):
#     global circle
#     # 讓 circle 的位置可以給 create_line 使用
#     circle = GOval(SIZE, SIZE, x=event.x - SIZE / 2, y=event.y - SIZE / 2)
#     window.add(circle)


# def create_line(event):
#     line = GLine(circle.x + SIZE / 2, circle.y + SIZE / 2, event.x + SIZE / 2, event.y + SIZE / 2)
#     window.add(line)
#     window.remove(circle)


if __name__ == "__main__":
    main()
