import sys
input = sys.stdin.readline
INF = float('inf')

n, m = map(int, input().split())
names = []
for i in range(n):
    names.append(int(input()))

dp = [[INF]*n for _ in range(n)]
res = INF
for i in range(n):
    for j in range(i, n):
        if i and dp[i-1][j-1] == INF:
            break
        sumN = 0
        for k in range(j, n):
            if sumN == 0:
                sumN += names[k]
            else:
                sumN += names[k]+1
            if sumN > m:
                break
            if k == n-1:
                if i == 0:
                    res = 0
                else:
                    res = min(res, dp[i-1][j-1])
            if i == 0:
                dp[i][k] = (m-sumN)**2
            else:
                dp[i][k] = min(dp[i][k], dp[i-1][j-1] + (m - sumN)**2)
        if i == 0:
            break

print(res)
