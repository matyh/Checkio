#!/usr/bin/env checkio --domain=py run humpty-dumpty

# END_DESC
import math


def checkio(height, width):
    a = width / 2
    c = height / 2
    if height == width:
        S = 4 * math.pi * c ** 2
        V = 4 / 3 * math.pi * c ** 3
    else:
        V = 4 * math.pi / 3 * a ** 2 * c
        if height > width:
            e = math.sqrt(1 - (a ** 2 / c ** 2))
            S = 2 * math.pi * a ** 2 * (1 + c / a / e * math.asin(e))
        elif height < width:
            e = math.sqrt(1 - (c ** 2 / a ** 2))
            S = 2 * math.pi * a ** 2 * (1 + (1 - e ** 2) / e * math.atanh(e))
    return [round(V, 2), round(S, 2)]


# checkio(4, 2) == [8.38, 21.48]
# checkio(2, 2) == [4.19, 12.57]
# checkio(2, 4) == [16.76, 34.69]

print(checkio(4, 2))
print(checkio(2, 2))
print(checkio(2, 4))
print(checkio(10, 10))