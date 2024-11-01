from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
t = min(k, n//3)
dp = [[0] * n for _ in range(t+1)]
#dp[t][j] = j열에서 t개 뽑을 때 최대값
pq = []

for i in range(n):
    dp1 = [[0] * (n+1) for _ in range(t+1)]
    # dp1[t][j] = j 번째 까지 t 개 묶음 뽑았을 때 최댓값
    nums = [0] + list(map(int, input().split()))
    for j in range(3, n+1):
        x = nums[j] + nums[j-1] + nums[j-2]
        for h in range(1, min(j//3, t)+1):
            dp1[h][j] = max(dp1[h][j-1], dp1[h-1][j-3] + x)
            dp[h][i] = max(dp[h][i], dp1[h][j])

    for h in range(1, t+1):
        heappush(pq, -dp[h][i] + dp[h-1][i])

answer = 0
for _ in range(k):
    if len(pq) == 0:
        break
    answer -= heappop(pq)

print(answer)
