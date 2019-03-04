#!/usr/bin/env checkio --domain=py run the-longest-palindromic

# https://py.checkio.org/mission/the-longest-palindromic/

# Write a function that finds the longestpalindromicsubstring of a given string. Try to be as efficient as possible!
# 
# If you find more than one substring you should return the one which is closer to the beginning.
# 
# Input:A text as a string.
# 
# Output:The longest palindromic substring.
# 
# Precondition:1 ≤ |text| ≤ 20
# The text contains only ASCII characters.
# 
# 
# END_DESC

from itertools import combinations


def is_palindromic(text):
    # print(text)
    i, j = 0, len(text) - 1
    while i < j:
        if text[i] != text[j]:
            return False
        i += 1
        j -= 1

    return True


def longest_palindromic(text):
    # firstly, store all positions for the same value
    # secondly, check the sub is palindromic
    char_dict = dict()
    for i, v in enumerate(text):
        if v in char_dict:
            char_dict[v].append(i)
        else:
            char_dict[v] = [i]

    print(text, char_dict)
    res_list = list()
    for k, v in char_dict.items():
        if len(v) <= 1:
            continue

        res_list.extend([
            text[pair[0]:pair[1] + 1]
            for pair in combinations(v, r=2)
            if is_palindromic(text[pair[0]:pair[1] + 1])
        ])

    # print(res_list)
    return max(res_list, key=len) if len(res_list) > 0 else text[0]

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"