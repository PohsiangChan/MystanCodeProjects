"""
File: rocket.py
Name:
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    From top to bottom, complete the six components sequentially, and resize them according to the size value.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    for i in range(SIZE):  # i=row
        for j in range((SIZE+1)-i):  # j=col
            if j <= ((SIZE-1)-i):
                print(' ', end='')
            else:  # put /\
                for k in range(i+1):  # k=repeat n times
                    print('/', end='')
                for k in range(i+1):
                    print('\\', end='')
        print('')


def belt():
    print('+', end='')
    for i in range(SIZE*2):  # i=repeat n times
        print('-', end='')
    print('+', end='')
    print('')


def upper():
    for i in range(SIZE):  # i=row
        print('|', end='')  # part1:|
        for j in range(SIZE*2):  # j=col
            if j <= ((SIZE-2)-i):  # part2:.
                print('.', end='')
            if j == ((SIZE-1)-i):  # part3:/\
                for k in range(i+1):
                    print('/', end='')
                for k in range(i+1):
                    print('\\', end='')
            if j == ((SIZE*2)-1-i):   # part4:.
                for k in range((SIZE-1)-i):  # k=repeat n times
                    print('.', end='')
        print('|', end='')  # part5:|
        print('')


def lower():
    for i in range(SIZE):  # i=row
        print('|', end='')  # part1:|
        for j in range(SIZE*2):  # j=col
            if j <= i-1:  # part2:.
                print('.', end='')
            if j == i:  # part3:\/
                for k in range(SIZE-i):
                    print('\\', end='')
                for k in range(SIZE-i):
                    print('/', end='')
            if j == ((SIZE*2)-i):   # part4:.
                for k in range(i):  # k=repeat n times
                    print('.', end='')
        print('|', end='')  # part5:|
        print('')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
