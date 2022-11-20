from Bio import SeqIO
max_id = None
max_gc = 0
for line in SeqIO.parse('rosalind_gc.txt', 'fasta'):
    seq = str(line.seq)
    id = str (line.id)
    count = 0
    tot = len(seq)
    for nuc in seq:
        if nuc == 'C' or nuc == 'G':
            count += 1
    perc = (count*100)/tot
    if perc > max_gc:
        max_gc = perc
        max_id = id
print(max_id, max_gc)