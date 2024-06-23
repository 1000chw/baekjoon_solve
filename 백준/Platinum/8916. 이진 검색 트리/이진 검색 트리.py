import sys
input = sys.stdin.readline

dp = [[]]
lrc, p, c = [], [], []

def makeTree(n, nums):
    global lrc, p, c
    lrc = [[0, 0] for _ in range(n + 1)]
    p = [0] * (n + 1)
    c = [[0, 0] for _ in range(n + 1)]
    for num in nums[1:]:
        P = nums[0]
        cur = nums[0]
        while cur:
            if cur < num:
                lrc[cur][1] += 1
                P = cur
                cur = c[cur][1]
            else:
                lrc[cur][0] += 1
                P = cur
                cur = c[cur][0]
        p[num] = P
        if P > num:
            c[P][0] = num
        else:
            c[P][1] = num

def fact(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def nCr(n, r):
    return fact(n)//(fact(n-r) * fact(r))

def calcChild(root):
    global dp
    if c[root][0] == c[root][1] == 0:
        dp[root] = 1
    elif c[root][0] == 0:
        calcChild(c[root][1])
        dp[root] = dp[c[root][1]]
    elif c[root][1] == 0:
        calcChild(c[root][0])
        dp[root] = dp[c[root][0]]
    else:
        calcChild(c[root][0])
        calcChild(c[root][1])
        dp[root] = (nCr(lrc[root][0]+lrc[root][1], lrc[root][0]) * dp[c[root][0]] * dp[c[root][1]]) % 9999991

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    makeTree(n, nums)
    dp = [0] * (n + 1)
    dp[0] = 1
    calcChild(nums[0])
    print(dp[nums[0]])
