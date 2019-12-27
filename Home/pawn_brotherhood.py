#!/usr/bin/env checkio --domain=py run pawn-brotherhood

# 
# END_DESC

def safe_pawns(pawns):
    coordinates = []
    pawns = list(pawns)

    # transforming letters to number coordinates
    for item in pawns:
        coordinates.append([ord(item[0]) - 96, int(item[1])])

    safe = 0
    for [x, y] in coordinates:
        right = coordinates.count([x + 1, y - 1]) if [x + 1, y - 1] \
            in coordinates else False
        left = coordinates.count([x - 1, y - 1]) if [x - 1, y - 1] \
            in coordinates else False
        if left or right:
            safe += 1
    return safe

# safe_pawns(["a1","b2","c3","d4","e5","f6","g7","h8"])
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1