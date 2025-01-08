import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n)]

max_node_d = {}

for i in range(n-1):
    a, b, c = map(int, input().split())
    tree[a-1].append((b-1, c))
    tree[b-1].append((a-1, c))
    max_node_d[a - 1] = []
    max_node_d[b - 1] = []

visited = [False] * n
dp = [0] * n

def dfs(node):
    visited[node] = True
    max_d, nn = 0, [0, 0]
    for n, v in tree[node]:
        if not visited[n]:
            d = dfs(n)
            if max_d < d + v:
                max_d = d + v
            if nn[1] < d + v:
                nn[1] = d + v
            if nn[0] < nn[1]:
                nn[0], nn[1] = nn[1], nn[0]

    max_node_d[node] = nn
    dp[node] = max_d

    return max_d

dfs(0)

visited = [False] * n

def dfs2(par, node, w):
    visited[node] = True
    if node:
        nd = 0
        if max_node_d[par][0] == dp[node] + w:
            nd = max_node_d[par][1] + w
        else:
            nd = max_node_d[par][0] + w

        if max_node_d[node][1] < nd:
            max_node_d[node][1] = nd
        if max_node_d[node][0] < max_node_d[node][1]:
            max_node_d[node][0], max_node_d[node][1] = max_node_d[node][1], max_node_d[node][0]

        dp[node] = max_node_d[node][0]

    for n, v in tree[node]:
        if not visited[n]:
            dfs2(node, n, v)

dfs2(0, 0, 0)


for d in dp:
    print(d)