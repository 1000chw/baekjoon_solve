import sys
from collections import deque
input = sys.stdin.readline
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
T = int(input())
for _ in range(T):
    r, c = map(int, input().split())
    ground = []
    for i in range(r):
        ground.append(input())
    visited = [[False]*c for _ in range(r)]
    answer = 0
    for i in range(r):
        for j in range(c):
            if ground[i][j] == '#' and not visited[i][j]:
                stack = deque()
                stack.append((i, j))
                while stack:
                    x, y = stack.pop()
                    if visited[x][y]:
                        continue
                    visited[x][y] = True
                    for d in range(4):
                        nx = dx[d] + x
                        ny = dy[d] + y
                        if 0 <= nx < r and 0 <= ny < c and ground[nx][ny] == '#' and not visited[nx][ny]:
                            stack.append((nx, ny))
                answer += 1
    print(answer)
