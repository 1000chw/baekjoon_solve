import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [True] * n
for _ in range(m):
    graph[int(input()) - 1] = False

dp = [[-1] * 150 for _ in range(n)]


def dfs(i, v):
    if v <= 0 or i >= n or not graph[i]:
        return n + 1
    if i == n - 1:
        return 0
    if dp[i][v] == -1:
        dp[i][v] = min(dfs(i + v - 1, v - 1), dfs(i + v, v), dfs(i + v + 1, v + 1)) + 1
    return dp[i][v]


answer = dfs(1, 1)

if answer == n + 1:
    print(-1)
else:
    print(answer+1)
