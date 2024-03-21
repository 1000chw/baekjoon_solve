from collections import defaultdict
import sys
sys.setrecursionlimit(10000000)
n, s = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
dl, dr = defaultdict(int), defaultdict(int)
mid = n//2
for i in range(mid):
    if nums[i] < 0:
        for key in sorted(dl.keys()):
            dl[key+nums[i]] += dl[key]
    else:
        for key in sorted(dl.keys(), reverse=True):
            dl[key+nums[i]] += dl[key]
    dl[nums[i]] += 1
for i in range(mid, n):
    if nums[i] < 0:
        for key in sorted(dr.keys()):
            dr[key + nums[i]] += dr[key]
    else:
        for key in sorted(dr.keys(), reverse=True):
            dr[key + nums[i]] += dr[key]
    dr[nums[i]] += 1

answer += dl[s] + dr[s]

for key in dl.keys():
    answer += dl[key]*dr[s-key]

print(answer)
