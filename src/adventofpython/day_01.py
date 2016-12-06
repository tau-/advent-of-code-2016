#!/usr/bin/env python3
"""
Advent of Code 2016
Alex Troesch
"""


def find_distance_to_last_position(commands):
    position = (0, 0)
    direction = (0, 1)

    for (turn, dist) in commands:
        direction = change_direction(direction, turn)
        position = (position[0] + direction[0] * dist, position[1] + direction[1] * dist)

    return taxicab_distance(position)


def find_distance_to_revisited_position(commands):
    position = (0, 0)
    direction = (0, 1)

    visited = {}
    revisited = None
    visited[position] = True

    for (turn, dist) in commands:
        direction = change_direction(direction, turn)
        for _ in range(dist):
            position = (position[0] + direction[0], position[1] + direction[1])
            if position in visited and revisited is None:
                return taxicab_distance(position)
            else:
                visited[position] = True

    return -1


def taxicab_distance(pos):
    return sum(abs(x) for x in pos)


def change_direction(dir, turn):
    if turn == 'R':
        return (dir[1], -dir[0])
    elif turn == 'L':
        return (-dir[1], dir[0])


if __name__ == '__main__':
    file_name = 'input/01.txt'

    with open(file_name) as file:
        input = file.readline().split(',')
        commands = [(cmd.strip()[0], int(cmd.strip()[1:])) for cmd in input]

        print('Part One:', find_distance_to_last_position(commands))
        print('Part Two:', find_distance_to_revisited_position(commands))

