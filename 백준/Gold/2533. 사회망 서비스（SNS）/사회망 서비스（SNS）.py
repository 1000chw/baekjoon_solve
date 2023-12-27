import sys
from collections import defaultdict
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n = int(input())
visited = [False]*(n+1)
dp = [[0, 0] for _ in range(n+1)]
tree = defaultdict(list)

def min_ea(node):
    visited[node] = True
    dp[node][1] = 1
    for child in tree[node]:
        if visited[child]:
            continue
        min_ea(child)
        dp[node][1] += min(dp[child][0], dp[child][1])
        dp[node][0] += dp[child][1]


for _ in range(n-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

min_ea(1)
print(min(dp[1][0], dp[1][1]))
