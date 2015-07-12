# Project Rosalind Problem 5: Computing GC Content
import sys

if(len(sys.argv) < 2):
    print("Please provide a dataset file to read from.")
    sys.exit()

filename = sys.argv[1]
with open(filename, 'r') as df:
    data = df.read()
print(data)

# extract the data we need
samples = data.split('>')
samples.remove('') # First element is blank, so remove it

# Use a list of tuples (name, GCcontent)
stats = []

for string in samples:
    numGC = 0
    numTotal = 0
    firstIndex = string.index('\n')
    name = string[0:firstIndex]
    for char in string[firstIndex:]:
        if char == '\n':
            continue
        elif char == 'G' or char == 'C':
            numGC += 1
        numTotal += 1
    stats.append((name, 100*numGC/numTotal)) #GCcontent reported in %

maxGC = stats[0][1]
index = 0
for i, stat in enumerate(stats):
    if stat[1] > maxGC:
        maxGC = stat[1]
        index = i

print("{0}\n{1}".format(stats[index][0], stats[index][1]))

