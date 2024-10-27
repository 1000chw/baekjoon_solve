import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, d, t = map(int, input().split())
    graph[u].append((v, d, t))
    graph[v].append((u, d, t))

td = [-1] * (n+1)
pq = []

for next_node, d, t in graph[n]:
    heappush(pq, (d-t, next_node))
    td[n] = max(t, td[n])
    td[next_node] = t-d


while len(pq):
    dt, cur = heappop(pq)
    if td[cur] > -dt:
        continue
    if cur == 1:
        break

    for nn, nd, nt in graph[cur]:
        ndt = min(-dt, nt) - nd
        if ndt <= td[nn]:
            continue

        td[nn] = ndt
        heappush(pq, (-ndt, nn))
print(td[1])
