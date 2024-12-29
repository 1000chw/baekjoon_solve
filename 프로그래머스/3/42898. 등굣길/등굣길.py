def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    for py, px in puddles:
        dp[px][py] = -1
    dp[1][1] = 1
    sx, sy = 1, 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if dp[i][j]:
                continue
            dp[i][j] = (dp[i-1][j] if dp[i-1][j] != -1 else 0) + (dp[i][j-1] if dp[i][j-1] != -1 else 0)
            dp[i][j] %= 1000000007

    return dp[n][m]