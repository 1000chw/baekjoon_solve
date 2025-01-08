import sys
input = sys.stdin.readline
INF = float('inf')

def distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

n = int(input())
points = [[] for _ in range(n+1)]
points[0] = [(0,0), (0,0)]
for i in range(1, n+1):
    x, y = map(int, input().split())
    points[i].append((x, y))
for i in range(1, n+1):
    v, w = map(int, input().split())
    points[i].append((v, w))

points.sort(key=lambda x: x[1][1])

dp = [-INF]*(n+1)
dp[0] = 0
answer = -INF
for i in range(1, n+1):
    for j in range(i):
        dp[i] = max(dp[i], dp[j] + points[i][1][1] - max(distance(points[i][0][0], points[i][0][1], points[j][0][0], points[j][0][1]) + points[j][1][1], points[i][1][0]))
    answer = max(answer, dp[i])
print(answer)
