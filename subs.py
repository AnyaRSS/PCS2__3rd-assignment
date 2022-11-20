f = open('rosalind_subs.txt')
file = f.read()
s , t = file.splitlines()
#s = 'GATATATGCATATACTT'
#t = 'ATAT'
res = ''
x = 0
while x < len(s):
    if s[x] == t[0]:
        if s[x : x + len(t)] == t:
            res += str(x+1) + ' '
    x += 1
print(res)
f.close()