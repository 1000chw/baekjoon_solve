import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')
MOD = 1000000009
dx, dy = [2, 2, -2, -2, 1, 1, -1, -1], [1, -1, 1, -1, 2, -2, 2, -2]
r, c = map(int, input().split())
world = [[[0, INF] for _ in range(c+1)] for _ in range(r+1)]
world[1][1] = [1, 0]
pq = [(0, 1, 1)]
while pq:
    d, x, y = heappop(pq)
    if x == r and y == c:
        break
    if world[x][y][1] == d:
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 < nx <= r and 0 < ny <= c:
                if world[nx][ny][1] > d+1:
                    world[nx][ny][1] = d + 1
                    world[nx][ny][0] = world[x][y][0]
                    heappush(pq, (d+1, nx, ny))
                elif world[nx][ny][1] == d+1:
                    world[nx][ny][0] += world[x][y][0]
                    world[nx][ny][0] %= MOD
if world[r][c][1] == INF:
    print('None')
else:
    print(world[r][c][1], world[r][c][0])
