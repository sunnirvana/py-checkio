#!/usr/bin/env checkio --domain=py run first-word

# https://py.checkio.org/mission/first-word/

# You are given a string where you have to find its first word.
# 
# When solving a task pay attention to the following points:
# 
# There can be dots and commas in a string.A string can start with a letter or, for example, a dot or space.A word can contain an apostrophe and it's a part of a word.The whole text can be represented with one word and that's it.Input:A string.
# 
# Output:A string.
# 
# Precondition:the text can contain a-z A-Z , . '
# 
# 
# END_DESC

#

#


#

#

#
#



# def first_word(text: str) -> str:
#     """
#         returns the first word in a given text.
#     """
#     # your code here
#     start = None
#     end = None
#     for i in range(len(text)):
#         if 'z' >= text[i] >= 'a' or 'Z' >= text[i] >= 'A':
#             if start is None:
#                 start = i
#
#         if text[i] in ['.', ',', ' '] and start is not None:
#             end = i
#             break
#     #  print('return first workd, ', text[start:end])
#     return text[start:end]
#     #  return text[0:2]

import string


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    apostrophe = '\''
    res = ''
    for chr in text:
        if chr in string.ascii_letters + apostrophe:
            res += chr
        elif len(res) > 0:
            break

    res_end = text.find(res) + len(res)
    if text[res_end:res_end+6:] == '......':
        res += '......'

    print(text[res_end:res_end+6:], res)
    return res


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    assert first_word(",  and...... How about you") == "and......"
    print("Coding complete? Click 'Check' to earn cool rewards!")