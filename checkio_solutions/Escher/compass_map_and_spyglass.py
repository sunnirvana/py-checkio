#!/usr/bin/env checkio --domain=py run compass-map-and-spyglass

# https://py.checkio.org/mission/compass-map-and-spyglass/

# 
# END_DESC

def distance(pos1, pos2):
    return max(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1]))

def navigation(seaside):
    #replace this for solution
    y, m, s, c = None, None, None, None
    for i in range(len(seaside)):
        for j in range(len(seaside[i])):
            if seaside[i][j] == 'C':
                c = (i, j)
            elif seaside[i][j] == 'M':
                m = (i, j)
            elif seaside[i][j] == 'S':
                s = (i, j)
            elif seaside[i][j] == 'Y':
                y = (i, j)
    return distance(y, c) + distance(y, s) + distance(y, m)

if __name__ == '__main__':
    print("Example:")
    print(navigation([['Y', 0, 0, 0, 'C'],
                      [ 0,  0, 0, 0,  0],
                      [ 0,  0, 0, 0,  0],
                      ['M', 0, 0, 0, 'S']]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert navigation([['Y', 0, 0, 0, 'C'],
                       [ 0,  0, 0, 0,  0],
                       [ 0,  0, 0, 0,  0],
                       ['M', 0, 0, 0, 'S']]) == 11

    assert navigation([[ 0,  0, 'C'],
                       [ 0, 'S', 0],
                       ['M','Y', 0]]) == 4

    assert navigation([[ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'M', 0, 'S', 0],
                       [ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'C', 0,  0,  0],
                       [ 0, 'Y',0,  0,  0,  0,  0],
                       [ 0,  0, 0,  0,  0,  0,  0]]) == 9
    print("Coding complete? Click 'Check' to earn cool rewards!")