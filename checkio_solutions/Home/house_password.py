#!/usr/bin/env checkio --domain=py run house-password

# https://py.checkio.org/mission/house-password/
# Stephan and Sophia forget about security and use simple passwords for everything.
# Help Nikola develop a password security check module.
# The password will be considered strong enough if
# - its length is greater than or equal to 10 symbols,
# - it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it.
# The password contains only ASCII latin letters or digits.

#
# END_DESC


def checkio(data: str) -> bool:
    has_lowercase = False
    has_uppercase = False
    has_number = False
    if len(data) >= 10:
        for c in data:
            if 'a' <= c <= 'z':
                has_lowercase = True
            if 'A' <= c <= 'Z':
                has_uppercase = True
            if '0' <= c <= '9':
                has_number = True
            if all([has_uppercase, has_lowercase, has_number]):
                return True
            else:
                continue
    return False



# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
