#!/usr/bin/env python3

import sys

input_file = sys.argv[1]

fasta_dict = {}

with open(input_file, "r") as read_file:
  for line in read_file:
    line = line.rstrip()
    if ">" in line:
      line = line.replace(">","")
      fasta_dict[line] = ""
      seq_name = line
      line_partial = ""
    else:
      line_partial += line
      fasta_dict[seq_name] = line_partial

GC_dict = {}
for seq in fasta_dict:
  dna = fasta_dict[seq]
  length = len(dna)
  G_count = dna.count('G')
  C_count = dna.count('C')
  GC_count = G_count + C_count
  GC_content = 100*GC_count / length
  GC_dict[seq] = GC_content

sorted_dict = sorted(GC_dict, key=GC_dict.get, reverse=True)
print(sorted_dict[0])
print(f'{GC_dict[sorted_dict[0]]:.10}')


