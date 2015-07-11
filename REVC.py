# Project Rosalind Problem 3: REVC

with open('REVC_dataset.txt', 'r') as df:
    data = df.read()
print(data)

# Store the complements in a dict for easy use
complements = {'A':'T', 'C':'G', 'G':'C', 'T':'A', '\n':'\n'}
output = ""
for letter in data:
    output = output + complements[letter]

# Remember to reverse the string as we print it (using python slicing)
print(output[::-1])

