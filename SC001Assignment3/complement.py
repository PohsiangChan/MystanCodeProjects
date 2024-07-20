"""
File: complement.py
Name:
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    The complement of ATGC is TACG, and when the input is empty, it should display "DNA string is missing."
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    ans = ''
    if dna == '':
        return 'DNA string is missing.'
    else:
        for i in range(len(dna)):
            ch = dna[i]
            if ch == 'A':
                ans = ans + 'T'
            elif ch == 'T':
                ans = ans + 'A'
            elif ch == 'G':
                ans = ans + 'C'
            else:
                ans = ans + 'G'
        return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
