#!/usr/bin/env python3
"""
Advent of Code 2016
Alex Troesch

--- Day 1: No Time for a Taxicab ---

Santa's sleigh uses a very high-precision clock to guide its movements,
and the clock's oscillator is regulated by stars. Unfortunately, the stars have
been stolen... by the Easter Bunny. To save Christmas, Santa needs you to
retrieve all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each
day in the advent calendar; the second puzzle is unlocked when you complete the
first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near",
unfortunately, is as close as you can get - the instructions on the Easter
Bunny Recruiting Document the Elves intercepted start here, and nobody had
time to work them out further.

The Document indicates that you should start at the given coordinates (where
you just landed) and face North. Then, follow the provided sequence: either
turn left (L) or right (R) 90 degrees, then walk forward the given number of
blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you
take a moment and work out the destination. Given that you can only walk on the
street grid of the city, how far is the shortest path to the destination?

For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2
blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.

How many blocks away is Easter Bunny HQ?

--- Part Two ---

Then, you notice the instructions continue on the back of the Recruiting
Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you
visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?
"""


def part1(commands):
    position = (0, 0)
    direction = (0, 1)

    for (turn, dist) in commands:
        direction = change_direction(direction, turn)
        position = (position[0] + direction[0] * dist, position[1] + direction[1] * dist)

    return taxicab_distance(position)


def part2(commands):
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
    file_name = 'input_01.txt'

    with open(file_name) as file:
        input = file.readline().split(',')
        commands = [(cmd.strip()[0], int(cmd.strip()[1:])) for cmd in input]

        print("Part One:", part1(commands))
        print("Part Two:", part2(commands))

