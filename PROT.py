# Project Rosalind: Translating RNA into Protein


# First, read the RNA codon table into a dictionary
with open('PROT_RNAcodonTable.txt', 'r') as ct:
    ct_iter = iter(ct.read().split())
    codon_table = {rna:aa for rna, aa in zip(ct_iter, ct_iter)}
print(codon_table)
# Manually replace "Stop" with "\n" for the three special cases
codon_table["UAA"] = "\n"
codon_table["UAG"] = "\n"
codon_table["UGA"] = "\n"

# Next, read the input
with open('PROT_dataset.txt', 'r') as ds:
    data = ds.read()
print(data)

# Split the input into triplets and iterate over each one
for triplet in map(''.join, zip(*[iter(data)]*3)):
    # print the corresponding amino acid
    print(codon_table[triplet], end="")
