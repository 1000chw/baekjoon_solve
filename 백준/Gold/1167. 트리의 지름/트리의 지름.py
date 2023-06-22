import sys
input = sys.stdin.readline

def dfs(node, costss):
    global max_cost
    global max_node

    if costss > max_cost:
        max_cost = costss
        max_node = node
    visited[node] = True
    for i, cost in tree[node]:
        if not visited[i]:
            dfs(i, costss+cost)
    visited[node] = False


V = int(input())

tree = [[] for _ in range(V+1)]
max_cost = 0
max_node = 0
visited = [False]*(V+1)

for _ in range(V):
    t = list(map(int, input().split()))
    node = t.pop(0)
    chk = True

    for i in range(len(t)):
        if t[i] == -1:
            break
        if chk:
            tree[node].append((t[i], t[i+1]))
        chk = not chk

res = 0
dfs(1, 0)
dfs(max_node, 0)
print(max_cost)
