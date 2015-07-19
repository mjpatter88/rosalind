#!/usr/bin/python3
import collections

# Project Rosalind: CONS - Consensus and Profile

# Parse input file for the DNA strings
with open('CONS_dataset.txt', 'r') as df:
    # split into strings ignoring the sample name and removing new lines
    dna_strings = [dna[dna.find("\n"):].replace('\n', '').replace('\r', '') for dna in df.read().split('>') if len(dna) > 0]
# print(dna_strings, end="\n\n")

# Zip will return tuples of all the first elements in each string, second elements in each string, etc.
# Map will create a Counter for each of these returned tuples
prof_matrix = list(map(collections.Counter, zip(*dna_strings)))

# Print concensus string
# Is looping pythonic here? I'm still not sure...
for col in prof_matrix:
    print(col.most_common(1)[0][0], end="")
print()

# Print profile matrix
for base in "ACGT":
    print(base + ": ", end="")
    # Map will apply the lambda function to each item (counter) in prof_matrix
    # Join will create a string from all the values, which is then printed
    print(" ".join(map(lambda counter: str(counter[base]), prof_matrix)))

#for counter in prof_matrix:
#    print(counter['A'], end=" ")

