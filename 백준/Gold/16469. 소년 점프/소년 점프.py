import sys
from queue import Queue
input = sys.stdin.readline
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

r, c = map(int, input().split())
maze = []
for i in range(r):
    maze.append(input())
answer = [[33333]*c for _ in range(r)]
visit3 = [[0]*c for _ in range(r)]
for _ in range(3):
    visited = [[False]*c for _ in range(r)]
    que = Queue()
    a, b = map(lambda k: int(k)-1, input().split())
    que.put((a, b, 0))
    while que.qsize():
        x, y, cnt = que.get()
        if visited[x][y]:
            continue
        visited[x][y] = True
        visit3[x][y] += 1
        if answer[x][y] == 33333:
            answer[x][y] = 0
        answer[x][y] = max(cnt, answer[x][y])
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] == '0' and not visited[nx][ny]:
                que.put((nx, ny, cnt+1))
min_n = 33333
cnt = 0
for i in range(r):
    for j in range(c):
        if visit3[i][j] == 3:
            if min_n > answer[i][j]:
                min_n = answer[i][j]
                cnt = 1
            elif min_n == answer[i][j]:
                cnt += 1
if cnt == 0:
    print(-1)
else:
    print(min_n)
    print(cnt)
