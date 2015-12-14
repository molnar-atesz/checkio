import math
from string import ascii_lowercase


def get_multiplier(digit_value):
    if digit_value.isdigit():
        return int(digit_value)
    else:
        return int(10+ascii_lowercase.index(digit_value))


def checkio(str_number, radix):
    summa = 0
    digit = 0
    for digit_value in reversed(str_number.lower()):
        multiplier = get_multiplier(digit_value)
        if (radix < 11 and digit_value.isalpha()) or multiplier >= radix:
            return -1

        summa += multiplier * math.pow(radix, digit)
        digit += 1
    return summa

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"
