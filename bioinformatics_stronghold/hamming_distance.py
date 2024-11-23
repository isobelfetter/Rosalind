#!/usr/bin/env python3

import sys

dna1 = sys.argv[1]
dna2 = sys.argv[2]

length = len(dna1)

mut = 0

for i in range(length):
    if dna1[i] != dna2[i]:
        mut +=1

print(mut)