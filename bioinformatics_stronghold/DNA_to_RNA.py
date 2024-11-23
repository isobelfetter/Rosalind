#!/usr/bin/env python3

import sys

dna = sys.argv[1]

rna = dna.replace('T', 'U')

print(rna)