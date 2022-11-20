from Bio import SeqIO
import numpy
#for every seq in the file I put its nucleotides in a list(sequence) and then the lists of nucleotides in the matix "sequences"
sequences = []
for s in SeqIO.parse('rosalind_cons.txt', 'fasta'):
     sequence = []
     for nucleotide in s.seq:
          sequence.extend(nucleotide)
     sequences.append(sequence)

#I create a matix of zeros and sum up the bases in all the sequences (vertically), creating a profile matrix for the sequences
profile = numpy.zeros((4, len(sequences[0])), dtype=numpy.int)
for i,line in enumerate(sequences):
     for j, nucleotide in enumerate(line):
          if nucleotide == 'A':
               profile[0][j] += 1
          elif nucleotide == 'C':
               profile[1][j] += 1
          elif nucleotide == 'G':
               profile[2][j] += 1
          elif nucleotide == 'T':
               profile[3][j] += 1 

#I zip all the profile lines and add to an empty string the nucleotide that appears the most in the analized position
consensus = ''
for A,C,G,T in zip(profile[0],profile[1],profile[2],profile[3]):
     if A >= C and A >= G and A >= T:                           
          consensus += 'A'                                      
     elif C >= A and C >= G and C >= T:                         
          consensus += 'C'                                      
     elif G >= A and G >= C and G >= T:                         
          consensus += 'G'                                      
     elif T >= A and T >= C and T >= G:                         
          consensus += 'T'                                      

print(consensus)                                   
print('A: ' + ' '.join(str(e) for e in profile[0]))
print('C: ' + ' '.join(str(e) for e in profile[1]))
print('G: ' + ' '.join(str(e) for e in profile[2]))
print('T: ' + ' '.join(str(e) for e in profile[3]))