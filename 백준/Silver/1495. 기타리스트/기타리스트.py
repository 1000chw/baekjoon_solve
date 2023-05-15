import sys
input = sys.stdin.readline

N, S, M = map(int, input().split())
v = [0] + list(map(int, input().split()))
dp = [[False]*(M+1) for _ in range(N+1)]
dp[0][S] = True
for i in range(1, N+1):
    for j in range(M+1):
        if j-v[i] >= 0 and dp[i-1][j-v[i]]:
            dp[i][j] = True
        if j+v[i] <= M and dp[i-1][j+v[i]]:
            dp[i][j] = True
chk = True
res = 0
for i in range(M+1):
    if dp[-1][i]:
        res = max(res, i)
        chk = False
if chk:
    print(-1)
else:
    print(res)
