#!/usr/bin/env python3

import regex as re

line_count = 0

with open('motif.txt', 'r') as read_file:
    for line in read_file:
        line = line.rstrip()
        line_count += 1
        if line_count == 1:
            dna = line
        elif line_count == 2:
            motif = line

loc_list = []
for found in re.finditer(motif, dna, overlapped=True):
    start = found.start(0) + 1
    loc_list.append(start)

print(*loc_list)