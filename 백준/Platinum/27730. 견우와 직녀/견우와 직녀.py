import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
E = [[] for _ in range(n)]


for i in range(n-1):
    a, b, c = map(int, input().split())
    E[a-1].append((b-1, c))
    E[b-1].append((a-1, c))

m = int(input())
W = [[] for _ in range(m)]
for i in range(m-1):
    a, b, c = map(int, input().split())
    W[a-1].append((b-1, c))
    W[b-1].append((a-1, c))


e_count_node_dp = [0]*n
e_sum_dp = [0]*n
e_visited = [False]*n

w_count_node_dp = [0]*m
w_sum_dp = [0]*m
w_visited = [False]*m


def dfs(node, tree, count_node_dp, sum_dp, visited):
    visited[node] = True
    count, sum_ = 1, 0
    for v, c in tree[node]:
        if not visited[v]:
            cn, s = dfs(v, tree, count_node_dp, sum_dp, visited)
            count += cn
            sum_ += c * cn + s

    count_node_dp[node] = count
    sum_dp[node] = sum_

    return count, sum_

dfs(0, E, e_count_node_dp, e_sum_dp, e_visited)
dfs(0, W, w_count_node_dp, w_sum_dp, w_visited)

e_visited = [False]*n
w_visited = [False]*m

min_e_root, e_sum = 0, e_sum_dp[0]
min_w_root, w_sum = 0, w_sum_dp[0]

e_dp = [0]*n
w_dp = [0]*m

e_dp[0] = e_sum_dp[0]
w_dp[0] = w_sum_dp[0]

def dfs_e(node, parent, edge):
    global min_e_root, e_sum

    e_visited[node] = True

    if node:
        s = e_dp[parent] + (e_count_node_dp[0] - 2 * e_count_node_dp[node]) * edge
        e_dp[node] = s
        if e_sum > s:
            min_e_root, e_sum = node, s

    for v, c in E[node]:
        if not e_visited[v]:
            dfs_e(v, node, c)


def dfs_w(node, parent, edge):
    global min_w_root, w_sum

    w_visited[node] = True

    if node:
        s = w_dp[parent] + (w_count_node_dp[0] - 2 * w_count_node_dp[node]) * edge
        w_dp[node] = s
        if w_sum > s:
            min_w_root, w_sum = node, s

    for v, c in W[node]:
        if not w_visited[v]:
            dfs_w(v, node, c)

dfs_e(0, 0, 0)
dfs_w(0, 0, 0)

print(min_e_root+1, min_w_root+1)
print(e_sum*m + (w_sum + m)*n )

