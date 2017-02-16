#!/usr/bin/env python3
"""
Advent of Code 2016
Alex Troesch
"""


class Bot(object):
    """A microchip sorting Bot"""
    def __init__(self):
        super(Bot, self).__init__()
        self.value_high = -1
        self.value_low = -1
        self.output_high = None
        self.output_low = None
        print('!')

    def attach_output(self, high, low):
        self.output_high = high
        self.output_low = low
        self.propagate()

    def attach_value(self, value):
        self.value_low = min(self.value_high, value)
        self.value_high = max(self.value_high, value)

    def propagate(self):
        if self.value_high > 0 and self.value_low > 0:
            if self.output_high:
                self.output_high.attach_value(self.value_high)
                self.output_high.propagate()
            if self.output_low:
                self.output_low.attach_value(self.value_low)
                self.output_low.propagate()


def parse_instruction(cmd):
    if cmd[0] == 'bot':
        source = int(cmd[1])
        destination_high = int(cmd[11]) if cmd[10] == 'bot' else None
        destination_low = int(cmd[6]) if cmd[5] == 'bot' else None
        
        print(source, destination_low, destination_high)

        if source not in bots:
            bots[source] = Bot()
        if destination_high not in bots:
            bots[destination_high] = Bot()
        if destination_low not in bots:
            bots[destination_low] = Bot()

        bots[source].attach_output(bots[destination_high], bots[destination_low])
    elif cmd[0] == 'value':
        destination = int(cmd[1])
        value = int(cmd[5])
        print(destination, value)



if __name__ == '__main__':
    file_name = 'input/10.txt'

    with open(file_name) as file:
        input = [line.strip().split() for line in file.readlines()]\

        bots = {}
        for cmd in input:
            parse_instruction(cmd)

        # print(input)

        print('Part One:', None)
        print('Part Two:', None)

