#!/usr/bin/env python3
import os
import subprocess
from argparse import ArgumentParser


def solve_day(day):
    script = 'src/adventofpython/day_{:0>2}.py'.format(day)
    input = 'input/{:0>2}.txt'.format(day)
    if os.path.isfile(input) and os.path.isfile(script):
        print('Day {:0>2}'.format(day))
        print('------')
        return subprocess.run(
            ['python3', script],
            stdout=subprocess.PIPE,
            universal_newlines=True)
    else:
        print('Invalid day {:0>2}'.format(day))


def solve(day):
    days = range(1, 26)
    if day == 0:
        for number in days:
            print(solve_day(number).stdout)
    elif day in days:
        print(solve_day(day).stdout)
    else:
        print('Invalid day {:0>2}'.format(day))


if __name__ == '__main__':
    parser = ArgumentParser(prog='solve.py',
        description='Solves the problem from Advent of Code 2016 for a given day')
    parser.add_argument('day', default=0, type=int, nargs='?', help='the day to solve')
    args = parser.parse_args()

    solve(args.day)

