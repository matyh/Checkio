#!/usr/bin/env checkio --domain=py run calculate-islands

# The Robots have found a chain of islands in the middle of the Ocean.
# They would like to explore these islands and have asked for your help
# calculating the areas of each island.    They have given you a map of the
# territory. The map is a 2D array, where 0 is water, 1 is land.    An
# island is a group of land cells surround by water.    Cells are connected
# by their edges and corners.    You should calculate the areas for each of
# the islands and return a list of sizes (quantity of cells) in    ascending
# order.    All of the cells outside the map are considered to be water.
# 
# 
# 
# Input:A map as a list of lists with 1 or 0.
# 
# Output:The sizes of island as a list of integers.
# 
# Precondition:0 < len(land_map) < 10
# all(len(land_map[0]) == len(row) for row in land_map)
# any(any(row) for row in land_map)
# 
# 
# END_DESC
from itertools import product
from typing import List


def neighbours(x, y, height, width):
    """
    Generates the list of neighbouring tiles in the map of size height x width
    relative to (x, y) tile including this tile.
    :param int x: x coordinate
    :param int y: y coordinate
    :param int height: height of the map
    :param int width: width of the map
    :return: the list of coordinates neighbouring (x, y) coordinate, included
    :rtype list
    """
    a = [x + i for i in range(-1, 2) if 0 <= x + i <= height]
    b = [y + i for i in range(-1, 2) if 0 <= y + i <= width]
    return list(product(a, b))


def checkio(land_map: List[List[int]]) -> List[int]:
    height = len(land_map)
    width = len(land_map[0])
    # land = [(x, y) for x in range(height) for y in range(width)]
    land = [(x, y) for x in range(height) for y in range(width) if land_map[x][y] == 1]  # only those which are 1

    islands = []
    while land:
        k = land.pop(0)
        count = 1
        n = neighbours(k[0], k[1], height, width)
        while n:
            tile = n.pop(0)
            if tile in land:
                n.extend(neighbours(tile[0], tile[1], height, width))
                land.remove(tile)
                count += 1
        islands.append(count)

    return sorted(islands)


# nice use of enumerate
def checkio2(land_map):
    same_island=lambda l,island:any([(x-l[0])**2+(y-l[1])**2<=2 for x,y in island])
    sizes=[]
    lands=[[i,j] for i,row in enumerate(land_map) for j,land in enumerate(row) if land]
    print (lands)
    while lands:
        #still one island
        island=[lands.pop()]
        old_size,size=0,1
        while old_size!=size:
            old_size=size
            for i,land in enumerate(lands):
                if same_island(land,island):island+=[lands.pop(i)]
            size=len(island)
        sizes+=[size]
    return sorted(sizes)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([[0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 0],
                   [0, 0, 0, 1, 0],
                   [0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0]]))

    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
    print("Coding complete? Click 'Check' to earn cool rewards!")
