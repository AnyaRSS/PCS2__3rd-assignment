f = open('rosalind_iev.txt')
arr = f.read().split()
AA_AA = int(arr[0])       #prob_domphen = 1
AA_Aa = int(arr[1])       #prob_domphen = 1
AA_aa = int(arr[2])       #prob_domphen = 1
Aa_Aa = int(arr[3])       #prob_domphen = 0.75
Aa_aa = int(arr[4])       #prob_domphen = 0.5
aa_aa = int(arr[5])       #prob_domphen = 0
domphen_offspring = (1*AA_AA + 1*AA_Aa + 1*AA_aa + 0.75*Aa_Aa + 0.5*Aa_aa + 0*aa_aa) * 2
print(domphen_offspring)
f.close()