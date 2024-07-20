"""
File: StoneMasonKarel.py
Name: Shawn Chan
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: karel is at the [1,1], facing east
    post-condition: karel is at the right side of the last arch, facing east
    """
    for i in range(2):
        if front_is_clear():
            go_up()
            move_forward()
            go_down()
            if front_is_clear():
                move_forward()
                if not front_is_clear():  # When arch is even, build another column and return to street 1.
                    go_up()
                    go_down()

def go_up():
    """
    pre-condition: karel is at the street 1, facing east
    post-condition: karel is at the street 5, facing east
    """
    turn_left()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
            move()
        else:
            if front_is_clear():
                move()
    if not on_beeper():  # not front_is clear add one more decision
        put_beeper()
    turn_right()


def move_forward():
    """
    pre-condition: karel is at the left side of the arch, facing east
    post-condition: karel is at the right side of the arch, facing east
    """
    for i in range(4):
        move()


def go_down():
    """
    pre-condition: karel is at the street 5, facing east
    post-condition: karel is at the street 1, facing east
    """
    turn_right()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
            move()
        else:
            if front_is_clear():
                move()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
