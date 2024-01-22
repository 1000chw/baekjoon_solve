import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ms = list(map(int, input().split()))
c = list(map(int, input().split()))
active_mem = sum(ms) - m

nap = [0]*(active_mem+1)

for i in range(ms[0], active_mem+1):
    nap[i] = c[0]

for i in range(1, n):
    for j in range(active_mem, ms[i]-1, -1):
        nap[j] = max(nap[j], nap[j-ms[i]] + c[i])

print(sum(c) - nap[-1])