import sys
input = sys.stdin.readline
MOD = 1000000007

dp = [0]*3334
dp[0] = 1
dp[1] = 3

def solve(n):
    if n % 3:
        print(0)
    elif dp[n // 3]:
        print(dp[n//3])
    else:
        for i in range(2, n//3+1):
            if dp[i]:
                continue
            dp[i] = dp[i-1]*3
            dp[i] %= MOD
            for j in range(2, i+1):
                dp[i] += dp[i-j]*j*2
                dp[i] %= MOD
        dp[n//3] %= MOD
        print(dp[n//3])

for _ in range(int(input())):
    solve(int(input()))
