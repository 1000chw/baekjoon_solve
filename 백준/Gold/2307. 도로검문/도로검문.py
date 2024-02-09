import sys
from collections import defaultdict
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
edges = defaultdict(list)

def dijk_path():
    res = [INF] * (N+1)
    visited = [False] * (N+1)
    before = [0] * (N+1)
    res[1] = 0
    pq = [(0, 1)]
    while pq:
        t, x = heappop(pq)
        if not visited[x]:
            visited[x] = True
            for n, nt in edges[x]:
                if not visited[n] and res[n] > t + nt:
                    before[n] = x
                    res[n] = t + nt
                    heappush(pq, (t+nt, n))
    path = [N]
    while True:
        if before[path[-1]] == 0:
            break
        path.append(before[path[-1]])
    path.reverse()
    return path, res[N]

def dijk(a, b):
    res = [INF] * (N+1)
    visited = [False] * (N+1)
    res[1] = 0
    pq = [(0, 1)]
    while pq:
        t, x = heappop(pq)
        if not visited[x]:
            visited[x] = True
            for n, nt in edges[x]:
                if (x, n) == (a, b) or (n, x) == (a, b):
                    continue
                if not visited[n] and res[n] > t + nt:
                    res[n] = t + nt
                    heappush(pq, (t+nt, n))
    return res[N]


for _ in range(M):
    a, b, t = map(int, input().split())
    edges[a].append((b, t))
    edges[b].append((a, t))
path, time = dijk_path()
answer = 0
for i in range(len(path) - 1):
    NT = dijk(path[i], path[i+1]) - time
    answer = max(answer, NT)
    if answer == INF:
        break
if answer == INF:
    print(-1)
else:
    print(answer)
