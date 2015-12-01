def conjunction(a, b):
    return a and b


def disjunction(a, b):
    return a or b


def implication(a, b):
    return (not a) or b


def exclusive(a, b):
    return (a and (not b)) or (b and (not a))


def equivalence(a, b):
    return a == b


OPERATIONS = {"conjunction": conjunction,
              "disjunction": disjunction,
              "implication": implication,
              "exclusive": exclusive,
              "equivalence": equivalence}


def boolean(x, y, operation):
    return OPERATIONS[operation](x, y)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
