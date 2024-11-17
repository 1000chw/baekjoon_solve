import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]


def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > graph[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]


answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)