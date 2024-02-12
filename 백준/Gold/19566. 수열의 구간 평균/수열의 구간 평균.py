import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
d = defaultdict(int)
d[0] = 1
res = 0
nums = [0]+list(map(int, input().split()))
prefix = [0]*(n+1)
for i in range(1, n+1):
    prefix[i] = prefix[i-1]+nums[i]
    res += d[prefix[i]-k*i]
    d[prefix[i]-k*i] += 1

print(res)
