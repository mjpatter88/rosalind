# Rosalind problem #1 : DNA


# Read the dataset
with open('DNA_dataset.txt', 'r') as df:
    data = df.read()
print(data)

# Create a dictionary for the values
counts = {'A':0, 'C':0, 'G':0, 'T':0}

# Update the counts
for char in data:
    if char == '\n':
        break
    counts[char] = counts[char] + 1

# Print out the answer in the required format
for key, value in counts.items():
    print("{0} ".format(value), end="")
