# Project Rosalind Problem 2: RNA


with open('RNA_dataset.txt', 'r') as df:
    data = df.read()
print(data)

print(data.replace("T", "U"))
