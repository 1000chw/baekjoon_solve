import sys
from collections import defaultdict
from queue import PriorityQueue
input = sys.stdin.readline
INF = float('inf')

n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]
res = 0
chk = False
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        min_x = float('inf')
        for k in range(n):
            if i == k or j == k:
                continue
            min_x = min(min_x, dist[i][k] + dist[k][j])
        if min_x < dist[i][j]:
            chk = True
            break
        if min_x > dist[i][j]:
            res += dist[i][j]
    if chk:
        break
if chk:
    print(-1)
else:
    print(res // 2)
