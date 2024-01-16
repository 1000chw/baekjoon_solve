import sys
from queue import PriorityQueue
from collections import defaultdict
input = sys.stdin.readline
INF = float("inf")

n, m, k = map(int, input().split())
d = [[INF]*(n+1) for _ in range(k+1)]
visited = [[False]*(n+1) for _ in range(k+1)]
edges = defaultdict(list)
pq = PriorityQueue()

for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))
for i in range(k+1):
    d[i][1] = 0
pq.put((0, 0, 1))

while pq.qsize():
    dist, cnt, cur = pq.get()
    if visited[cnt][cur]:
        continue
    visited[cnt][cur] = True
    for next_edge in edges[cur]:
        next_node, next_dist = next_edge
        next_dist = max(dist, next_dist)
        if not visited[cnt][next_node] and next_dist < d[cnt][next_node]:
            d[cnt][next_node] = next_dist
            pq.put((next_dist, cnt, next_node))
        if cnt < k:
            if not visited[cnt+1][next_node] and dist < d[cnt+1][next_node]:
                d[cnt+1][next_node] = dist
                pq.put((dist, cnt+1, next_node))

res = min([d[i][n] for i in range(k+1)])
if res == INF:
    print(-1)
else:
    print(res)
