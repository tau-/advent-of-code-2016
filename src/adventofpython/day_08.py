#!/usr/bin/env python3
"""
Advent of Code 2016
Alex Troesch
"""


display_height = 6
display_width = 50
display = [[0] * display_width for _ in range(display_height)]


def execute_command(command):
    command = command.split()
    command.reverse()

    type = command.pop()
    if type == 'rect':
        (width, height) = tuple([int(dim) for dim in command.pop().split('x')])
        create_rectangle(height, width)
    elif type == 'rotate':
        orientation = command.pop()
        position = int(command.pop().split('=')[-1])
        command.pop()
        shift = int(command.pop())
        if orientation == 'row':
            rotate_row(position, shift)
        elif orientation == 'column':
            rotate_column(position, shift)


def create_rectangle(height, width):
    for row in range(height):
        display[row][:width] = [1] * width


def rotate_row(row, shift):
    display[row] = display[row][-shift:] + display[row][:-shift]


def rotate_column(col, shift):
    col_data = [row[col] for row in display]
    col_data = col_data[-shift:] + col_data[:-shift]
    for row in range(display_height):
        display[row][col] = col_data[row]


def render(display):
    output = []
    for row in display:
        row_buffer = []
        for c in row:
            if c == 0: row_buffer.append(' ')
            if c == 1: row_buffer.append('█')
        output.append(''.join(row_buffer))
    return '\n'.join(output)


if __name__ == '__main__':
    file_name = 'input/08.txt'

    with open(file_name) as file:
        commands = [line.strip() for line in file.readlines()]

        for command in commands:
            execute_command(command)

        print('Part One:', sum([sum(row) for row in display]))
        print('Part Two:\n{}'.format(render(display)))

