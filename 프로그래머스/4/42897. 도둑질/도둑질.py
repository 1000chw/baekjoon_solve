import sys

sys.setrecursionlimit(100000000)


def solution(money):
    answer = 0
    lm = len(money)

    def solve(l, r):
        dp = [0]*(lm+2)
        for i in range(l+2, r+3):
            dp[i] = max(dp[i-2] + money[i-2], dp[i-1])

        return dp[r+2]

    
    answer = max(answer, solve(0, lm - 2), solve(1, lm - 1))

    return answer