import sys
from heapq import heappush, heappop
input = sys.stdin.readline

v, e = map(int, input().split())

cost = [[float('inf'), float('inf')] for _ in range(v+1)]
edge = [[] for _ in range(v+1)]

for _ in range(e):
    x, y, t, k = map(int, input().split())
    edge[x].append((y, t, k))
    edge[y].append((x, t, k))

cost[1][1] = 0

pq = [(0, 1, 1)]

while len(pq):
    c, eat, x = heappop(pq)

    if cost[x][eat] < c:
        continue

    for next_x, next_c, next_k in edge[x]:
        if eat == 1:
            if cost[next_x][0] > c + next_c - next_k:
                cost[next_x][0] = c + next_c - next_k
                heappush(pq, (cost[next_x][0], 0, next_x))

        if cost[next_x][eat] > c + next_c:
            cost[next_x][eat] = c + next_c
            heappush(pq, (cost[next_x][eat], eat, next_x))

for i in range(2, v+1):
    print(min(cost[i]))
