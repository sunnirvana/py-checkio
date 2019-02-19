#!/usr/bin/env checkio --domain=py run flatten-list

# https://py.checkio.org/mission/flatten-list/

# 
# END_DESC

def flat_list(array, res=None):
    if res is None:
        res = list()
    if isinstance(array, list):
        for i in array:
            flat_list(i, res)
    else:
        return res.append(array)
    return res


if __name__ == '__main__':
    print(flat_list([1, 2, 3]))
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')