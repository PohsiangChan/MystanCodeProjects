"""
File: anagram.py
Name: Shawn Chan
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    ####################
    print('Welcome to stanCode \"Anagram Generator" (or -1 to quit)')

    while True:
        search = input('Find anagrams for: ')
        if search == EXIT:
            break
        else:
            start = time.time()
            anagrams = find_anagrams(search)
            print(f'{len(anagrams)} anagrams: {anagrams}')
            ####################
            end = time.time()
            print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    # 比對用字典
    dictionary = []
    with open(FILE, 'r') as f:
        for line in f:
            # 去除換行
            word = line.strip()
            dictionary.append(word)
    return dictionary


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    dictionary = read_dictionary()
    ans = []
    # 記錄有用過的字母
    used_ch = [False] * len(s)
    find_anagrams_helper(s, '', len(s), dictionary, ans, used_ch)
    return ans


def find_anagrams_helper(s, current_word, s_len, dictionary, ans, used_ch):
    # BS: 長度跟 len(s) 一樣
    if len(current_word) == s_len:
        # 需要是字典裡有的字跟去除重複
        if current_word in dictionary and current_word not in ans:
            # 不確定是不是放這裡
            print('searching...')
            print(f'Found: {current_word}')
            ans.append(current_word)

    else:
        for i in range(s_len):
            if not used_ch[i]:
                if not has_prefix(current_word, dictionary):
                    break

                # choose
                used_ch[i] = True
                # explore
                find_anagrams_helper(s, current_word + s[i], s_len, dictionary, ans, used_ch)
                # un-choose
                used_ch[i] = False


def has_prefix(sub_s, dictionary):
    """
    :param sub_s:
    :param dictionary:
    :return:
    """
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False

    # #  binary search
    # left, right = 0, len(dictionary) - 1
    # while right >= left:
    #     mid = (right + left) // 2
    #     word = dictionary[mid]
    #     if word.startwith(sub_s):
    #         return True
    #     elif word < sub_s:
    #         left = mid + 1
    #     else:
    #         right = mid - 1
    # return False


if __name__ == '__main__':
    main()
