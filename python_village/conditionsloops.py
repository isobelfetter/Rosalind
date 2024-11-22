#!/usr/bin/env python3

import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

sum = 0

for number in range(a,b+1):
    if number % 2 == 1:
        sum += number

print(sum)