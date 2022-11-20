f = open('rosalind_iprb.txt')
arr = f.read().split()
#arr = 25 28 16
k = int(arr[0])
m = int(arr[1])
n = int(arr[2])
population = k + m + n
total = 4*population*(population-1)
dominant = 4*(k*(k-1)+2*k*m+2*k*n+m*n)+3*m*(m-1)
p = dominant/total
probability = round(p, 5)
print(probability)
f.close()