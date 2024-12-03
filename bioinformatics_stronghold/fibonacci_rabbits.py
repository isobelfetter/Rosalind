#!/usr/bin/env python3

import sys

month = int(sys.argv[1])

litter = int(sys.argv[2])

newborn = 1
juvenile = 0
adult = 0
for i in range(month-1):
    adult += juvenile
    juvenile = newborn
    newborn = adult * litter
    total = newborn + adult + juvenile

print(f'total: {total}')