"""
File: 
Name: Shawn Chan
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GLine, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO: Draw a one punch man.
    He became bald in order to become stronger.
    """

    window = GWindow(800, 400)

    body = GRect(200, 300, x=275, y=230)
    window.add(body)
    body.fill_color = 'gold'

    label = GLabel('One Punch')
    label.font = '-50'
    label.color = 'red'
    window.add(label, x=255, y=80)

    neck = GArc(80, 160, 0, -180)
    neck.filled = True
    neck.fill_color = 'antiquewhite'
    window.add(neck, 335, 190)

    neck1 = GLine(350, 230, 355, 200)
    window.add(neck1)

    neck2 = GLine(400, 200, 405, 230)
    window.add(neck2)

    face = GOval(150, 200, x=300, y=10)
    window.add(face)
    face.fill_color = 'antiquewhite'

    l_eyebrow = GArc(50, 5, 0, 120)
    window.add(l_eyebrow, 320, 80)

    l_eye = GOval(30, 15, x=330, y=90)
    window.add(l_eye)
    l_eye.fill_color = 'white'

    l_eyeball = GOval(5, 5, x=330+l_eye.width/2, y=90+l_eye.height/2)
    l_eyeball.filled = True
    window.add(l_eyeball)

    r_eyebrow = GArc(50, 5, 60, 120)
    window.add(r_eyebrow, 390, 80)

    r_eye = GOval(30, 15, x=390, y=90)
    window.add(r_eye)
    r_eye.fill_color = 'white'

    r_eyeball = GOval(5, 5, x=390+r_eye.width/2, y=90+r_eye.height/2)
    r_eyeball.filled = True
    window.add(r_eyeball)

    nose = GLine(375, 110, 365, 150)
    window.add(nose)

    nose2 = GLine(365, 150, 370, 155)
    window.add(nose2)

    mouse = GArc(50, 25, 0, -180)
    window.add(mouse, 350, 170)
    mouse.fill_color = 'rosybrown'

    left_arm = GOval(50, 200, x=250, y=230)
    window.add(left_arm)
    left_arm.fill_color = 'gold'

    right_arm = GOval(50, 200, x=450, y=230)
    window.add(right_arm)
    right_arm.fill_color = 'gold'


if __name__ == '__main__':
    main()
