#!/usr/bin/env checkio --domain=py run pawn-brotherhood

# https://py.checkio.org/mission/pawn-brotherhood/

# 
# END_DESC

def my_defenses(pawn):
    # file -> column (a-h)
    # rank -> row (1-9)
    file = pawn[0]
    rank = int(pawn[1])

    if rank == 0:
        return []
    else:
        _rank = rank - 1

    # _file = [file]
    _file = []
    if file != 'a':
        _file.append(chr(ord(file) - 1))
    if file != 'h':
        _file.append(chr(ord(file) + 1))

    return ['{}{}'.format(f, _rank) for f in _file]


def safe_pawns(pawns: set) -> int:
    return len([pawn for pawn in pawns if pawns & set(my_defenses(pawn))])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({ "b4", "d4", "f4", "c3", "e3", "g5", "d2" }) == 6
    assert safe_pawns({ "b4", "c4", "d4", "e4", "f4", "g4", "e5" }) == 1
    assert safe_pawns({ "a1", "a2", "a3", "a4", "h1", "h2", "h3", "h4" }) == 0
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
