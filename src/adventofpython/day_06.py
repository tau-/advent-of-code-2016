#!/usr/bin/env python3
"""
Advent of Code 2016
Alex Troesch
"""


from collections import Counter


def find_most_common_by_column(input, index):
    cols = [[y[i] for y in input] for i in range(min([len(y) for y in input]))]
    letters = [Counter(col).most_common()[index] for col in cols]
    return ''.join([letter[0] for letter in letters])


if __name__ == '__main__':
    file_name = 'input/06.txt'

    with open(file_name) as file:
        input = [line.strip() for line in file.readlines()]

        print('Part One:', find_most_common_by_column(input, 0))
        print('Part Two:', find_most_common_by_column(input, -1))

