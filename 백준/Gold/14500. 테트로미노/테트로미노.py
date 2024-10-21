import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (m+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * (m+2)]
dx, dy = [0, 1, -1], [1, 0, 0]
visited = [[False] * (m+2) for _ in range(n+2)]

answer = 0

def dfs(x, y):
    global answer
    res = 0
    stack = []
    stack.append((x, y, 1, graph[x][y]))
    tmp = []
    while len(stack):
        cx, cy, cnt, s = stack.pop()
        if cnt == 4:
            res = max(res, s)
            visited[cx][cy] = False
            continue
        visited[cx][cy] = True
        if len(tmp) >= cnt:
            for i in range(cnt-1, len(tmp)):
                r, c = tmp.pop()
                visited[r][c] = False
        tmp.append((cx, cy))
        for i in range(3):
            nx, ny = cx + dx[i], cy + dy[i]
            if 1 <= nx <= n and 1 <= ny <= m and not visited[nx][ny]:
                stack.append((nx, ny, cnt+1, s+graph[nx][ny]))
    for r, c in tmp:
        visited[r][c] = False
    answer = max(answer, res)

def oh(i, j):
    global answer
    if (i == 1 and (j == m or j == 1)) or (i == n and (j == m or j == 1)):
        return
    up, down, left, right = graph[i-1][j], graph[i+1][j], graph[i][j-1], graph[i][j+1]
    answer = max(answer, graph[i][j] + up + down + left + right - min(up, down, left, right))


for i in range(1, n+1):
    for j in range(1, m+1):
        visited[i][j] = True
        dfs(i, j)
        oh(i, j)
        visited[i][j] = False

print(answer)
