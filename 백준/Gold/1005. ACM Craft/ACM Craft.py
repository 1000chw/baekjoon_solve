import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    costs = [0]+list(map(int, input().split()))
    degrees = [0]*(N+1)
    tree = [[] for _ in range(N+1)]

    for _ in range(K):
        p, c = map(int, input().split())
        degrees[c] += 1
        tree[p].append(c)
    W = int(input())

    stack = []
    sorted_nodes = []
    for i in range(1, N+1):
        if degrees[i] == 0:
            stack.append(i)
    while stack:
        node = stack.pop()
        sorted_nodes.append(node)
        for n in tree[node]:
            degrees[n] -= 1
            if degrees[n] == 0:
                stack.append(n)

    dp = [0]*(N+1)
    for node in sorted_nodes:
        p_cost = dp[node] + costs[node]
        for c_node in tree[node]:
            dp[c_node] = max(dp[c_node], p_cost)
    print(dp[W] + costs[W])
