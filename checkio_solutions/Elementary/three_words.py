#!/usr/bin/env checkio --domain=py run three-words

# https://py.checkio.org/mission/three-words/

# Let's teach the Robots to distinguish words and numbers.
# 
# You are given a string with words and numbers separated by whitespaces (one space).    The words contains only letters.    You should check if the string contains three words insuccession.    For example, the string "start 5one two three7 end" contains three words in succession.
# 
# Input:A string with words.
# 
# Output:The answer as a boolean.
# 
# Precondition:The input contains words and/or numbers. There are no mixed words (letters and digits combined).
# 0 < len(words) < 100
# 
# 
# END_DESC

#



#

#

#


#
#



def checkio(words: str) -> bool:
    if len(words) < 3:
        return False

    lst = words.split()
    # store the number positions
    numbers = [i for i in range(len(lst)) if lst[i].isnumeric()]
    if not numbers and len(words) >= 3:
        return True

    numbers = [0] + numbers + [len(lst)]

    #  print(numbers)
    for i in range(1, len(numbers)):
        if (numbers[i] - numbers[i-1]) > 3:
            return True

    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") is True, "Hello"
    assert checkio("He is 123 man") is False, "123 man"
    assert checkio("1 2 3 4") is False, "Digits"
    assert checkio("bla bla bla bla") is True, "Bla Bla"
    assert checkio("Hi") is False, "Hi"

    assert checkio("one two 3 four five 6 seven eight 9 ten eleven 12") is False, "on line"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")