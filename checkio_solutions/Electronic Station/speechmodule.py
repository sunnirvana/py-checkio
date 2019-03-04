#!/usr/bin/env checkio --domain=py run speechmodule

# https://py.checkio.org/mission/speechmodule/

# Stephen's speech module is broken.    This module is responsible for his number pronunciation.    He has to click to input all of the numerical digits in a figure,    so when there are big numbers it can take him a long time.    Help the robot to speak properly and increase his number processing speed by writing a new speech module for him.    All the words in the string must be separated by exactly one space character.    Be careful with spaces -- it's hard to see if you place two spaces instead one.
# 
# Input:A number as an integer.
# 
# Output:The string representation of the number as a string.
# 
# How it is used:This concept may be useful for the speech synthesis software or automatic reports systems.    This system can also be used when writing a chatbot by assigning words or phrases numerical    values and having a system retrieve responses based on those values.
# 
# Precondition:0 < number < 1000
# 
# 
# END_DESC

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    hundreds = number // 100
    tens = (number % 100) // 10
    ones = number % 10

    res = list()
    if hundreds > 0:
        res.append(FIRST_TEN[hundreds - 1])
        res.append(HUNDRED)

    # tens > 1, ones == 0, e.g. 30
    # tens == 1, ones >= 0, e.g. 18
    # tens > 1, ones > 1, e.g. 23

    if tens > 1 and ones == 0:
        # 30
        res.append(OTHER_TENS[tens - 2])

    if tens == 1 and ones >= 0:
        # 18
        res.append(SECOND_TEN[ones])

    if tens > 1 and ones >= 1:
        # 41
        res.append(OTHER_TENS[tens - 2])
        res.append(FIRST_TEN[ones - 1])

    if tens == 0 and ones > 0:
        # 2
        res.append(FIRST_TEN[ones - 1])

    # print(number, hundreds, tens, ones, res)

    return ' '.join(res)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')