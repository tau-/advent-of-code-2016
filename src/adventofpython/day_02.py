#!/usr/bin/env python3
"""
Advent of Code 2016
Alex Troesch
"""


keypad_square = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]


keypad_diamond = [[None, None, 1,   None, None],
                  [None, 2,    3,   4,    None],
                  [5,    6,    7,   8,    9   ],
                  [None, 'A',  'B', 'C',  None],
                  [None, None, 'D', None, None]]


delta = {'U': (0, -1),
         'D': (0, 1),
         'L': (-1, 0),
         'R': (1, 0)}


def move(pos, dir):
    (x, y) = pos
    (dx, dy) = delta[dir]
    return (x + dx, y + dy)


def bounded_move(pos, dir, area):
    (x, y) = move(pos, dir)

    y = y if y < len(area) else len(area)-1
    y = y if y > -1 else 0
    x = x if x < len(area[y]) else len(area[y])-1
    x = x if x > -1 else 0

    if area[y][x] is None:
        return pos
    else:
        return (x, y)


def find_keycode(commands, starting_position, keypad):
    (x, y) = starting_position
    code = []
    
    for cmd in commands:
        for dir in cmd:
            (x, y) = bounded_move((x, y), dir, keypad)
        code.append(str(keypad[y][x]))
    
    return ''.join(code)


if __name__ == '__main__':
    file_name = 'input/02.txt'

    with open(file_name) as file:
        commands = [line.strip() for line in file.readlines()]

        print('Part One:', find_keycode(commands, (1, 1), keypad_square))
        print('Part Two:', find_keycode(commands, (0, 2), keypad_diamond))

