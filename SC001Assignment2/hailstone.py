"""
File: hailstone.py
Name: Shawn Chan
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""
EXIT = 1  # Sentinel value


def main():
    """
    pre-condition: -
    post-condition: Input a number. If it's odd, multiply by 3 and add 1. If it's even, divide by 2.
    Repeat until the number equals 1, and count the number of steps taken.
    """
    print('This program computes Hailstone sequences')
    number = int(input('Enter a number: '))
    steps = 0  # counting steps, start from 0

    if number == EXIT:
        print('It took ' + str(steps) + ' step to reach 1.')
    else:
        while True:
            if number == EXIT:
                break
            if number % 2 == 0:
                answer = int(number / 2)
                print(number, 'is even', 'so I take half:', answer)
            if number % 2 != 0:
                answer = int((number * 3)+1)
                print(number, 'is odd', 'so I make 3n+1:', answer)
            number = answer  # Throw the calculated numbers back into the loop
            steps += 1
        print('It took ' + str(steps) + ' steps to reach 1.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
