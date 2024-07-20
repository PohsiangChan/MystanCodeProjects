"""
File: extension1_MidpointKarel.py
Name: 
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    TODO:
    """
    while front_is_clear():
        if not on_beeper():
            put_beeper()
            move()
    put_beeper()
    turn_around()
    while front_is_clear():
        move()
        if on_beeper():
            pick_beeper()
            turn_around()
            while front_is_clear():
                move()
            put_beeper()
            turn_around()
    turn_around()
    while front_is_clear():
        move()
    turn_around()
    while on_beeper():
        pick_beeper()
        if on_beeper():
            pick_beeper()
        move()
        put_beeper()
        turn_around()
        while front_is_clear():
            move()
        turn_around()
        while not on_beeper():
            move()





def turn_around():
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
