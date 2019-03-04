#!/usr/bin/env checkio --domain=py run roman-numerals

# https://py.checkio.org/mission/roman-numerals/

# .numeral-table {    margin: auto;    border-collapse: collapse;    text-align: center;  }  .numeral-table * {    border: 1px solid black;    padding: 8px;    width: 50%;  }
# END_DESC

ROMAN_DICT = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def checkio(data):
    # replace this for solution
    thousand_list = ['M', 'MM', 'MMM']
    hundred_list = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    ten_list = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    one_list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

    thousands = data // 1000
    hundreds = (data % 1000) // 100
    tens = (data % 100) // 10
    ones = data % 10
    print(thousands, hundreds, tens, ones)
    res = ''
    if thousands > 0:
        res += thousand_list[thousands - 1]
    if hundreds > 0:
        res += hundred_list[hundreds - 1]
    if tens > 0:
        res += ten_list[tens - 1]
    if ones > 0:
        res += one_list[ones - 1]

    print(res)
    return res


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')