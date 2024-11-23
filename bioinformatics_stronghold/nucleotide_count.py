#!/usr/bin/env python3

import sys

dna = sys.argv[1]

A = dna.count('A')
C = dna.count('C')
G = dna.count('G')
T = dna.count('T')

print(A,C,G,T)