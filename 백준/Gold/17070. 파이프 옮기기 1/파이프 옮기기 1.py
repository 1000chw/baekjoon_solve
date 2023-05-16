import sys
input = sys.stdin.readline
n = int(input())
dp = [[[0]*n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(3):
            if dp[k][i][j]:
                if k == 0:
                    if j+1 <n and not arr[i][j+1]:
                        dp[0][i][j + 1] += dp[k][i][j]
                    if i+1 < n and j + 1 < n and not arr[i+1][j+1] and not arr[i+1][j] and not arr[i][j+1]:
                        dp[2][i + 1][j + 1] += dp[k][i][j]
                elif k == 1:
                    if i + 1 < n and not arr[i+1][j]:
                        dp[1][i+1][j] += dp[k][i][j]
                    if j + 1 < n and i+1<n and not arr[i+1][j+1] and not arr[i+1][j] and not arr[i][j+1]:
                        dp[2][i + 1][j + 1] += dp[k][i][j]
                else:
                    if j+1 < n and not arr[i][j+1]:
                        dp[0][i][j + 1] += dp[k][i][j]
                    if i+1 <n and not arr[i+1][j]:
                        dp[1][i + 1][j] += dp[k][i][j]
                    if i+1 < n and j+1 < n and not arr[i+1][j+1] and not arr[i+1][j] and not arr[i][j+1]:
                        dp[2][i + 1][j+1] += dp[k][i][j]

print(dp[0][n-1][n-1] + dp[1][n-1][n-1] + dp[2][n-1][n-1])
