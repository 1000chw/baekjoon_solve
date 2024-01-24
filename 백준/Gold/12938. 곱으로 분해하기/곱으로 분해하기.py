import sys
from math import log, sqrt, comb
from collections import defaultdict
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
MOD = 1000000009

N = int(input())
nums = list(map(int, input().split()))
primeN = defaultdict(int)
for num in nums:
    i = 2
    tmp = num
    while tmp > 1:
        if i > sqrt(num):
            primeN[tmp] += 1
            break
        if tmp % i == 0:
            tmp //= i
            primeN[i] += 1
        else:
            i += 1

res = 1
for v in primeN.values():
    res = (res * (comb(v + N - 1, v))) % MOD

print(res)
