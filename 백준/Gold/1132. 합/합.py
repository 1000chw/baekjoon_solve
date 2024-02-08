import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
nums = [input().strip()[::-1] for _ in range(n)]
chk_zero = defaultdict(int)
sum_idx = defaultdict(int)
for num in nums:
    ln = len(num)
    for i in range(ln):
        sum_idx[num[i]] += 10**i
        chk_zero[num[i]] += 0
        if i == ln-1:
            chk_zero[num[i]] = 1

s, zero_alpha = float('inf'), ''
if len(chk_zero.keys()) == 10:
    for key in chk_zero.keys():
        if not chk_zero[key] and s > sum_idx[key]:
            s = sum_idx[key]
            zero_alpha = key

res = 0
alpha = list(sum_idx.keys())
alpha.sort(key=lambda x: sum_idx[x], reverse=True)
N = 9
for a in alpha:
    if a == zero_alpha:
        continue
    res += N*sum_idx[a]
    N -= 1
print(res)
