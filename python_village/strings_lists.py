#!/usr/bin/env python3

import sys

input_file = sys.argv[1]

linenum = 0
with open(input_file, 'r')  as read_file:
    for line in read_file:
        line = line.rstrip()
        linenum += 1
        if linenum == 1:
            s = line
        if linenum == 2:
            a,b,c,d = line.split()
            a = int(a)
            b = int(b)
            c = int(c)
            d = int(d)

slice1 = s[a:b+1]
slice2 = s[c:d+1]
print(slice1,slice2)