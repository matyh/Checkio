#!/usr/bin/env checkio --domain=py run roman-numerals

# .numeral-table {    margin: auto;    border-collapse: collapse;    text-align: center;  }  .numeral-table * {    border: 1px solid black;    padding: 8px;    width: 50%;  }
# END_DESC

def checkio(data):
    roman_number = []
    roman_dict = {'ones': ['I', 'V', 'X'], 'tens': ['X', 'L', 'C'],
                  'hundreds': ['C', 'D', 'M'], 'thousands': ['M']}
    helper = ['ones', 'tens', 'hundreds', 'thousands']

    for item in helper:
        matrix = roman_dict[item]
        n = data % 10
        if 0 < n < 4:
            roman_number.insert(0, n * matrix[0])
        elif n == 4:
            roman_number.insert(0, matrix[0] + matrix[1])
        elif 4 < n < 9:
            m = n % 5
            roman_number.insert(0, matrix[1] + m * matrix[0])
        elif n == 9:
            roman_number.insert(0, matrix[0] + matrix[2])
        data //= 10
        if not data:
            break
    roman = ''.join(roman_number)
    return roman

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'