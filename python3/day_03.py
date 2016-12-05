#!/usr/bin/env python3
"""
Advent of Code 2016
Alex Troesch

--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways
and office furniture that makes up this part of Easter Bunny HQ. This must be a
graphic design department; the walls are covered in specifications for
triangles.

Or are they?

The design document gives the side lengths of each triangle it describes,
but... 5 10 25? Some of these aren't triangles. You can't help but mark the
impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining
side. For example, the "triangle" given above is impossible, because 5 + 10 is
not larger than 25.

In your puzzle input, how many of the listed triangles are possible?

--- Part Two ---

Now that you've helpfully marked up their design documents, it occurs to you
that triangles are specified in groups of three vertically. Each set of three
numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds
digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603

In your puzzle input, and instead reading by columns, how many of the listed
triangles are possible?
"""


def count_possible(triangles):
    return sum([1 if is_possible(a, b, c) else 0 for (a, b, c) in triangles])


def is_possible(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)


if __name__ == '__main__':
    file_name = 'input_03.txt'

    with open(file_name) as file:
        triangles = [tuple([int(side) for side in line.split()]) for line in file.readlines()]

        triangles_col = [tuple([triangles[i+k][j] for k in range(3)])
                         for i in range(0,len(triangles),3) for j in range(3)] 

        print('Part One:', count_possible(triangles))
        print('Part Two:', count_possible(triangles_col))

