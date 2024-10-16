n = int(input())
nums = [0] + list(map(int, input().split()))

dp = [0] * (n+1)
res = -float('INF')

for i in range(1, n+1):
    dp[i] = max(dp[i-1] + nums[i], nums[i])
    res = max(res, dp[i])
print(res)
