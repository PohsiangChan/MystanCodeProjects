"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nmb = int(input('Secret number: '))


def main():
    """
    Decipher the input string by consider its positions shifting to the right.
    """
    noun = upper(input('What\'s the ciphered string? '))
    print(deciphered(noun))


def deciphered(string):
    ans = ''
    for i in range(len(string)):
        ch = string[i]
        for j in range(len(ALPHABET)):
            ch2 = ALPHABET[j]
            if ch == ch2:
                if j+nmb > 25:
                    ans = ans + ALPHABET[(j+nmb)-26]
                else:
                    ans = ans + ALPHABET[j+nmb]
            if not ch.isalpha():
                ans = ans + ch
                break
    return ans


def upper(s):
    ans = ''
    for i in range(len(s)):
        ch = s[i]
        if s[i].islower():
            ans += s[i].upper()
        else:
            ans += ch
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
