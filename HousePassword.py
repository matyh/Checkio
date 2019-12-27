import re


def checkio(data: str) -> bool:
    length = len(data)
    lower = 0
    upper = 0
    digit = 0
    if length < 10:
        return False
    for i in data:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isdigit():
            digit += 1
    if lower > 0 and upper > 0 and digit > 0:
        return True


def checkio(data: str) -> bool:
    return len(data) > 9 and all(re.search(p, data) for p in ('[A-Z]', '\d', '[a-z]'))


