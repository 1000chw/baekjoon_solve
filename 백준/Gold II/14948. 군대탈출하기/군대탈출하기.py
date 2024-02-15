import sys
from heapq import heappush, heappop
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
INF = float('inf')
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
n, m = map(int, input().split())
army = [list(map(int, input().split())) for _ in range(n)]
visited = [[[INF]*m for _ in range(n)], [[INF]*m for _ in range(n)]]
visited[0][0][0], visited[1][0][0] = army[0][0], army[0][0]
pq = [(army[0][0], 0, 0, 0)]

while pq:
    level, x, y, used = heappop(pq)
    if x == n-1 and y == m-1:
        print(level)
        break
    if visited[used][x][y] == level:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[used][nx][ny] > max(level, army[nx][ny]):
                visited[used][nx][ny] = max(level, army[nx][ny])
                heappush(pq, (visited[used][nx][ny], nx, ny, used))
                nx, ny = nx + dx[i], ny + dy[i]
                if used == 0 and 0 <= nx < n and 0 <= ny < m and visited[1][nx][ny] > max(level, army[nx][ny]):
                    visited[1][nx][ny] = max(level, army[nx][ny])
                    heappush(pq, (visited[1][nx][ny], nx, ny, 1))
