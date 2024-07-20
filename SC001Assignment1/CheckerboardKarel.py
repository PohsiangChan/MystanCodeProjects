"""
File: CheckerboardKarel.py
Name: Shawn Chan
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: karel is at the [1,1], facing east
    post-condition: karel
    """
    if not front_is_clear():  # 1*1
        put_beeper()
    else:
        while front_is_clear():
            fill_one_line()
        while left_is_clear():  # consider not front_is_clear() situation
            turn_left()
            fill_one_line()


def fill_one_line():
    """
    pre-condition:
    post-condition:
    """
    while front_is_clear():
        if not on_beeper():
            put_beeper()
        move()
        if front_is_clear():
            move()
            if not on_beeper():
                put_beeper()
        else:  # when it's even number avenue, not front is clear happen
            move_to_next_street()
            if front_is_clear():
                put_beeper()
    while not front_is_clear():  # when it's odd number avenue, not front is clear happen
        move_to_next_street()
        if front_is_clear():
            move()


def move_to_next_street():
    """
    pre-condition: karel is at the street n next to the wall, might facing East or West
    post-condition: Karel is moving to the street n+1, still next to the wall but facing the opposite direction
    """
    if facing_east():
        if left_is_clear():
            turn_left()
            move()
            turn_left()
        else:  # if not left_is_clear
            turn_left()

    else:
        if facing_west():
            if right_is_clear():
                turn_right()
                move()
                turn_right()
            else:    # if not right_is_clear
                turn_right()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
