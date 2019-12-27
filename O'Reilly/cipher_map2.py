#!/usr/bin/env checkio --domain=py run cipher-map2

# 
# END_DESC

def recall_password(cipher_grille, ciphered_password):
    original = [[0, 0], [0, 1], [0, 2], [0, 3],
                [1, 0], [1, 1], [1, 2], [1, 3],
                [2, 0], [2, 1], [2, 2], [2, 3],
                [3, 0], [3, 1], [3, 2], [3, 3]
                ]
    rotation = [[0, 3], [1, 3], [2, 3], [3, 3],
                [0, 2], [1, 2], [2, 2], [3, 2],
                [0, 1], [1, 1], [2, 1], [3, 1],
                [0, 0], [1, 0], [2, 0], [3, 0]
                ]
    matrix = []
    # x: row, y: column
    for x, item in enumerate(cipher_grille):
        for y, sign in enumerate(item):
            if sign == 'X':
                matrix.append([x, y])
    # print matrix

    password = ''
    for n in range(0, 4):
        # getting letters
        for k, (x, y) in zip(range(0, 4), matrix):
            password += ciphered_password[x][y]
        # rotation
        for i in range(0, 4):
            matrix[i] = rotation[original.index(matrix[i])]
        matrix.sort()

    return password


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'