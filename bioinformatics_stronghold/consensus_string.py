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

sequences = []

for fasta in fasta_dict:
  sequences.append(fasta_dict[fasta])

A_dict = {}
C_dict = {}
G_dict = {}
T_dict = {}
consensus_dict = {}


for seq in sequences:
   for i in range(len(seq)):
     A_dict[i] = 0
     C_dict[i] = 0
     G_dict[i] = 0
     T_dict[i] = 0
     consensus_dict[i] = 0
   break

for seq in sequences:
   for i in range(len(seq)):
     if seq[i] == 'A':
       A_dict[i] += 1
     if seq[i] == 'G':
       G_dict[i] += 1
     if seq[i] == 'C':
       C_dict[i] += 1
     if seq[i] == 'T':
       T_dict[i] += 1

consensus = list(range(len(A_dict)))
A_list = ['A:']
C_list = ['C:']
G_list = ['G:']
T_list = ['T:']

for item in consensus_dict:
  if A_dict[item] > consensus_dict[item]:
    consensus_dict[item] = A_dict[item]
    consensus[item] = 'A' 
  if C_dict[item] > consensus_dict[item]:
    consensus_dict[item] = C_dict[item]
    consensus[item] = 'C'
  if G_dict[item] > consensus_dict[item]:
    consensus_dict[item] = G_dict[item]
    consensus[item] = 'G'
  if T_dict[item] > consensus_dict[item]:
    consensus_dict[item] = T_dict[item]
    consensus[item] = 'T'

for index in A_dict:
  A_list.append(A_dict[index])
  C_list.append(C_dict[index])
  G_list.append(G_dict[index])
  T_list.append(T_dict[index])

consensus_string = "".join(consensus)

print(consensus_string)
print(*A_list)
print(*C_list)
print(*G_list)
print(*T_list)