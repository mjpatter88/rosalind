# Project Rosalind: Problem 6: Counting Point Mutations

import sys

if len(sys.argv) < 2:
    print("Please provide a dataset input file.")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, 'r') as df:
    dataLines = df.read().split('\n')
print(dataLines)

dist = 0
for i, j in zip(dataLines[0], dataLines[1]):
    if i != j:
        dist += 1

print(dist)
