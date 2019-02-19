#!/usr/bin/env checkio --domain=py run long-repeat

# https://py.checkio.org/mission/long-repeat/

# There are four substring missionsthat were born all in one day and you shouldn’t be needed more than one day to solve them. All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).
# 
# This mission is the first one of the series. Here you should find the length of the longest substring that consists of the same letter. For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa". The last substring is the longest one which makes it an answer.
# 
# Input:String.Output:Int.
# 
# 
# END_DESC

import itertools


def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    if len(line) == 0:
        return 0
    if len(line) == 1:
        return 1

    max_len = 0
    for char, group in itertools.groupby(line):
        lst = list(group)
        # print(char, lst, len(lst))
        if len(lst) > max_len:
            max_len = len(lst)

    return max_len

    # substr_list = [line[0]]
    # for i in range(1, len(line)):
    #     if line[i] in substr_list[-1]:
    #         substr_list[-1] += line[i]
    #     else:
    #         substr_list.append(line[i])
    #
    # return len(max(substr_list, key=len))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')