#!/usr/bin/env python3

import sys

input_file = sys.argv[1]
linenum = 0

with open(input_file, 'r') as read_file, open('output.txt', 'w') as write_file:
    for line in read_file:
        line = line.rstrip()
        linenum += 1
        if linenum % 2 == 0:
            write_file.write(f'{line}\n')

