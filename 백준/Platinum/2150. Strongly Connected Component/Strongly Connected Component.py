import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)

sccs = []
id = 0
ids = [0]*(v+1)
finished = [False]*(v+1)
stack = []

def dfs(v):
    global id

    id += 1
    parent = ids[v] = id
    stack.append(v)

    for u in graph[v]:
        if not ids[u]:
            parent = min(parent, dfs(u))
        elif not finished[u]:
            parent = min(parent, ids[u])

    if ids[v] == parent:
        scc = []
        while stack:
            x = stack.pop()
            scc.append(x)
            finished[x] = True
            if x == v:
                break
        scc.sort()
        scc.append(-1)
        sccs.append(scc)
    return parent


for i in range(1, v+1):
    if not ids[i]:
        dfs(i)

print(len(sccs))
sccs.sort()
for scc in sccs:
    print(*scc)
