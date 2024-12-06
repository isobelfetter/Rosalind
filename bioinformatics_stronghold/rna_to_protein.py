#!/usr/bin/env python3

import sys, re

rna = sys.argv[1]

codon_list = re.findall(r'\w{3}', rna)

translation_table = {
    'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAU':'N', 'AAC':'N',
    'GAU':'D', 'GAC':'D',
    'UGU':'C', 'UGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAU':'H', 'CAC':'H',
    'AUU':'I', 'AUC':'I', 'AUA':'I',
    'UUA':'L', 'UUG':'L', 'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
    'AAA':'K', 'AAG':'K',
    'AUG':'M',
    'UUU':'F', 'UUC':'F',
    'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 'AGU':'S', 'AGC':'S',
    'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'UGG':'W',
    'UAU':'Y', 'UAC':'Y',
    'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
    'UAA':'*', 'UAG':'*', 'UGA':'*'
}

peptide_list = []
for codon in codon_list:
        amino_acid = translation_table[codon]
        peptide_list.append(amino_acid)

peptide = "".join(peptide_list)
short_peptide = re.search(r'^\w+', peptide)
print(short_peptide.group(0))