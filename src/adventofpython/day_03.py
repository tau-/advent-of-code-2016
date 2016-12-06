#!/usr/bin/env python3
"""
Advent of Code 2016
Alex Troesch
"""


def count_possible(triangles):
    return sum([1 if is_possible(a, b, c) else 0 for (a, b, c) in triangles])


def is_possible(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)


if __name__ == '__main__':
    file_name = 'input/03.txt'

    with open(file_name) as file:
        triangles = [tuple([int(side) for side in line.split()]) for line in file.readlines()]

        triangles_col = [tuple([triangles[i+k][j] for k in range(3)])
                         for i in range(0,len(triangles),3) for j in range(3)] 

        print('Part One:', count_possible(triangles))
        print('Part Two:', count_possible(triangles_col))

