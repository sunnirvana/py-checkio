#!/usr/bin/env checkio --domain=py run ground-for-the-house

# https://py.checkio.org/mission/ground-for-the-house/

# 
# END_DESC

def house(plan):
    plan_list = plan.split()
    left, right, top, bottom = None, None, None, None
    for i in range(len(plan_list)):
        if '#' in plan_list[i]:
            bottom = i
            if top == None:
                top = i
            if left == None or left > plan_list[i].find('#'):
                left = plan_list[i].find('#')
            if right == None or right <  plan_list[i].rfind('#'):
                right = plan_list[i].rfind('#')
    if top == None:
        return 0
    return (bottom - top + 1) * (right - left + 1)

if __name__ == '__main__':
    print("Example:")
#     print(house('''
# 0000000
# ##00##0
# ######0
# ##00##0
# #0000#0
# '''))
    print(house('''
0000##0000
#000##000#
##########
##000000##
0########0
    '''))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12

    print("Coding complete? Click 'Check' to earn cool rewards!")
