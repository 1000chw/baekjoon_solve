import sys
input = sys.stdin.readline

n = int(input())
dp = [[0]*(n+1) for _ in range(3)]

for i in range(1, n+1):
    r, g, b = map(int, input().split())
    dp[0][i] = min(dp[1][i-1]+r, dp[2][i-1]+r)
    dp[1][i] = min(dp[0][i - 1] + g, dp[2][i - 1] + g)
    dp[2][i] = min(dp[0][i - 1] + b, dp[1][i - 1] + b)
print(min(dp[i][-1] for i in range(3)))