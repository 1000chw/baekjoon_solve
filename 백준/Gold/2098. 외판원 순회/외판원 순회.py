import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def tsp(cur, visited):
    if visited == M:
        if graph[cur][0] == 0:
            return INF
        return graph[cur][0]

    if dp[visited][cur] != -1:
        return dp[visited][cur]

    answer = INF
    for i in range(n):
        _next = visited | 1 << i
        if _next == visited or not graph[cur][i]:
            continue
        answer = min(answer, tsp(i, _next) + graph[cur][i])
    dp[visited][cur] = answer
    return dp[visited][cur]


n = int(input())
INF = float('inf')
M = (1 << n) - 1
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(M+1)]

print(tsp(0, 1))



