#!/usr/bin/env python3
"""
Advent of Code 2016
Alex Troesch
"""


from hashlib import md5


def find_password_one(room):
    password = []
    salt = 0
    while len(password) < 8:
        hash = md5(room + str(salt).encode('ascii')).hexdigest()
        if hash.startswith('00000'):
            password.append(hash[5])
            print(password)
        salt += 1

    return ''.join(password)


def find_password_two(room):
    password = ['_'] * 8
    salt = 0
    while '_' in password:
        hash = md5(room + str(salt).encode('ascii')).hexdigest()
        if hash.startswith('00000'):
            pos = int(hash[5], 16)
            val = hash[6]
            if pos in range(8) and password[pos] == '_':
                password[pos] = val
                print(password)
        salt += 1

    return ''.join(password)


if __name__ == '__main__':
    file_name = 'input/05.txt'

    with open(file_name) as file:
        room = file.readline().strip()

        print('Finding Passwords for Room:', room)
        print()
        pwd1 = find_password_one(room.encode('ascii'))
        print()
        pwd2 = find_password_two(room.encode('ascii'))
        print()
        print('Part One:', pwd1)
        print('Part Two:', pwd2)

