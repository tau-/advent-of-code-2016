#!/usr/bin/env python3
"""
Advent of Code 2016
Alex Troesch
"""


def supports_tls(address):
    good_abba = 0
    poor_abba = 0

    for section in address.split('['):
        subsections = section.split(']')
        if len(subsections) == 1:
            good_abba += scan_for_abba(subsections[0])
        else:
            poor_abba += scan_for_abba(subsections[0])
            for subsection in subsections[1:]:
                good_abba += scan_for_abba(subsection)
    return good_abba > 0 and poor_abba == 0


def scan_for_abba(string):
    abba = 0
    for i in range(len(string) - 3):
        substr = string[i:i + 4]
        if (substr[0] == substr[3] and 
            substr[1] == substr[2] and 
            substr[0] != substr[1]):
           abba += 1
    return abba


def supports_ssl(address):
    aba_list = []
    bab_list = []

    for section in address.split('['):
        subsections = section.split(']')
        if len(subsections) == 1:
            aba_list += scan_for_aba(subsections[0])
        else:
            babs = scan_for_aba(subsections[0])
            for bab in babs:
                matching_aba = bab[1] + bab[0] + bab[1]
                bab_list.append(matching_aba)
            for subsection in subsections[1:]:
                aba_list += scan_for_aba(subsection)
    for aba in aba_list:
        if aba in bab_list:
            return True
    return False


def scan_for_aba(string):
    aba_list = []
    for i in range(len(string) - 2):
        substr = string[i:i + 3]
        if substr[0] == substr[2] and substr[0] != substr[1]:
            aba_list.append(substr)
    return aba_list


if __name__ == '__main__':
    file_name = 'input/07.txt'

    with open(file_name) as file:
        addresses = [line.strip() for line in file.readlines()]

        part1 = sum([supports_tls(address) for address in addresses])
        part2 = sum([supports_ssl(address) for address in addresses])
        print('Part One:', part1)
        print('Part Two:', part2)

