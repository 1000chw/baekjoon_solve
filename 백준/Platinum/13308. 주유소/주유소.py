from collections import defaultdict
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lp = [0] + list(map(int, input().split()))
cities = defaultdict(list)
answer = float('inf')


def goToN():
    visited = [[float('inf')]*(n+1) for _ in range(2501)]
    visited[lp[1]][1] = 0
    q = [(0, 1, lp[1])]
    while q:
        cost, v, pr = heappop(q)
        if visited[pr][v] != cost:
            continue
        if v == n:
            print(cost)
            return
        pr = min(pr, lp[v])
        for nv, c in cities[v]:
            nc = c * pr + cost
            if visited[pr][nv] > nc:
                visited[pr][nv] = nc
                heappush(q, (nc, nv, pr))


for i in range(m):
    x, y, c = map(int, input().split())
    cities[x].append((y, c))
    cities[y].append((x, c))


goToN()