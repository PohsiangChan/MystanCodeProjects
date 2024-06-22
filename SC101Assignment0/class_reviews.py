"""
File: class_reviews.py
Name: Shawn Chan
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = '-1'


def main():
    """
    TODO: Based on student class, calculate the highest and lowest scores as well as the average score.
    """
    max_001 = -float('inf')
    min_001 = float('inf')
    cnt_001 = 0
    ttl_score_001 = 0
    max_101 = -float('inf')
    min_101 = float('inf')
    cnt_101 = 0
    ttl_score_101 = 0

    classes = upper(str(input('Which Class ? ')))
    while True:
        if classes == EXIT:
            print('No class scores were entered.')
            break

        score = int(input('Score ? '))
        if classes == 'SC001':
            if score > max_001:
                max_001 = score
            if score < min_001:
                min_001 = score
            cnt_001 += 1
            ttl_score_001 += score
            classes = upper(str(input('Which Class ? ')))
        elif classes == 'SC101':
            if score > max_101:
                max_101 = score
            if score < min_101:
                min_101 = score
            cnt_101 += 1
            ttl_score_101 += score
            classes = upper(str(input('Which Class ? ')))

    if cnt_001 == 0 and cnt_101 == 0:
        print('No class scores were entered.')

    if cnt_001 > 0 or cnt_101 > 0:
        print('=============SC001=============')
        if cnt_001 > 0:
            print('Max (001)' + str(max_001))
            print('Min (001)' + str(min_001))
            print('Avg (001)' + str(ttl_score_001 / cnt_001))
        else:
            print('No score for SC001')
        print('=============SC001=============')
        if cnt_101 > 0:
            print('Max (101)' + str(max_101))
            print('Min (101)' + str(min_101))
            print('Avg (101)' + str(ttl_score_101 / cnt_101))
        else:
            print('No score for SC101')


def upper(s):
    ans = ''
    for i in range(len(s)):
        ch = s[i]
        if s[i].islower():
            ans += s[i].upper()
        else:
            ans += ch
    return ans


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
