"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    The system randomly selects a word, and the player inputs one English letter at a time.
    There are 7 chances to guess wrong. If the guessed letter is incorrect, it will be displayed as '_';
    if it is correct, it will be revealed."
    """
    ans = random_word()
    dashed_ans = dashed(ans)
    print('The word looks like: ' + dashed_ans)
    print('You have '+str(N_TURNS)+' wrong guesses left.')
    wrong_guesses = 0
    while wrong_guesses < N_TURNS:
        input_ch = upper(input('Your guess: '))
        if not input_ch.isalpha():
            print('illegal format')
        elif len(input_ch) != 1:
            print('illegal format')
        elif input_ch in ans:
            print('You are correct!')
            dashed_ans = update_dashed(ans, dashed_ans, input_ch)
            print('The word looks like: ' + dashed_ans)
            print('You have ' + str(N_TURNS-wrong_guesses) + ' wrong guesses left.')
            if '_' not in dashed_ans:
                print('You win!!')
                break
        else:
            print('There is no ' + str(input_ch) + '\'s in the word.')
            wrong_guesses += 1
            print('You have ' + str(N_TURNS-wrong_guesses) + ' wrong guesses left.')
            if wrong_guesses == 7:
                print('You are completely hung :(')
                break


def dashed(ans):
    look = ''
    for i in range(len(ans)):
        look = look + '_'
    return look


def update_dashed(ans, dashed_ans, input_ch):
    look = ''
    for i in range(len(ans)):
        if ans[i] == input_ch:
            look += input_ch
        else:
            look += dashed_ans[i]
    return look


def upper(s):
    ans = ''
    for i in range(len(s)):
        ch = s[i]
        if s[i].islower():
            ans += s[i].upper()
    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
