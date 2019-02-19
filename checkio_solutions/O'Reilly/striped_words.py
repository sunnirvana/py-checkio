#!/usr/bin/env checkio --domain=py run striped-words

# https://py.checkio.org/mission/striped-words/

# Our robots are always working to improve their linguistic skills.    For this mission, they research the latin alphabet and its applications.
# 
# The alphabet contains both vowel and consonant letters (yes, we divide the letters).
# Vowels --A E I O U Y
# Consonants --B C D F G H J K L M N P Q R S T V W X Z
# 
# You are given a block of text with different words.     These words are separated by white-spaces and punctuation marks.    Numbers are not considered words in this mission (a mix of letters and digits is not a word either).    You should count the number of words (striped words) where the vowels with consonants are alternating,    that is; words that you count cannot have two consecutive vowels or consonants.    The words consisting of a single letter are not striped -- do not count those. Casing is not significant for this mission.
# 
# Input:A text as a string (unicode)
# 
# Output:A quantity of striped words as an integer.
# 
# Precondition:The text contains only ASCII symbols.
# 0 < len(text) < 105
# 
# 
# END_DESC

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

import re
def checkio(text):
    res = list()
    words = [word.upper() for word in re.split(',|\.| |\?', text) if '.' not in word and len(word) > 1]
    # print(words)
    for word in words:
        odd_letters = word[::2]
        even_letters = word[1::2]
        if word[0] in VOWELS:
            # start with vowel
            if set(odd_letters) & set(VOWELS) == set(odd_letters) and set(even_letters) & set(CONSONANTS) == set(
                    even_letters):
                res.append(word)
        else:
            # start with consonant
            if set(odd_letters) & set(CONSONANTS) == set(odd_letters) and set(even_letters) & set(VOWELS) == set(
                    even_letters):
                res.append(word)

    print(res)
    return len(res)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
