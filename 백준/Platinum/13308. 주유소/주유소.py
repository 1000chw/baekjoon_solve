from collections import defaultdict
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lp = [0] + list(map(int, input().split()))
cities = defaultdict(list)
answer = float('inf')

def goToN(cur, n):
    visited = [float('inf')]*(n+1)
    visited[cur] = 0
    q = [(0, cur)]
    while q:
        cost, v = heappop(q)
        if visited[v] != cost:
            continue
        if v == n:
            continue
        for nv, c in cities[v]:
            if visited[nv] > c + cost:
                visited[nv] = c + cost
                heappush(q, (c + cost, nv))

    return visited


for i in range(m):
    x, y, c = map(int, input().split())
    cities[x].append((y, c))
    cities[y].append((x, c))

times = [[]]
for i in range(1, n):
    timeToN = list(map(lambda x: x * lp[i], goToN(i, n)))
    times.append(timeToN)

timechk = [float('inf')]*(n+1)
def solve(cur, n, cost):
    global answer
    if timechk[cur] > cost:
        timechk[cur] = cost
    else:
        return
    for i in range(1, n):
        if lp[i] < lp[cur] and timechk[i] > cost + times[cur][i]:
            solve(i, n, cost + times[cur][i])
    answer = min(answer, cost + times[cur][n])

solve(1, n, 0)
print(answer)
