"""
File: MidpointKarel.py
Name: Shawn Chan
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
    pre-condition: Karel is at the [1,1], facing East
    post-condition: Karel is at the middle on 1 beeper
    """
    if front_is_clear():
        put_beeper()
        while front_is_clear():
            move()
        put_beeper()  # Put beeper on the each side of street 1
        turn_around()
        while on_beeper():
            if not facing_south():  # for get out of the loop
                move_beeper()
            while not on_beeper():
                if front_is_clear():
                    if facing_west():  # scenario 1
                        move()
                    if facing_east():  # scenario 2
                        move()
            if facing_west():  # while on beeper
                turn_around()
            else:
                if facing_east():
                    turn_around()
    else:  # 1*1
        put_beeper()


def move_beeper():
    """
    pre-condition: Karel is on the beeper
    post-condition:
    """
    pick_beeper()
    if front_is_clear():
        move()
    if front_is_clear():
        put_beeper()
    if front_is_clear():
        move()
    if on_beeper():  # if there is second beeper
        if front_is_clear():
            pick_beeper()
        else:
            turn_right()  # 2*2
            if front_is_clear():
                move()
        turn_around()
        move()
        if facing_west():  # turn to facing South to get out of the loop
            turn_left()
        else:
            if facing_east():
                turn_right()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
