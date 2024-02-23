import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
nums = tuple(map(int, input().split()))
p = {per: 0.0 for per in permutations(range(1, n+1))}

for key in sorted(p.keys()):
    a = cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if key[i] < key[j]:
                continue
            key1 = list(key)
            key1[i], key1[j] = key[j], key[i]
            key1 = tuple(key1)
            a += p[key1] + 1
            cnt += 1
    if cnt:
        p[key] = a / cnt
    if key == nums:
        break
print(p[nums])
