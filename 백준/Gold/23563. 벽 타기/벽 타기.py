import sys
from queue import PriorityQueue
input = sys.stdin.readline
INF = float('inf')
H, W = map(int, input().split())
Map = [input().strip() for _ in range(H)]
start = [0]
for i in range(H):
    for j in range(W):
        if Map[i][j] == 'S':
            start += [i, j]
            break
    if len(start) != 1:
        break

points = [[INF]*W for _ in range(H)]
points[start[1]][start[2]] = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def isWallClose(i, j):
    for k in range(4):
        if Map[i+dx[k]][j+dy[k]] == '#':
            return True
    return False

q = PriorityQueue()
q.put(start)
res = INF
while q.qsize():
    p, x, y = q.get()
    if points[x][y] != p:
        continue
    if Map[x][y] == 'E':
        res = min(res, p)
    iwc = isWallClose(x, y)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if Map[nx][ny] == '#':
            continue
        if iwc and isWallClose(nx, ny):
            if points[nx][ny] > p:
                points[nx][ny] = p
                q.put([p, nx, ny])
        else:
            if points[nx][ny] > p+1:
                points[nx][ny] = p+1
                q.put([p+1, nx, ny])

print(res)
