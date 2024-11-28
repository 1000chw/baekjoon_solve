import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m, f = map(int, input().split())

graph = []
max_t = 0

for _ in range(m):
    i, j, c, t = map(int, input().split())
    heappush(graph, (c, t, i, j))
    max_t += t

par = []

def find(v):
    if par[v] != v:
        par[v] = find(par[v])
    return par[v]

def union(v1, v2):
    f1, f2 = find(v1), find(v2)
    if f1 == f2:
        return False
    if f1 < f2:
        par[f2] = f1
    else:
        par[f1] = f2
    return True

answer = 0
left, right = 0, 2000000000

for _ in range(500):
    par = [i for i in range(n + 1)]
    mid = (left + right) / 2

    pq = []
    for c, t, i, j in graph:
        heappush(pq,(c + t * mid, i, j))

    cnt = 0
    x = 0
    while pq:
        cx, ci, cj = heappop(pq)
        if not union(ci, cj):
            continue
        x += cx
        cnt += 1
        if cnt == n-1:
            break

    if x <= f:
        left = mid
    else:
        right = mid
    answer = mid

print("{:.4f}".format(answer))
