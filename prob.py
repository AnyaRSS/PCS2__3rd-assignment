import math

f = open('rosalind_prob.txt')
file = f.read().split()
AT = 0
GC = 0
for c in file[0]:
    if c == 'A' or c == 'T':
        AT += 1
    else:
        GC += 1

for number in file[1:]:
    prob_GC = float(number)/2
    prob_AT = (1 - float(number))/2
    probability = math.log10(pow(prob_GC, GC)) + math.log10(pow(prob_AT, AT))
    print(probability, end = " ")
