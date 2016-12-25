#!/usr/bin/env python3
"""
Advent of Code 2016
Alex Troesch
"""


def decompress(data):
    output = ''

    mode = 'scan'
    while data:
        if mode == 'scan':
            try:
                index = data.index('(')
                mode = 'duplicate'
            except:
                index = len(data)

            output += data[:index]
            data = data[index + 1:]

        elif mode == 'duplicate':
            try:
                index = data.index(')')
                mode = 'scan'
            except:
                index = len(data)

            window, repeat = map(int, data[:index].split('x'))
            data = data[index + 1:]
            output += data[:window] * repeat
            data = data[window:]

    return output


def decompressed_length(data, multiplier=1):
    def contains_marker(data):
        try:
            return 'x' in data[data.index('('):data.index(')')+1][1:-1]
        except:
            return False

    def extract_marker(data):
        start, end = [data.index('('), data.index(')')+1]
        return map(int, [start, end] + data[start:end][1:-1].split('x'))

    if contains_marker(data):
        start, end, window, repeat = extract_marker(data)
        return (decompressed_length(data[:start], multiplier) + 
            decompressed_length(data[end:end+window], repeat * multiplier) +
            decompressed_length(data[end+window:], multiplier))
    else:
        return len(data) * multiplier


if __name__ == '__main__':
    file_name = 'input/09.txt'

    with open(file_name) as file:
        input = file.readline().strip()

        print('Part One:', len(decompress(input)))
        print('Part Two:', decompressed_length(input))

