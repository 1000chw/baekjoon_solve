import sys
input = sys.stdin. readline

H, W = map(int, input().split())
dp = [[0]*(W+1) for _ in range(W+1)]
result = [[0]*(W+1) for _ in range(H+1)]
result[0][1] = 1

for i in range(1, W + 1):
    for j in range(1, W + 1):
        for k in range(j):
            dp[i][j] += dp[i - 1][j - k] % 1000000007
        dp[i][j] += 1

for day in range(1, H+1):
    for i in range(1, W+1):
        prev_sum = result[day-1][i]
        if not prev_sum:
            continue
        for j in range(1, W+1):
            result[day][j] += (prev_sum*dp[i][j]) % 1000000007
            result[day][j] %= 1000000007

print(sum(result[H]) % 1000000007)
