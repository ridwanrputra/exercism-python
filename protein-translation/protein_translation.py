from textwrap import wrap

Methionine = ['AUG']
Phenylalanine =['UUU','UUC']
Leucine = ['UUA'], ['UUG']
Serine = ['UCU'], ['UCC'], ['UCA'], ['UCG']
Tyrosine = ['UAU'], ['UAC']
Cysteine = ['UGU'], ['UGC']
Tryptophan = ['UGG']
STOP  = ['UAA', 'UAG', 'UGA']


def proteins(strand):
    return wrap(strand,3)

print(proteins("UGGUGUUAUUAAUGGUUU"))
