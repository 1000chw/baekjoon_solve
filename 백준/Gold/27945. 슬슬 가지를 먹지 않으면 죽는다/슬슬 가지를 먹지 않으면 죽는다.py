import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
visited = [False]*(N+1)
par = [i for i in range(N+1)]

def find(n):
    if par[n] == n:
        return n
    par[n] = find(par[n])
    return par[n]

def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        par[px] = py

for _ in range(M):
    u, v, t = map(int, input().split())
    edges.append((t, u, v))
edges.sort()
cnt = 1
res = 0
for t, u, v in edges:
    if t != cnt:
        res = cnt
        break
    elif visited[u] and visited[v] and find(u) == find(v):
        res = cnt
        break
    else:
        visited[u], visited[v] = True, True
        union(u, v)
        cnt += 1
if res:
    print(res)
else:
    print(cnt)
