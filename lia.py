import math
f = open('rosalind_lia.txt')
arr = f.read().split()
#arr = '7 36'
k = int(arr[0]) 
N = int(arr[1])
population = 2**k
probability = 0
for x in range(N, population+1):
    p = (math.factorial(population) / (math.factorial(x) * math.factorial(population-x))) * (0.25**x) * (0.75**(population - x)) 
    probability += p
print(probability)
f.close()