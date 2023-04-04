import sys
input = sys.stdin.readline
dx = [0, 0, -1, -1, -1, 1, 1, 1]
dy = [-1 ,1, 0, 1, -1, 0, 1, -1]
while 1:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    maps = []
    visited = [[False]*w for _ in range(h)]
    for i in range(h):
        maps.append(input().split())
    stack = []
    answer = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == '1' and not visited[i][j]:
                answer += 1
                stack.append((i, j))
                while len(stack):
                    x, y = stack.pop()
                    visited[x][y] = True
                    for k in range(8):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == '1' and not visited[nx][ny]:
                            stack.append((nx, ny))
    print(answer)

