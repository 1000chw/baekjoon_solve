import sys
input = sys.stdin. readline

mod = 1000000000
n = int(input())

last = (1 << 10) - 1
dp = [[[0]*(last+1) for _ in range(10)] for _ in range(n+1)]

for i in range(1, 10):
    dp[1][i][1 << i] = 1

for i in range(2, n+1):
    for j in range(10):
        for k in range(last+1):
            if j == 0:
                dp[i][j][k | 1 << j] = (dp[i][j][k | 1 << j] + dp[i-1][1][k]) % mod
            elif j == 9:
                dp[i][j][k | 1 << j] = (dp[i][j][k | 1 << j] + dp[i - 1][8][k]) % mod
            else:
                dp[i][j][k | 1 << j] = (dp[i][j][k | 1 << j] + dp[i - 1][j-1][k] + dp[i - 1][j+1][k]) % mod
                
answer = sum(dp[n][i][last] for i in range(10)) % mod
print(answer)
