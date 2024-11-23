#!/usr/bin/env python3

import sys

dna = sys.argv[1]

rev = dna[::-1]

revcomp = rev.replace('A', 't')
revcomp = revcomp.replace('T', 'a')
revcomp = revcomp.replace('C', 'g')
revcomp = revcomp.replace('G', 'c')
revcomp= revcomp.upper()
print(revcomp)