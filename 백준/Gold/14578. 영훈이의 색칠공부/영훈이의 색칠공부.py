MOD = 1000000007
n = int(input())

d = [0] * (n+1)
d[0] = 1
f = 1

for i in range(2, n+1):
    f = (f * i) % MOD
    d[i] = ((i-1)*(d[i-1] + d[i-2])) % MOD

print((d[n] * f) % MOD)