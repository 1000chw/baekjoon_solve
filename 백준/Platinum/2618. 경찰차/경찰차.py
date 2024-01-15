import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
w = int(input())
cases = [(1, 1)] + [tuple(map(int, input().split())) for _ in range(w)] + [(n, n)]

dp = [[-1]*(w+1) for _ in range(w+1)]

def solve(x, y):
    if x == w or y == w:
        return 0

    if dp[x][y] != -1:
        return dp[x][y]

    next_case = max(x, y) + 1
    dist1 = solve(next_case, y) + dist(x, next_case)
    dist2 = solve(x, next_case)
    if y == 0:
        dist2 += dist(w+1, next_case)
    else:
        dist2 += dist(y, next_case)

    dp[x][y] = min(dist1, dist2)
    return dp[x][y]


def dist(i, j):
    return abs(cases[i][0] - cases[j][0]) + abs(cases[i][1] - cases[j][1])


solve(0, 0)

print(dp[0][0])
x, y = 0, 0
while x < w and y < w:
    next_case = max(x, y) + 1
    dist1 = dp[next_case][y] + dist(x, next_case)
    dist2 = dp[x][next_case]
    if y == 0:
        dist2 += dist(w+1, next_case)
    else:
        dist2 += dist(y, next_case)

    if dist1 < dist2:
        print(1)
        x = next_case
    else:
        print(2)
        y = next_case
