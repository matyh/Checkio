#!/usr/bin/env checkio --domain=py run house-password

# 
# END_DESC

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

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")