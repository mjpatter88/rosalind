#!/usr/bin/python3

# Project Rosalind: Finding a Motif in DNA

with open("SUBS_dataset.txt", 'r') as df:
    s1, s2 = df.read().split()[0:2]
print(s1)
print(s2)

index = s1.find(s2)
while index != -1:
    print(index+1, end=" ")
    index = s1.find(s2, index+1)
