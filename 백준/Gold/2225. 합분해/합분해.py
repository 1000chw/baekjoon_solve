n, k = map(int, input().split())
dp = [1]*(n+1)

for i in range(k-1):
    new_dp = [0]*(n+1)
    for j in range(n+1):
        for k in range(j+1):
            new_dp[j] += dp[j-k]
            new_dp[j] %= 1000000000
    dp = new_dp

print(dp[-1])