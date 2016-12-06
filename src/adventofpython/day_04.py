#!/usr/bin/env python3
"""
Advent of Code 2016
Alex Troesch
"""


from collections import Counter
from string import ascii_lowercase


def find_northpole(rooms):
    for room in rooms:
        if is_valid(room):
            (name, id, checksum) = room
            if shift_cypher(name, int(id)).count('northpole') > 0:
                return id


def shift_cypher(txt, rot):
    alphabet = ascii_lowercase
    shifted_alphabet = alphabet[rot%26:] + alphabet[:rot%26]
    table = str.maketrans(alphabet, shifted_alphabet)
    
    return txt.translate(table)


def is_valid(room):
    (name, id, checksum) = room
    name = name.replace(' ','')
    letters = sorted(Counter(name).most_common(), key=lambda x: (-x[1], x[0]))
    letters = [letter[0] for letter in letters]
    key = ''.join(letters[:5])

    return int(id) if key == checksum else 0


if __name__ == '__main__':
    file_name = 'input/04.txt'

    with open(file_name) as file:
        rooms = [line.strip().split('-') for line in file.readlines()]
        rooms = [[' '.join(room[:-1])] + room[-1].rstrip(']').split('[') for room in rooms]
        rooms = [tuple(room) for room in rooms]

        print('Part One:', sum([is_valid(room) for room in rooms]))
        print('Part Two:', find_northpole(rooms))

