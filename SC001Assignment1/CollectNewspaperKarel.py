"""
File: CollectNewspaperKarel.py
Name: Shawn Chan
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: karel is in the upper left corner of the house, facing east
    post-condition: karel is in the upper left corner of the house, facing east
    """
    pick_newspaper()
    go_home()


def pick_newspaper():
    """
    pre-condition: karel is in the upper left corner of the house, facing east
    post-condition: karel is at the door of its house, facing east
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()


def go_home():
    """
    pre-condition: karel is at the door of its house, facing east
    post-condition: karel is in the upper left corner of the house, facing east
    """
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_around()
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
