import sys
sys.setrecursionlimit(100000)
s = input()
ls = len(s)

dp = [[0]*ls for _ in range(ls)]

for i in range(ls):
    for j in range(i+1):
        if i == j:
            dp[j][i] = 1
        elif j + 1 == i and s[i] == s[j]:
            dp[j][i] = 1
        elif s[i] == s[j] and dp[j+1][i-1]:
            dp[j][i] = 1


def solve(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if dp[x][y]:
        return dp[x][y]

    min_n = 2500
    for i in range(x, y+1):
        if dp[x][i]:
            min_n = min(min_n, solve(i+1, y) + 1)

    dp[x][y] = min_n
    return min_n

print(solve(0, ls-1))
