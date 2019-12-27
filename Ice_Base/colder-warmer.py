#!/usr/bin/env checkio --domain=py run colder-warmer

# Let's play a game of hide and seek. You have been given a map of 10x10
# cells and in one of the cells we've hidden your goal.    You can move to
# and from any cell in the field.    On each move you'll get informed if the
# move places you closer or further away from your goal, compared to your
# previous location.    Your function compiles data about previous steps,
# each step is a list of list, where first and second elements are    your
# coordinates (row and column) and third is the info on how much closer
# you've gotten (colder or warmer) -- "colder" is -1, "warmer" is 1 and
# "same" is 0.    For your measurement of the distance to the goal you
# should use the Euclidean distance. At each step you need to return the
# coordinates for your next step.    If your step places you within the goal
# cell, then you win! You should find the goal within12steps.
#
#
# Input:Information about previous steps as a list of lists.    Each list
# contains coordinates and status alteration (warm, cold same).
# 
# Output:The coordinates of your new move as a list/tuple of two integers.
# 
# Precondition:|map| = 10x10
#
# END_DESC


from typing import List, Dict, Tuple
from math import hypot
from itertools import product, combinations
import random

GOAL = [7, 2]
START = [4, 4]
MAP_SIZE = [10, 10]

remaining: List[Tuple] = []


def checkio(data: List[Tuple]) -> List:
    """
    From the data of previously visited tiles, returns the next possible position
    :param data: previously visited tiles with information whether the
    position is closer, further or at the same distance
    :return: next position
    """
    global remaining

    cx, cy, chint = data[-1]

    if len(data) == 1:
        # initialize the list of possible remaining positions
        remaining = list(product(range(MAP_SIZE[0]),
                                 range(MAP_SIZE[1])))
        remaining.remove((cx, cy))
        new = random.choice(remaining)
        remaining.remove(new)
        return new

    px, py, _ = data[-2]

    for x, y in remaining[:]:
        prev = hypot(px - x, py - y)
        curr = hypot(cx - x, cy - y)
        if (chint == -1 and prev >= curr) or \
                (chint == 0 and prev != curr) or \
                (chint == 1 and prev <= curr):
            remaining.remove((x, y))

    # print(data)
    # draw(MAP_SIZE, remaining)

    new = random.choice(remaining)
    remaining.remove(new)
    return new


def draw(map_size: List, remaining_tiles: List[Tuple]):
    """
    Draws the field with distinct available and unavailable tiles.
    """
    mx, my = map_size

    decimals = my // 10
    reminder = my % 10

    # generate a first line with decimals
    if my > 10:
        first = 24 * ' '
        for i in range(1, decimals):
            first += f'{10 * (str(i) + " ")}'
        first += reminder * f'{decimals} '
        print(first)

    # generate a second line
    line = '0 1 2 3 4 5 6 7 8 9 '
    second = f'{4 * " " + decimals * line + line[0:(2 * reminder)]}'
    print(second)

    lines = []
    skelet = ''
    for x, y in list(product(range(mx), range(my))):
        if (x, y) in remaining_tiles:
            skelet += '| '
        else:
            skelet += '|X'
        if len(skelet) == 2 * my:
            skelet += '|'
            lines.append(skelet)
            skelet = ''

    for i in range(mx):
        print(f'{i:2} {lines[i]}')
    print(2 * '\n')


# print(draw([8, 12], [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]))



if __name__ == '__main__':
    # This part is using only for self-checking and not necessary for
    # auto-testing
    from math import hypot

    MAX_STEP = 20


    def check_solution(func, goal, start):
        prev_steps = [start]
        for step in range(MAX_STEP):
            row, col = func([s[:] for s in prev_steps])
            if [row, col] == goal:
                return True
            # if 10 <= row or 0 > row or 10 <= col or 0 > col:
            #     print("You gave wrong coordinates.")
            #     return False
            prev_distance = hypot(prev_steps[-1][0] - goal[0],
                                  prev_steps[-1][1] - goal[1])
            distance = hypot(row - goal[0], col - goal[1])
            alteration = 0 if prev_distance == distance else (
                1 if prev_distance > distance else -1)
            prev_steps.append([row, col, alteration])
        print("Too many steps")
        return False


    assert check_solution(checkio, [7, 7], [5, 5, 0]), "1st example"
    assert check_solution(checkio, [5, 6], [0, 0, 0]), "2nd example"

# print(checkio([(8, 2, 0), (6, 2, -1)]))
