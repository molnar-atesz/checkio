
def get_save_pawns(pawn):
    cols = ["a", "b", "c", "d", "e", "f", "g", "h"]
    pawn_col = pawn[0]
    pawn_row = pawn[1]
    safe_row = str(int(pawn_row)-1)

    left_safe = cols[cols.index(pawn_col)+1] + safe_row if pawn_col is not "h" else ""
    right_safe = cols[cols.index(pawn_col)-1] + safe_row if pawn_col is not "a" else ""

    return left_safe, right_safe


def safe_pawns(pawns):
    #safe2 = [pawn for pawn in pawns if get_save_pawns(pawn)[0] in pawns or get_save_pawns(pawn)[1] in pawns]

    safe = []
    for pawn in pawns:
        left, right = get_save_pawns(pawn)
        if left in pawns or right in pawns:
            safe.append(pawn)

    return len(safe)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
