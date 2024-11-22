#!/usr/bin/env python3

import sys

input_string = sys.argv[1]
input_list = input_string.split()
dictionary = {}

for word in input_list:
    if word not in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word] += 1

for word in dictionary:
    print(word, dictionary[word])

