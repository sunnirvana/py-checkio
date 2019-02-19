#!/usr/bin/env checkio --domain=py run monkey-typing

# https://py.checkio.org/mission/monkey-typing/

# p.quote-source {        float: right;        font-size: 10px;    }
# END_DESC


def count_words(text: str, words: set) -> int:
    text_lc = text.lower()
    matched = 0
    for w in words:
        if w in text_lc:
            matched += 1

    # print(text_lc, words, matched)
    return matched


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", { "how", "are", "you", "hello" }) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", { "banana", "bananas" }) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       { "sum", "hamlet", "infinity", "anything" }) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
