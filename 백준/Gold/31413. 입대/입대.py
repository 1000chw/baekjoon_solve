import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = float('inf')
N, M = map(int, input().split())
points = [0] + list(map(int, input().split()))
A, D = map(int, input().split())
points += [0]*D

dp = [[0]*(N+D) for _ in range(N//D+2)]

for cnt in range(N//D+2):
    for i in range(1, N+D):
        if cnt == 0:
            dp[cnt][i] = dp[cnt][i-1] + points[i]
        elif i < cnt * D:
            continue
        else:
            dp[cnt][i] = max(dp[cnt-1][i-D]+A, dp[cnt][i-1]+points[i])

chk = False
for i in range(N//D+2):
    if dp[i][N+D-1] >= M:
        print(i)
        chk = True
        break
if not chk:
    print(-1)


