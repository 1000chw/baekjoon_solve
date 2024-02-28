import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline

n, k, s = map(int, input().split())
left, right = [], []
for _ in range(n):
    x, p = map(int, input().split())
    if x < s:
        left.append([x, p])
    else:
        right.append([x, p])
left.sort()
right.sort(reverse=True)

answer = 0
ind = 0
last = 0
p = 0
while ind < len(left):
    if left[ind][1] + p >= k:
        left[ind][1] -= k - p
        answer += (s - left[last][0]) * 2
        if left[ind][1]:
            last = ind
        else:
            last = ind + 1
            ind += 1
        p = 0
    else:
        p += left[ind][1]
        ind += 1
if p:
    answer += (s - left[last][0]) * 2

ind = 0
last = 0
p = 0
while ind < len(right):
    if right[ind][1] + p >= k:
        right[ind][1] -= k - p
        answer += (right[last][0] - s) * 2
        if right[ind][1]:
            last = ind
        else:
            last = ind + 1
            ind += 1
        p = 0
    else:
        p += right[ind][1]
        ind += 1
if p:
    answer += (right[last][0] - s) * 2
print(answer)